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
    name = request.GET.get('name')
    
    if name:
        countries = [c for c in countries if c.get('name', '').lower() == name.lower()]
    
    return JsonResponse({'countries': countries})

# def get_states(request):
#     country_id = request.GET.get('country_id')
#     states = load_json_file('states.json')
#     filtered = [s for s in states if str(s['country_id']) == str(country_id)]
#     return JsonResponse({'states': filtered})
def get_states(request):
    country_name = request.GET.get('country')

    if not country_name:
        return JsonResponse({'error': 'Country name is required as query param (?country=India)'}, status=400)

    states_data = load_json_file('states.json')
    states = [state for state in states_data if state.get('country_name') == country_name]

    return JsonResponse({'states': states})
def get_cities(request):
    country_name = request.GET.get('country')
    state_name = request.GET.get('state')

    if not country_name or not state_name:
        return JsonResponse({'error': 'Both country and state query parameters are required (?country=India&state=Maharashtra)'}, status=400)

    cities_data = load_json_file('cities.json')
    cities = [
        city for city in cities_data
        if city.get('country_name') == country_name and city.get('state_name') == state_name
    ]

    return JsonResponse({'cities': cities})


