"""
views.py
Django Views for Smart Crop Disease Detection & Soil Advisory Platform.
"""

import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .services.data_store import DISEASE_DATABASE, BARC_BENCHMARKS, PREVIOUS_CROPS
from .services.soil_analyzer import analyze_soil
from .services.disease_soil_linker import link_disease_to_soil
from .services.advisory_generator import generate_full_advisory
from .services.model_engine import analyze_leaf_image
from .models import DiagnosisRecord

def index(request):
    """Main agricultural advisory dashboard."""
    context = {
        'barc_benchmarks': BARC_BENCHMARKS,
        'previous_crops': PREVIOUS_CROPS,
        'diseases': DISEASE_DATABASE,
    }
    return render(request, 'index.html', context)

def about(request):
    """System architecture and methodology overview."""
    return render(request, 'about.html')

def find_sample_file_bytes(samples_dir, sample_name_or_preset):
    """
    Smart file finder: Resolves sample image with ANY extension (.png, .jpg, .jpeg, .webp, .jfif, etc.)
    Handles hidden extensions in Windows and case differences.
    """
    if not sample_name_or_preset or not os.path.exists(samples_dir):
        return None, None
        
    base_target = os.path.splitext(os.path.basename(sample_name_or_preset))[0].lower().strip()
    
    # 1. Check exact filename
    exact_path = os.path.join(samples_dir, os.path.basename(sample_name_or_preset))
    if os.path.isfile(exact_path):
        try:
            with open(exact_path, 'rb') as f:
                return f.read(), os.path.basename(exact_path)
        except Exception:
            pass

    # 2. Check by base name with any valid image extension
    allowed_exts = ['.jpg', '.jpeg', '.png', '.webp', '.jfif', '.bmp']
    try:
        files = os.listdir(samples_dir)
    except Exception:
        files = []

    for fname in files:
        f_base, f_ext = os.path.splitext(fname)
        if f_base.lower() == base_target and f_ext.lower() in allowed_exts:
            t_path = os.path.join(samples_dir, fname)
            try:
                with open(t_path, 'rb') as f:
                    return f.read(), fname
            except Exception:
                continue

    # 3. Fuzzy prefix match
    for fname in files:
        if fname.lower().startswith(base_target):
            t_path = os.path.join(samples_dir, fname)
            if os.path.isfile(t_path):
                try:
                    with open(t_path, 'rb') as f:
                        return f.read(), fname
                except Exception:
                    continue

    return None, None

def api_samples(request):
    """
    Dynamically scans static/images/samples directory and returns
    actual filenames currently on disk (.png, .jpg, .jpeg, .webp),
    so real user photos never break the UI!
    """
    samples_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'samples')
    presets = [
        {"preset": "rice_blast", "crop": "rice", "name_bn": "ধানের ব্লাস্ট রোগ", "name_en": "Rice Leaf Blast", "default": "rice_blast.jpg"},
        {"preset": "rice_bacterial_blight", "crop": "rice", "name_bn": "ধানের পাতা পোড়া (BLB)", "name_en": "Bacterial Leaf Blight", "default": "rice_bacterial_blight.jpg"},
        {"preset": "rice_brown_spot", "crop": "rice", "name_bn": "ধানের বাদামী দাগ", "name_en": "Rice Brown Spot", "default": "rice_brown_spot.jpg"},
        {"preset": "rice_tungro", "crop": "rice", "name_bn": "ধানের টুংরো রোগ", "name_en": "Rice Tungro", "default": "rice_tungro.jpg"},
        {"preset": "rice_healthy", "crop": "rice", "name_bn": "সুস্থ ধান পাতা", "name_en": "Healthy Rice Leaf", "default": "rice_healthy.jpg"},
        {"preset": "jute_cercospora", "crop": "jute", "name_bn": "পাটের সারকোস্পোরা দাগ", "name_en": "Jute Cercospora Spot", "default": "jute_cercospora.jpg"},
        {"preset": "jute_golden_mosaic", "crop": "jute", "name_bn": "পাটের হলুদ মোজাইক", "name_en": "Jute Golden Mosaic", "default": "jute_golden_mosaic.jpg"},
        {"preset": "jute_stem_rot", "crop": "jute", "name_bn": "পাটের কান্ড পচা রোগ", "name_en": "Jute Stem Rot", "default": "jute_stem_rot.jpg"},
        {"preset": "jute_healthy", "crop": "jute", "name_bn": "সুস্থ পাট পাতা", "name_en": "Healthy Jute Leaf", "default": "jute_healthy.jpg"}
    ]

    actual_files = os.listdir(samples_dir) if os.path.exists(samples_dir) else []
    results = []
    for item in presets:
        found_filename = item["default"]
        target = item["preset"].lower()
        for f in actual_files:
            f_base, f_ext = os.path.splitext(f)
            if f_base.lower() == target and f_ext.lower() in ['.jpg', '.jpeg', '.png', '.webp', '.jfif', '.bmp']:
                found_filename = f
                break
        results.append({
            "id": found_filename,
            "crop": item["crop"],
            "name_bn": item["name_bn"],
            "name_en": item["name_en"],
            "preset": item["preset"]
        })

    return JsonResponse({"status": "success", "samples": results})

