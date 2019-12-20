#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('weather.db')

# get old value in DB

def latest_five_value():
    # 從尾到頭讀取，抓五筆
    record_list = conn.execute(
        '''
        SELECT * from weather_list
        ORDER BY ID DESC
        LIMIT 5
        '''
    )

    for lt in record_list:
        print(lt[0])

    conn.commit()
    conn.close()

# save to DB

def insert_weather_info(city, temp, desc, ts):
    conn.execute(
        '''
        INSERT INTO weather_list (city, temperature, description, create_timestamp, delete_timestamp)
        VALUES (?, ?, ?, ?, 0);
        ''', [city, temp, desc, ts]
    )

    conn.commit()
    conn.close()