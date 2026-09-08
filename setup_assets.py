"""
setup_assets.py
Generates realistic agricultural field photography visuals,
crop leaf samples, and UI banners for the Django application.
"""

import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLES_DIR = os.path.join(BASE_DIR, 'static', 'images', 'samples')
ASSETS_DIR = os.path.join(BASE_DIR, 'static', 'images', 'assets')

os.makedirs(SAMPLES_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def generate_field_hero():
    """Generates a realistic agriculture field landscape banner."""
    w, h = 1300, 480
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    # Sky gradient (Soft dawn blue to warm sun golden haze)
    for y in range(int(h * 0.45)):
        ratio = y / (h * 0.45)
        r = int(185 * (1 - ratio) + 235 * ratio)
        g = int(220 * (1 - ratio) + 245 * ratio)
        b = int(245 * (1 - ratio) + 225 * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Distant tree line / horizon
    horizon_y = int(h * 0.42)
    for x in range(0, w, 2):
        tree_h = int(18 + 12 * math.sin(x / 40.0) + 8 * math.cos(x / 15.0))
        draw.line([(x, horizon_y - tree_h), (x, horizon_y + 10)], fill=(45, 95, 60), width=2)

    # Lush green agricultural field rows with perspective
    for y in range(horizon_y, h):
        ratio = (y - horizon_y) / float(h - horizon_y)
        # Deep lush emerald paddy green
        r = int(35 * (1 - ratio) + 25 * ratio)
        g = int(125 * (1 - ratio) + 165 * ratio)
        b = int(45 * (1 - ratio) + 55 * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Field furrows & vibrant crop textures
    np.random.seed(42)
    for row_y in range(horizon_y + 10, h, 8):
        scale = (row_y - horizon_y) / float(h - horizon_y)
        stroke_w = max(1, int(scale * 4))
        for x in range(0, w, int(max(4, 16 * (1 - scale*0.5)))):
            jitter = int(np.random.uniform(-4, 4))
            draw.line([(x, row_y + jitter), (x + 8, row_y - int(scale * 12) + jitter)], 
                      fill=(int(60 + scale * 40), int(160 + scale * 50), int(60)), width=stroke_w)

    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    img.save(os.path.join(ASSETS_DIR, 'hero_field.jpg'), quality=95)
    print("hero_field.jpg generated successfully!")

def generate_crop_thumbnails():
    """Generates realistic field thumbnails for Rice and Jute crop selector cards."""
    # Rice field card
    r_img = Image.new("RGB", (200, 200), (46, 125, 50))
    r_draw = ImageDraw.Draw(r_img)
    for y in range(200):
        ratio = y / 200.0
        r_draw.line([(0, y), (200, y)], fill=(int(35 + 25*ratio), int(115 + 45*ratio), int(45 + 15*ratio)))
    for x in range(10, 190, 8):
        for y in range(40, 190, 15):
            r_draw.line([(x, y), (x + 4, y - 25)], fill=(129, 199, 132), width=2)
            r_draw.ellipse([x+2, y-30, x+6, y-22], fill=(230, 210, 110)) # Golden grain head
    r_img.save(os.path.join(ASSETS_DIR, 'rice_thumb.jpg'), quality=95)

    # Jute field card
    j_img = Image.new("RGB", (200, 200), (27, 94, 32))
    j_draw = ImageDraw.Draw(j_img)
    for y in range(200):
        ratio = y / 200.0
        j_draw.line([(0, y), (200, y)], fill=(int(20 + 20*ratio), int(90 + 40*ratio), int(35 + 15*ratio)))
    for x in range(15, 185, 18):
        j_draw.line([(x, 190), (x, 25)], fill=(139, 195, 74), width=3) # Tall jute stalk
        for ly in range(40, 180, 25):
            j_draw.ellipse([x - 18, ly - 8, x + 4, ly + 8], fill=(76, 175, 80))
            j_draw.ellipse([x - 4, ly - 8, x + 18, ly + 8], fill=(76, 175, 80))
    j_img.save(os.path.join(ASSETS_DIR, 'jute_thumb.jpg'), quality=95)

def create_base_leaf(width=450, height=450, leaf_type="rice"):
    img = Image.new("RGB", (width, height), (250, 252, 250))
    draw = ImageDraw.Draw(img)
    cx, cy = width // 2, height // 2

    if leaf_type == "rice":
        pts = [
            (cx - 36, cy + 185), (cx - 52, cy + 40), (cx - 38, cy - 80),
            (cx - 15, cy - 180), (cx, cy - 200), (cx + 15, cy - 180),
            (cx + 38, cy - 80), (cx + 52, cy + 40), (cx + 36, cy + 185),
            (cx, cy + 200)
        ]
        draw.polygon(pts, fill=(58, 142, 60))
        for off in range(-32, 33, 5):
            draw.line([(cx + off, cy + 185), (cx + int(off * 0.4), cy - 180)], fill=(76, 175, 80), width=1)
        draw.line([(cx, cy + 200), (cx, cy - 195)], fill=(129, 199, 132), width=3)
    else:
        pts = [
            (cx, cy + 180), (cx - 45, cy + 135), (cx - 90, cy + 50),
            (cx - 105, cy - 30), (cx - 80, cy - 110), (cx - 40, cy - 165),
            (cx, cy - 190), (cx + 40, cy - 165), (cx + 80, cy - 110),
            (cx + 105, cy - 30), (cx - 90, cy + 50), (cx + 45, cy + 135)
        ]
        draw.polygon(pts, fill=(46, 125, 50))
        draw.line([(cx, cy + 180), (cx, cy - 185)], fill=(102, 187, 106), width=3)
        for vy in range(cy + 120, cy - 130, -30):
            draw.line([(cx, vy), (cx - 75, vy - 30)], fill=(76, 175, 80), width=2)
            draw.line([(cx, vy), (cx + 75, vy - 30)], fill=(76, 175, 80), width=2)

    return img, draw, cx, cy

def generate_samples():
    # Rice Blast
    img, draw, cx, cy = create_base_leaf(450, 450, "rice")
    lesions = [(cx - 8, cy - 40, 22, 50), (cx + 10, cy + 40, 18, 44), (cx - 12, cy + 90, 15, 34), (cx + 4, cy - 110, 14, 30)]
    for lx, ly, rw, rh in lesions:
        draw.ellipse([lx - rw - 8, ly - rh - 8, lx + rw + 8, ly + rh + 8], fill=(195, 175, 50))
        draw.ellipse([lx - rw, ly - rh, lx + rw, ly + rh], fill=(120, 50, 20))
        draw.ellipse([lx - rw//2, ly - rh//2, lx + rw//2, ly + rh//2], fill=(215, 215, 210))
    img.save(os.path.join(SAMPLES_DIR, "rice_blast.jpg"), quality=95)

    # Rice Blight
    img, draw, cx, cy = create_base_leaf(450, 450, "rice")
    for y in range(cy - 170, cy + 110, 4):
        wave = int(12 * math.sin(y / 18.0)) + 26
        lx = cx - 44 + wave // 2
        draw.line([(lx, y), (cx - 50, y)], fill=(218, 195, 115), width=3)
    img.save(os.path.join(SAMPLES_DIR, "rice_bacterial_blight.jpg"), quality=95)

    # Rice Brown Spot
    img, draw, cx, cy = create_base_leaf(450, 450, "rice")
    np.random.seed(42)
    for _ in range(50):
        sx = int(np.random.normal(cx, 16))
        sy = int(np.random.uniform(cy - 140, cy + 150))
        r = np.random.uniform(3, 7)
        draw.ellipse([sx - r - 2, sy - r - 2, sx + r + 2, sy + r + 2], fill=(185, 175, 45))
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(85, 35, 15))
    img.save(os.path.join(SAMPLES_DIR, "rice_brown_spot.jpg"), quality=95)

    # Rice Tungro
    img, draw, cx, cy = create_base_leaf(450, 450, "rice")
    for y in range(cy - 190, cy + 70):
        ratio = max(0.0, 1.0 - (y - (cy - 190)) / 220.0)
        r = int(58 * (1 - ratio) + 245 * ratio)
        g = int(142 * (1 - ratio) + 160 * ratio)
        b = int(60 * (1 - ratio) + 20 * ratio)
        w_y = int(40 * (1.0 - abs(y - cy) / 210.0))
        draw.line([(cx - w_y, y), (cx + w_y, y)], fill=(r, g, b), width=2)
    img.save(os.path.join(SAMPLES_DIR, "rice_tungro.jpg"), quality=95)

    # Rice Healthy
    img, draw, cx, cy = create_base_leaf(450, 450, "rice")
    img.save(os.path.join(SAMPLES_DIR, "rice_healthy.jpg"), quality=95)

    # Jute Cercospora
    img, draw, cx, cy = create_base_leaf(450, 450, "jute")
    np.random.seed(101)
    for _ in range(25):
        jx = int(np.random.uniform(cx - 70, cx + 70))
        jy = int(np.random.uniform(cy - 110, cy + 100))
        r = np.random.uniform(7, 13)
        draw.ellipse([jx - r - 3, jy - r - 3, jx + r + 3, jy + r + 3], fill=(160, 150, 40))
        draw.ellipse([jx - r, jy - r, jx + r, jy + r], fill=(130, 40, 25))
        draw.ellipse([jx - r*0.5, jy - r*0.5, jx + r*0.5, jy + r*0.5], fill=(200, 195, 190))
    img.save(os.path.join(SAMPLES_DIR, "jute_cercospora.jpg"), quality=95)

    # Jute Golden Mosaic
    img, draw, cx, cy = create_base_leaf(450, 450, "jute")
    np.random.seed(88)
    for _ in range(35):
        mx = int(np.random.uniform(cx - 80, cx + 80))
        my = int(np.random.uniform(cy - 130, cy + 110))
        rw, rh = np.random.uniform(14, 26), np.random.uniform(10, 22)
        draw.ellipse([mx - rw, my - rh, mx + rw, my + rh], fill=(240, 205, 45))
        draw.ellipse([mx - rw*0.6, my - rh*0.6, mx + rw*0.6, my + rh*0.6], fill=(255, 230, 80))
    img.save(os.path.join(SAMPLES_DIR, "jute_golden_mosaic.jpg"), quality=95)

    # Jute Stem Rot
    img, draw, cx, cy = create_base_leaf(450, 450, "jute")
    for sy in range(cy + 35, cy + 165, 4):
        rw = int(20 + 8 * math.sin(sy / 12.0))
        draw.ellipse([cx - rw, sy - 8, cx + rw, sy + 8], fill=(45, 30, 25))
    draw.ellipse([cx - 35, cy - 25, cx + 20, cy + 40], fill=(65, 40, 30))
    img.save(os.path.join(SAMPLES_DIR, "jute_stem_rot.jpg"), quality=95)

    # Jute Healthy
    img, draw, cx, cy = create_base_leaf(450, 450, "jute")
    img.save(os.path.join(SAMPLES_DIR, "jute_healthy.jpg"), quality=95)
    print("All sample images generated successfully!")

if __name__ == "__main__":
    generate_field_hero()
    generate_crop_thumbnails()
    generate_samples()
