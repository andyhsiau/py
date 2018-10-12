# coding=utf-8
import requests
import time
import json


def lineNotify(msg):
     
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer gbJGbuiMx236T6bHZR0221VUIRDTsC54zOCdzF8qcLs", 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code



def get_token() :
    data = {
        "code": "EAABgo9dnSUABAH9XOUJ1cAy1lfwZBdwFi1RFZAKTXxDqdCRq0dfTycLoOc2wR4oZBByvzC0KNCi5ACyiK4NlLicOqog5iY08qFZBfgmAMqDPpnHbKphbKtpAbNAZCl1GoTU8C4PGMxUPMX7DS6UTT3JykdIKDstvtSJfNODpALR7QDzTkQECIZBQvQRACERVOkU63jlyJb2E1pQJlpmZBOT8n0i7PGisK4ZD"
    }

    try :
        r = requests.post("https://api.v2.swag.live/login/facebook", data = data)
        token = str(r.headers['Authorization'])
        
    except :
        lineNotify('FB Token失效，延用舊Token重試，請更新FB Token')
        print("FB Token失效，延用舊Token重試")    
        oldtoken = open('old_token.txt','r')
        token = str(oldtoken.read())

    text_file = open("old_token.txt", "w")
    text_file.write(token)
    text_file.close()
    
    return token




headers2 = {

    'Authorization': get_token(),
    'User-Agent': 'swag/2.27.0 (Android; com.machipopo.swag; htc; HTC_D816x; zh-TW)',
    'Host': 'api.v2.swag.live',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
    #'If-Modified-Since': 'Tue, 25 Sep 2018 01:40:05 GMT'

}



r = requests.get("https://api.v2.swag.live/me", headers = headers2)

try :
    me = json.loads(r.text)
    currentdiamond = int(me['balance'])
except :
    currentdiamond = 0
time.sleep(2)
f = requests.get("https://api.v2.swag.live/flight-check", headers = headers2)
print("flight-check:"+str(f))
time.sleep(2)

r1 = requests.get("https://api.v2.swag.live/me", headers = headers2)
try : 
    me1 = json.loads(r1.text)
    afterdiamond = int(me1['balance'])
except :
    afterdiamond = 0



if f.status_code == 200:
    
    print("今日已成功登入Swag\n獲得鑽石："+str(afterdiamond-currentdiamond)+"\n鑽石餘額："+str(afterdiamond))
    lineNotify("今日已成功登入Swag\n獲得鑽石："+str(afterdiamond-currentdiamond)+"\n鑽石餘額："+str(afterdiamond))

elif f.status_code == 401 :
    print("Token失效，登入失敗，請自行登入領取鑽石")
    lineNotify("Token失效，登入失敗，請自行登入領取鑽石")

else :
    print("登入失敗，請自行登入領取鑽石")
    lineNotify("登入失敗，請自行登入領取鑽石")