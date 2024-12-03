from django.shortcuts import render
from django.http import HttpResponse
import urllib.request 
import json
import requests  # Use requests instead of urllib for better readability and error handling


def index(request):
    data = {}
    
    if request.method == 'POST':
        city = request.POST.get('city')  # Get city from the form input
        '''api_key = 'appid=http%3A%2F%2Fapi.openweathermap.org%2Fdata%2F2.5%2Fweather%3Fq+%3DChennai%26appid+%3D+c46a37d2a9013913629a38ea42b426fb'''
          # Replace with your valid OpenWeatherMap API key
        api_key = 'f272d8b7f1bc2ff0dd3026438baf1fa6'
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        # Correctly format the request URL
        response = requests.get(base_url, params={'q': city, 'appid': api_key})

        if response.status_code == 200:
            weather_data = response.json()

            # Prepare data to pass to the template
            data = {
                "city": city,
                "country_code": weather_data['sys']['country'],
                "coordinate": f"{weather_data['coord']['lon']} {weather_data['coord']['lat']}",
                "temp": f"{weather_data['main']['temp']} K",
                "pressure": weather_data['main']['pressure'],
                "humidity": weather_data['main']['humidity'],
                "description": weather_data['weather'][0]['description'],
            }
        else:
            data = {"error": f"Error {response.status_code}: {response.reason}"}

    return render(request, "main/index.html", {"data": data})
