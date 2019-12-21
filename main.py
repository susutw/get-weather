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
        if value == None:
            print("沒有這個城市的說(|||ﾟдﾟ)")
            return
        result = DB.insert_weather_info(value['city'], value['temp'], value['main'], value['timestamp'])        
        c_temp = round(value['temp'] - 273.15, 2) # 攝氏
        time_array = time.strftime("%Y/%m/%d %H:%M", time.localtime(value['timestamp']))
        print('感謝查詢！你要的資訊在下面！(●´ω｀●)ゞ')
        print("地區：{}，溫度（攝氏）：{}，氣象：{}，查詢時間：{}。".format(city_name, c_temp, value['main'], time_array))
        return
    
    if action == feature[1]:
        result = DB.latest_five_value()
        return

    print("不好意思！我們沒有這個參數哦( ×ω× )")    
    return

if __name__ == "__main__":
    main()