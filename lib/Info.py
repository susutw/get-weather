import requests
import time

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

    c_temp = round(weathet_temp - 273.15, 2) # 攝氏
    ts = int(time.time())
    time_array = time.strftime("%Y/%m/%d %H:%M", time.localtime(ts))

    print('感謝查詢！你要的資訊在下面！(●´ω｀●)ゞ')
    print("地區：{}，溫度（攝氏）：{}，氣象：{}，查詢時間：{}。".format(city_name, c_temp, weather_main, time_array))

    weather_value = {"city": city_name, "temp": weathet_temp, 'main': weather_main, 'timestamp': ts}
    
    return weather_value
