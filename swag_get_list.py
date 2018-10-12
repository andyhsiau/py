# coding=utf-8
import requests
import json
import time





headers = {

    'Host': 'api.v2.swag.live',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjU5MTVhOWYzIn0.eyJzdWIiOiI1OGRhZmZjYjRlMGM2YjNiM2UyY2M3NmEiLCJpc3MiOiJhcGkudjIuc3dhZy5saXZlIiwiYXVkIjoiYXBpLnYyLnN3YWcubGl2ZSIsImlhdCI6MTUzNzk1MTUyNiwiZXhwIjoxNTM5MTYxMTI2LCJqdGkiOiJXNnRISmlWaWtsMXV1SHpRIn0.u5KFkKIJIRMzM6WnGp3Kd8Tkgqqktese849GLA-ilbY',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

}



r = requests.get("https://api.v2.swag.live/users/5a22f4deaf9c462c61f2c7e1/outbox?page=1&limit=30", headers = headers)
#57c16f5bb811055b66d8ef46 Riva
#5989ac2b07067e258c19ba7f Nina
#5a5f3b40af9c462c6147f2e8 Baily
print(r)
swaglist = json.loads(r.text)
#print(r)
#print(swaglist)




for mediaID in swaglist :
    medias = mediaID['id']
    
    
    try:
        print(mediaID['caption']+"\nhttps://asia.messages.swag.live/"+str(medias)+".m3u8")
    except:
        print('empty')

    


