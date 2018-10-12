# coding=utf-8
import os
import lineTool
import requests
import json
import time
import random
import time

def lineNotify(token, msg):
     
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code


token = "7kxQeLiGzyAuHiMvkYWA1naurg0aETk7uOYgKw7SeLu"



localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

msg = "現在時間為\n" +localtime

lineNotify(token, msg)