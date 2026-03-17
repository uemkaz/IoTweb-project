#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys
import io
import base64

# データの読み込み
times = []
temperatures = []
date_str = ""

with open('temperature_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        try:
            parts = line.split()
            if len(parts) >= 6 and parts[0] == 'get_time:':
                if not date_str:
                    date_str = parts[1]
                times.append(parts[2])
                temperatures.append(float(parts[5]))
        except ValueError:
            pass

# グラフの作成
plt.figure(figsize=(8, 5))
plt.plot(times, temperatures, marker='o', label='Temperature')
plt.title(f'Time and Temperature Variation: {date_str}')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# 画像をBase64の文字列に変換
png_buf = io.BytesIO()
plt.savefig(png_buf, format="png", dpi=90)
plt.close()
image_base64 = base64.b64encode(png_buf.getvalue()).decode('utf-8')

# HTMLとして出力
print("Content-Type: text/html; charset=utf-8")
print("")

# HTMLの前半部分
html_top = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>自作IoT温度監視システム </title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="container">
        <h1>IoTデータ可視化Webアプリケーション</h1>

        <div class="card">
            <h2>1. 本サイトの概要</h2>
            <p>大学のゼミにて、温度センサーを用いて冷蔵庫内の温度を定期的に測定し、そのログファイルから動的にグラフを生成してWebブラウザ上で確認できるシステムを構築しました。
このプロジェクトを通じてサーバーサイドにおけるCGIの仕組みを深く学び、同時にHTMLやCSSを活用して活動をまとめることを目的として本Webサイトを制作しました。</p>
        </div>

        <div class="card">
            <h2>2. システム構成</h2>
            <p>以下の技術スタックで構築・運用しています。センサーを用いたハードウェアからのデータ取得を起点に、サーバーサイドでのデータ処理からフロントエンドのUI構築まで、Webアプリケーションに必要な要素を一貫して設計・実装しました。</p>
            <ul>
                <li><strong>フロントエンド:</strong> HTML5, CSS3 </li>
                <li><strong>バックエンド:</strong>Python 3, CGI</li>
                <li><strong>インフラ:</strong> Webサーバー（Apache)</li>
            </ul>
            <div class="photo-placeholder">
              <img src="../flowchart.png" alt="システムのフローチャート" style="max-width: 100%; height: auto;">
            </div>
        </div>

        <div class="card">
            <h2>3. 測定結果 (動的生成グラフ)</h2>
            <p>以下のグラフは、サーバー上の最新のログデータを読み込み、Pythonがリアルタイムで描画したものです。</p>
            <div class="image-container">
                <img class="graph" src="data:image/png;base64,"""

# HTMLの後半部分（整理版）
html_bottom = """" alt="温度変化グラフ">
            </div>
        </div>

        <div class="card">
            <h2>4. 製作したソースコード</h2>
            <ul>
                <li>
                    <a href="https://github.com/uemkaz/IoTweb-project" target="_blank" rel="noopener noreferrer">
                        GitHubリポジトリ（IoTweb-project）
                    </a>
                </li>
            </ul>
        </div>

        <div class="card">
            <h2>5. 作成した関連ブログ</h2>
            <ul>
                <li>
                    <a href="https://www.48v.me/~uemkaz/blog/blog01" target="_blank" rel="noopener noreferrer">
                        HACCPと飲食店の冷蔵庫の温度管理
                    </a>
                </li>
                <li>
                    <a href="https://www.48v.me/~uemkaz/blog/blog02" target="_blank" rel="noopener noreferrer">
                        冷蔵庫の温度管理システムの既存製品
                    </a>
                </li>
            </ul>
        </div>

    </div> </body>
</html>
"""
# 全てを結合して出力
print(html_top + image_base64 + html_bottom)