from django.contrib import admin
from .models import DiagnosisRecord

@admin.register(DiagnosisRecord)
class DiagnosisRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'crop_type', 'disease_name_en', 'confidence', 'soil_health_score', 'created_at')
    list_filter = ('crop_type', 'created_at')
    search_fields = ('disease_name_en', 'disease_name_bn', 'disease_id')
    readonly_fields = ('created_at',)
