# Get Weather

## 可能會需要安裝的套件
* `pip3 install requests2`
* `brew install sqlite`

## Quick Start

`git clone git@github.com:susutw/get-weather.git`

`cd get-weather`

功能介紹：`python3 main.py`

## 功能簡介

### 查詢某城市的天氣

`python3 main.py search_by_city`

* 會跳出一個輸入框，請輸入想查詢的城市（英文）

### 查看搜尋紀錄

`python3 main.py weather_record`

## DB Schema 設計

* 一個 table，當查詢資料產生時，會存入
    1. 城市名稱（一律轉成全小寫）
    2. 溫度（絕對溫度）
    3. 氣象（多雲、晴朗 等等）
    4. 查詢時間（timestamp）


欄位             | Type        | 設計概念
----------------|-------------|--------------------------------------------
ID              |INTEGER      |`PRIMARY KEY` & `AUTOINCREMENT` 屬性
city            |CHARACTER(20)|以城市名稱長度設計
temperature     |FLOAT        |存絕對溫度到小數點第二位，方便轉換攝氏、華氏
description     |CHARACTER(20)|以氣象名稱長度設計
create_timestamp|TINYINT      |儲存 timestamp 的整數，固定長度為 10，也可用排序最新查詢時間
delete_timestamp|TINYINT      |預設為 0，可用在之後擴充刪除功能，刪除時把刪除當下的 timestamp 存入


## 檔案介紹

File       | 主要內容
-----------|-----------------------------
main.py    | 功能總表，接收參數執行指定功能
lib/DB.py  | Database 相關操作都放在這個表，包含：建立 Table、SELECT 最新五筆資料、INSERT 資料進表格
lib/Info.py| 執行抓取 API、印出的動作，且回傳到 `main.py`