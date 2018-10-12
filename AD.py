# coding=utf-8
import requests
import time
import json


def lineNotify(token, msg):
     
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code

linetoken = "gbJGbuiMx236T6bHZR0221VUIRDTsC54zOCdzF8qcLs"


headers = {

    'Host': 'quests.swag.live',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '2',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; HTC_D816x Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,en-US;q=0.9',
    'X-Requested-With': 'com.machipopo.swag'

}

headers2 = {

    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjU5MTVhOWYzIn0.eyJzdWIiOiI1OGRhZmZjYjRlMGM2YjNiM2UyY2M3NmEiLCJpc3MiOiJhcGkudjIuc3dhZy5saXZlIiwiYXVkIjoiYXBpLnYyLnN3YWcubGl2ZSIsImlhdCI6MTUzNzQzNjkyNywiZXhwIjoxNTM4NjQ2NTI3LCJqdGkiOiJXNk5zX194di1CczBRR3VEIn0.1Sc6U3pA99WErcKKFXFiHrCauXlLYosFsUoNNxffLE8',
    'User-Agent': 'swag/2.27.0 (Android; com.machipopo.swag; htc; HTC_D816x; zh-TW)',
    'Host': 'api.v2.swag.live',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',

}


r = requests.get("https://api.v2.swag.live/me", headers = headers2)

try :
    me = json.loads(r.text)
    currentdiamond = int(me['balance'])
except :
    currentdiamond = 0
time.sleep(2)
f = requests.get("https://api.v2.swag.live/flight-check1", headers = headers2)
print("flight-check:"+str(f))
time.sleep(2)
d = requests.get("https://quests.swag.live/dailylogin/zh-tw/7.html?diamonds=200&auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjU5MTVhOWYzIn0.eyJzdWIiOiI1OGRhZmZjYjRlMGM2YjNiM2UyY2M3NmEiLCJpc3MiOiJhcGkudjIuc3dhZy5saXZlIiwiYXVkIjoiYXBpLnYyLnN3YWcubGl2ZSIsImlhdCI6MTUzNzQzNjkyNywiZXhwIjoxNTM4NjQ2NTI3LCJqdGkiOiJXNk5zX194di1CczBRR3VEIn0.1Sc6U3pA99WErcKKFXFiHrCauXlLYosFsUoNNxffLE8", headers = headers)
print("daily-login:"+str(d))
time.sleep(2)
r1 = requests.get("https://api.v2.swag.live/me", headers = headers2)
try : 
    me1 = json.loads(r1.text)
    afterdiamond = int(me1['balance'])
except :
    afterdiamond = 0



if f.status_code == 200:
    
    print("今日登入已成功Swag\n獲得鑽石："+str(afterdiamond-currentdiamond)+"\n鑽石餘額："+str(afterdiamond))
    lineNotify(linetoken, "今日登入已成功Swag\n獲得鑽石："+str(afterdiamond-currentdiamond)+"\n鑽石餘額："+str(afterdiamond))

elif f.status_code == 401 :
    print("Token失效，登入失敗，請自行登入領取鑽石")
    lineNotify(linetoken, "Token失效，登入失敗，請自行登入領取鑽石")

else :
    print("登入失敗，請自行登入領取鑽石")
    lineNotify(linetoken, "登入失敗，請自行登入領取鑽石")