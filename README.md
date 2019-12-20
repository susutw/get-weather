# Get Weather

## 可能會需要安裝的套件
- `pip3 install requests2`
- `brew install sqlite`

## Install

`git clone git@github.com:susutw/get-weather.git`

`cd get-weather`

`python3 createDB.py`（程式執行前需要先建立 Database）

## 功能簡介

### 查詢某城市的天氣

`python3 main.py search_by_city`

- 會跳出一個輸入框，請輸入想查詢的城市（英文）

### 查看搜尋紀錄

`python3 main.py weather_record`