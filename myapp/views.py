from django.shortcuts import render

# Create your views here.
import json
import os
from django.http import JsonResponse
from django.conf import settings

# Helper function to load JSON
def load_json_file(filename):
    filepath = os.path.join(settings.BASE_DIR, 'myapp', 'data', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_all_countries(request):
    countries = load_json_file('countries.json')
    return JsonResponse({'countries': countries})

def get_states(request):
    country_id = request.GET.get('country_id')
    states = load_json_file('states.json')
    filtered = [s for s in states if str(s['country_id']) == str(country_id)]
    return JsonResponse({'states': filtered})

def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = load_json_file('cities.json')
    filtered = [c for c in cities if str(c['state_id']) == str(state_id)]
    return JsonResponse({'cities': filtered})

def location_form(request):
    return render(request, 'location_form.html')
