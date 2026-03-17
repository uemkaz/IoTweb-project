#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import time
from datetime import datetime
import pytz

data_file = "temperature_data.txt"

# HTTPレスポンスのコンテンツタイプを出力
print('Content-type: text/html; charset=UTF-8')
print('')

# 標準入力からJSONデータを読み込む
form = json.load(sys.stdin)

# フォームデータから温度値と時間を取得
temp = form.get('temperature')
get_time = form.get('get_time', int(time.time()))

jst = pytz.timezone('Asia/Tokyo')
jst_time = datetime.now(jst).strftime('%Y-%m-%d %H:%M:%S %Z')


# データファイルを開き、温度と取得した時間を書き込む       
with open(data_file, 'a', encoding='utf-8') as file:
    file.write(f"get_time: {jst_time}, temperature: {temp}\n")




