# coding=utf-8
import requests
import json
import os
import time
from requests_toolbelt  import MultipartEncoder
import random


headers = {

    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjU5MTVhOWYzIn0.eyJzdWIiOiI1OGRhZmZjYjRlMGM2YjNiM2UyY2M3NmEiLCJpc3MiOiJhcGkudjIuc3dhZy5saXZlIiwiYXVkIjoiYXBpLnYyLnN3YWcubGl2ZSIsImlhdCI6MTUzNjU0MzQzOSwiZXhwIjoxNTM3NzUzMDM5LCJqdGkiOiJXNVhLenlMVXoydXNfeDV0In0.zLZ5bf59wLsGMMR3wO_MRln5gRYHcV8izbKwv3rdntU',
    'User-Agent': 'swag/2.26.3 (Android; com.machipopo.swag; htc; HTC_D816x; zh-TW)',
    'Host': 'asia.messages.swag.live',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

a = 1
for i in range(1, 9) :
    url = "https://asia.messages.swag.live/5b96f44df1a5875bc4dec356-1-0000"+str(a)+".m4s"
    videofile = "video\\5b96f44df1a5875bc4dec356-1-0000"+str(a)+".m4s"

    r = requests.get(url, headers = headers)


    with open(videofile, "wb") as code:
        code.write(r.content)
    a += 1
    print(r)

