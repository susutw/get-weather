#!/usr/bin/python
import sqlite3
import time

conn = sqlite3.connect('weather.db')

# get old value in DB

def latest_five_value():
    # 從尾到頭讀取，抓五筆
    record_list = conn.execute(
        '''
        SELECT * from weather_list
        GROUP BY city
        ORDER BY MAX(create_timestamp) DESC
        LIMIT 5
        '''
    )

    print('---------------------------------------(*’ｰ’*)----------------------------------------')
    for row in record_list:
        time_array = time.strftime("%Y/%m/%d %H:%M", time.localtime(row[4]))
        c_temp = round(row[2] - 273.15, 2)
        print('[ID:{}] => 城市：{}，溫度：{}，氣象：{}，查詢時間：{}。'.format(row[0], row[1], c_temp, row[3], time_array))
    
    conn.commit()
    conn.close()

# save to DB

def insert_weather_info(city, temp, desc, ts):
    conn.execute(
        '''
        INSERT INTO weather_list (city, temperature, description, create_timestamp, delete_timestamp)
        VALUES (?, ?, ?, ?, 0)
        ''', [city, temp, desc, ts]
    )

    conn.commit()
    conn.close()