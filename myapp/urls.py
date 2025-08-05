from django.urls import path
from . import views

urlpatterns = [
    path('api/countries/', views.get_all_countries, name='get_all_countries'),
    path('api/states/', views.get_states, name='get_states'),
    path('api/cities/', views.get_cities, name='get_cities'),
]
