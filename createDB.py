#!/usr/bin/python
import sqlite3 

conn = sqlite3.connect('weather.db')
conn.execute(
    '''
    CREATE TABLE weather_list
    (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        city CHARACTER(20) NOT NULL,
        temperature FLOAT NOT NULL,
        description CHARACTER(20) NOT NULL,
        create_timestamp TINYINT NOT NULL,
        delete_timestamp TINYINT NOT NULL
    );
    '''
)

print('Create Table SUCCESSFULLY')

conn.commit()
conn.close()