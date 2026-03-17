# IoT センサーデータ可視化システム (IoT Web Project)

Raspberry Piで取得したセンサーデータをサーバーに送信し、Webブラウザ上でリアルタイムにグラフとして表示するIoTシステムです。

## 1. 必要なハードウェア
このシステムを動かすために、以下の部品を使用しています。

* **Raspberry Pi:** 例：Raspberry Pi 4 Model B
* **センサー:** LM61CIZ
* **ADコンバータ:** MCP3002
* **その他:** ブレッドボード、ジャンパーワイヤー適量

**【配線図について】**
センサーとラズパイの配線は、以下のサイトを参考に接続しています。
* [LM61CIZとラズパイの接続方法（参考サイト）](https://qiita.com/ktamido/items/937712efa5c2640eb472)

## 2. 使用技術
以下の技術を組み合わせて構築・運用しています。

* **フロントエンド:** HTML5, CSS3
* **バックエンド:** Python 3, CGI (`temperature_logger.cgi`, `graph.cgi`)
* **インフラ・サーバー:** Raspberry Pi, Webサーバー (Apache)

## 3. 主な機能とファイルの役割
* `temp.py` (Raspberry Pi側):温度取得し`temperature_logger.cgi`に温度データを送信するプログラム。
* `style.css` : ユーザーが見るWebページのデザインとレイアウト。
* `temperature_logger.cgi` : ラズパイから送られてきたデータを受信し、テキストファイル（`temperature_data.txt`）に保存するプログラム。
* `graph.cgi` : 保存された最新のログデータを読み込み、Pythonで動的にグラフ画像（Base64形式）を生成してWebページに埋め込むプログラム。


---
*Created by uemkaz*