@csrf_exempt
def api_diagnose(request):
    """
    Main Diagnostic & Advisory Endpoint.
    Accepts: leaf image file upload OR demo sample, crop type, soil NPK values, previous crop, land specs.
    Supports any real user leaf image with automatic format detection.
    """
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "POST method required"}, status=405)

    try:
        crop_type = request.POST.get('crop', 'rice').strip().lower()
        if crop_type not in ['rice', 'jute']:
            crop_type = 'rice'

        n_val = float(request.POST.get('nitrogen', 48.0 if crop_type == 'rice' else 42.0))
        p_val = float(request.POST.get('phosphorus', 16.0 if crop_type == 'rice' else 15.0))
        k_val = float(request.POST.get('potassium', 0.14 if crop_type == 'rice' else 0.16))
        ph_val = float(request.POST.get('ph', 5.6 if crop_type == 'rice' else 6.2))
        prev_crop = request.POST.get('prev_crop', 'boro_rice' if crop_type == 'rice' else 'potato')
        land_unit = request.POST.get('land_unit', 'bigha')
        land_amount = float(request.POST.get('land_amount', 1.0))

        preset_class = request.POST.get('preset_class', None)
        sample_file = request.POST.get('sample_file', None)

        image_bytes = None
        samples_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'samples')

        # 1. Direct file upload from user
        if 'image' in request.FILES:
            uploaded = request.FILES['image']
            image_bytes = uploaded.read()
        
        # 2. Sample file resolution (supports .png, .jpg, .jpeg, .webp, etc.)
        if not image_bytes and sample_file:
            image_bytes, _ = find_sample_file_bytes(samples_dir, sample_file)

        # 3. Preset class lookup
        if not image_bytes and preset_class:
            image_bytes, _ = find_sample_file_bytes(samples_dir, preset_class)

        # 4. Fallback to default sample
        if not image_bytes:
            def_target = "rice_blast" if crop_type == "rice" else "jute_cercospora"
            image_bytes, _ = find_sample_file_bytes(samples_dir, def_target)

        if not image_bytes:
            return JsonResponse({
                "status": "error",
                "message": "চিত্র লোড করা সম্ভব হয়নি। অনুগ্রহ করে একটি বৈধ ছবি ফাইল আপলোড করুন (JPG/PNG)।"
            }, status=400)

        # Step 1 & 2: CNN Inference + Grad-CAM Explainability
        ai_res = analyze_leaf_image(image_bytes, crop_type, preset_class)
        detected_disease = ai_res["primary_class"]

        # Step 3 & 4: BARC Soil Health Score & Element Evaluation
        soil_res = analyze_soil(crop_type, n_val, p_val, k_val, ph_val, prev_crop)

        # Step 3: Rule-Based Disease-Soil Linking
        link_res = link_disease_to_soil(detected_disease, soil_res, crop_type)

        # Step 5: Advisory & Prescription
        advisory_res = generate_full_advisory(
            detected_disease,
            soil_res,
            link_res,
            crop_type,
            land_unit,
            land_amount
        )

        # Save to database record for history
        try:
            DiagnosisRecord.objects.create(
                crop_type=crop_type,
                disease_id=detected_disease,
                disease_name_bn=ai_res['primary_name_bn'],
                disease_name_en=ai_res['primary_name_en'],
                confidence=ai_res['primary_confidence'],
                soil_health_score=soil_res['final_score'],
                nitrogen=n_val,
                phosphorus=p_val,
                potassium=k_val,
                soil_ph=ph_val,
                previous_crop=prev_crop,
                land_unit=land_unit,
                land_amount=land_amount
            )
        except Exception:
            pass # Keep advisory working even if DB is unmigrated

        return JsonResponse({
            "status": "success",
            "ai_detection": ai_res,
            "soil_analysis": soil_res,
            "disease_soil_link": link_res,
            "advisory": advisory_res
        })

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@csrf_exempt
def api_recalculate_soil(request):
    """Live interactive recalculation when user tweaks sliders."""
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "POST method required"}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8')) if request.body else {}
        crop_type = data.get('crop', 'rice').lower()
        n_val = float(data.get('nitrogen', 35.0))
        p_val = float(data.get('phosphorus', 18.0))
        k_val = float(data.get('potassium', 0.22))
        ph_val = float(data.get('ph', 6.2))
        prev_crop = data.get('prev_crop', 'aman_rice')
        disease_id = data.get('disease_id', 'rice_blast')
        land_unit = data.get('land_unit', 'bigha')
        land_amount = float(data.get('land_amount', 1.0))

        soil_res = analyze_soil(crop_type, n_val, p_val, k_val, ph_val, prev_crop)
        link_res = link_disease_to_soil(disease_id, soil_res, crop_type)
        advisory_res = generate_full_advisory(
            disease_id,
            soil_res,
            link_res,
            crop_type,
            land_unit,
            land_amount
        )

        return JsonResponse({
            "status": "success",
            "soil_analysis": soil_res,
            "disease_soil_link": link_res,
            "advisory": advisory_res
        })
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)

def api_history(request):
    """Returns recent diagnosis records."""
    records = DiagnosisRecord.objects.all()[:10]
    data = []
    for r in records:
        data.append({
            "id": r.id,
            "crop": r.crop_type,
            "disease_en": r.disease_name_en,
            "disease_bn": r.disease_name_bn,
            "confidence": r.confidence,
            "soil_score": r.soil_health_score,
            "created_at": r.created_at.strftime("%d %b %Y, %I:%M %p")
        })
    return JsonResponse({"status": "success", "history": data})
