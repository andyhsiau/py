# coding=utf-8
import requests




headers = {

    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjU5MTVhOWYzIn0.eyJzdWIiOiI1OGRhZmZjYjRlMGM2YjNiM2UyY2M3NmEiLCJpc3MiOiJhcGkudjIuc3dhZy5saXZlIiwiYXVkIjoiYXBpLnYyLnN3YWcubGl2ZSIsImlhdCI6MTUzNjU0MzQzOSwiZXhwIjoxNTM3NzUzMDM5LCJqdGkiOiJXNVhLenlMVXoydXNfeDV0In0.zLZ5bf59wLsGMMR3wO_MRln5gRYHcV8izbKwv3rdntU',
    'User-Agent': 'swag/2.26.3 (Android; com.machipopo.swag; htc; HTC_D816x; zh-TW)',
    'Host': 'api.v2.swag.live',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    


}

r = requests.put("https://api.v2.swag.live/messages/5b98441937c22700470d9d53/unlock", headers = headers)

print(r)
print(r.text)