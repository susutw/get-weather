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
        return    
    weathet_temp = weather_json['main']['temp']
    weather_main = weather_json['weather'][0]['main']
    ts = int(time.time())
    weather_value = {"city": city_name, "temp": weathet_temp, 'main': weather_main, 'timestamp': ts}    
    return weather_value

def no_argument():
    show_log = '''
        嗨！請輸入參數！
        以下是我們的功能表，請把他帶到程式後面告訴我們你需要什麼
        （例：python3 main.py search_by_city）

        search_by_city
        => 想知道任何城市最即時的溫度訊息嗎？輸入此參數，快速查詢你要的資料！

        weather_record
        => 想知道之前的查詢記錄嗎？輸入此參數，可看到最新的五筆紀錄！
    '''
    return show_log
