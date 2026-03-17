#!/usr/bin/python
#coding: utf-8

import wiringpi as pi
import time
import requests

SPI_CH = 0
READ_CH = 0
ZERO = 0.6
SPI_SPEED = 1000000
VOLTAGE = 3.3
ADC = 1023
cooltime = 60
post_url = "https://www.48v.me/~uemkaz/cgi-bin/temperature_logger.cgi" 

pi.wiringPiSPISetup(SPI_CH, SPI_SPEED)


# オフセットの計算 LM61BIZ オフセットは 0℃ = 0.6V(600mV)
Offset = (ZERO / VOLTAGE) * ADC

while True:
    # SPI通信の準備
    Buffer = 0x6800 | (0x1800 * READ_CH)
    Buffer = Buffer.to_bytes(2, byteorder='big')
    pi.wiringPiSPIDataRW(SPI_CH, Buffer)

    # ADCからの値を温度に変換
    Value = (Buffer[0] * 256 + Buffer[1]) & 0x3ff
    Volt = (Value - Offset) * VOLTAGE / ADC
    temp = round(Volt * 100, 3)


    # POSTリクエスト送信
    response = requests.post(post_url, json={"temperature": temp})

    time.sleep(cooltime)



