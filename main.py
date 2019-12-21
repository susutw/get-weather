import requests
import json
import sys
import time

# lib
import lib.Info as Info
import lib.DB as DB

feature = ['search_by_city', 'weather_record']

def main():
    # 用 argument 的方式指定動作
    try:
        action = sys.argv[1]
    except IndexError:
        print(Info.no_argument())        
        return

    if action == feature[0]:
        city_name = input('請輸入要查詢的城市：')
        value = Info.get_weather_by_city(city_name.lower())
        if value == False:
            return

        result = DB.insert_weather_info(value['city'], value['temp'], value['main'], value['timestamp'])
        return
    
    if action == feature[1]:
        result = DB.latest_five_value()
        return

    print("不好意思！我們沒有這個參數哦( ×ω× )")    
    return

if __name__ == "__main__":
    main()