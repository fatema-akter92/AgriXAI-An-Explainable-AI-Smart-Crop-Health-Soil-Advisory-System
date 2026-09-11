from django.urls import path
from . import views

app_name = 'advisor'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('api/samples/', views.api_samples, name='api_samples'),
    path('api/diagnose/', views.api_diagnose, name='api_diagnose'),
    path('api/recalculate-soil/', views.api_recalculate_soil, name='api_recalculate_soil'),
    path('api/history/', views.api_history, name='api_history'),
]
