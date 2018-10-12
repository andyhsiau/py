# coding=utf-8
import requests
import json
import os
import datetime
import time
import random

def lineNotify(token, msg):
     
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code

token = "0LFRzFYJHTisoaduF7m9qFIIBXbf6sqXRI2otpULHbZ"
linemsg = ''
holiday = ['09/24/18','10/10/18','12/31/18']

checkin = 0

delay = random.randint(0,600)
print('等待 '+str(delay)+' 秒後打卡...')
time.sleep(delay)

if str(time.strftime("%D", time.localtime())) in holiday :
        checkin += 1

if checkin == 1 :
    print('今天國定假日不用打卡')
    linemsg = '\n今天國定假日不用打卡'

elif datetime.date.today().weekday() == 5 :
    print('今天星期六不用打卡')
    linemsg = '\n今天星期六不用打卡'

elif datetime.date.today().weekday() == 6 :
    print('今天星期日不用打卡')
    linemsg = '\n今天星期日不用打卡'

else :
    r = requests.get("https://oa.deltaww.com/TASTWApi/TASCheckIn/CheckIn?_CheckInTw=631578")

    #r = requests.get("http://www.google.com")

    if r.status_code == 200 :
        print('\n打卡成功' + '\n時間 : ' + time.strftime("%D %H:%M:%S", time.localtime()))
        linemsg = '\n打卡成功' + '\n時間 : ' + time.strftime("%D %H:%M:%S", time.localtime())+"\n差異 "+str(delay)+" 秒"
    else :
        print('打卡失敗')
        linemsg = '\n打卡失敗'

lineNotify(token, linemsg)

