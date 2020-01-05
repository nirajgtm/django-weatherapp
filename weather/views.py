from django.shortcuts import render
import requests
import json
from .searchForm import searchForm
# Create your views here.

def index(request):
    searchForms = searchForm()
    city= None
    if (request.method == 'GET'):
        cityQuery = request.GET.get('cityQuery')
        if cityQuery is not None:
            city = cityQuery.upper()
    if city is None:
        try:
            send_url = "http://api.ipstack.com/check?access_key=9a003dcb361e37837550e3aa73de8600"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            city = geo_json['city'].upper()
            # city = "ann arbor".upper()
        except:
            city = "United States"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=86d48cf453c11818fc62ec0c40ffdb20"
    try:
        response = requests.get(url.format(city))
        response = json.loads(response.text)
        description = response['weather'][0]['description']
        temperature = str(round(response['main']['temp'])) + "° C"
        feelsLike = "Feels like " + str(round(response['main']['feels_like'])) + "° C"
        
    except Exception:
        print(Exception)
        description = "Please check your city name and make sure you are online. If you are still facing problems, please send me a feedback"
        response = ""
        response = ""
        temperature = ""
        feelsLike = ""
    imageURL = "https://source.unsplash.com/1600x900/?" + description.replace(" ", "%20") 
    # print("The image URL is" + )

    
    # print("city is {}",format(city))
    # print(response)
    return render (request, 'weather/weather.html', { 'city' : city, 'description': description.capitalize(), 'temperature' : temperature.capitalize(), 'feelsLike' : feelsLike.capitalize(), "imageURL": imageURL, "searchForms" : searchForms})