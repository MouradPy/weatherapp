import urllib.request
import json
import os
import requests
from django.shortcuts import render


api_key = os.environ.get('API_KEY')


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +
                              city + '&units=metric&appid=' + api_key, timeout=1)
        # list_of_data = json.loads(source)
        list_of_data = source.json()

        # print(list_of_data['name'])
        data = {
            "city": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data['city'])
    else:
        data = {}

    return render(request, "main/index.html", data)


# def index(request):

#     if request.method == 'POST':
#         city = request.POST['city']

#         source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
#                                         city + '&units=metric&appid=182d8f0e74df7728f510e7e39ee8b2e0').read()
#         list_of_data = json.loads(source)
#         # print(list_of_data['name'])
#         data = {
#             "city": str(list_of_data['name']),
#             "country_code": str(list_of_data['sys']['country']),
#             "coordinate": str(list_of_data['coord']['lon']) + ', '
#             + str(list_of_data['coord']['lat']),

#             "temp": str(list_of_data['main']['temp']) + ' °C',
#             "pressure": str(list_of_data['main']['pressure']),
#             "humidity": str(list_of_data['main']['humidity']),
#             'main': str(list_of_data['weather'][0]['main']),
#             'description': str(list_of_data['weather'][0]['description']),
#             'icon': list_of_data['weather'][0]['icon'],
#         }
#         print(data['city'])
#     else:
#         data = {}

#     return render(request, "main/index.html", data)
