from django.db import models

class DiagnosisRecord(models.Model):
    CROP_CHOICES = [
        ('rice', 'Rice (ধান)'),
        ('jute', 'Jute (পাট)'),
    ]

    crop_type = models.CharField(max_length=20, choices=CROP_CHOICES, default='rice')
    image = models.ImageField(upload_to='diagnoses/', null=True, blank=True)
    disease_id = models.CharField(max_length=64)
    disease_name_bn = models.CharField(max_length=128)
    disease_name_en = models.CharField(max_length=128)
    confidence = models.FloatField(default=0.0)
    soil_health_score = models.FloatField(default=0.0)
    nitrogen = models.FloatField(default=0.0)
    phosphorus = models.FloatField(default=0.0)
    potassium = models.FloatField(default=0.0)
    soil_ph = models.FloatField(default=0.0)
    previous_crop = models.CharField(max_length=64, default='boro_rice')
    land_unit = models.CharField(max_length=32, default='bigha')
    land_amount = models.FloatField(default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Diagnosis Record'
        verbose_name_plural = 'Diagnosis Records'

    def __str__(self):
        return f"{self.crop_type.capitalize()} - {self.disease_name_en} ({self.confidence}%) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
