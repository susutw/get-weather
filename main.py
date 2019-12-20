import requests
import json
import sys
import time

# lib
import lib.Info as Info
import lib.DB as DB

def main():
    # 用 argument 的方式指定動作
    try:
        action = sys.argv[1]
    except IndexError:
        print('～～請輸入參數～～')        
        return

    if action == 'search_by_city':
        
        city_name = input('請輸入要查詢的城市：')
        value = Info.get_weather_by_city(city_name)
        if value == False:
            return

        print(value)
        # 回存
        # result = DB.xxx
        ts = int(time.time())
        result = DB.insert_weather_info(value["city"], value["temp"], value["main"], ts)
        return
    
    if action == 'weather_record':
        DB.latest_five_value()
    
    return

if __name__ == "__main__":
    main()