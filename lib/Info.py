import requests

# get weather api
def get_weather_by_city(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "appid=bd45fc9db8849cb46d00a451483ccd44"
    complete_url = base_url + api_key + "&q=" + city_name

    res = requests.get(complete_url)
    
    weather_json = res.json()

    if weather_json['cod'] == '404':
        print("沒有這個城市哦！")
        return False
    
    weathet_temp = weather_json['main']['temp']
    weather_main = weather_json['weather'][0]['main']
    
    weather_value = {"city": city_name, "temp": weathet_temp, 'main': weather_main}
    
    return weather_value
