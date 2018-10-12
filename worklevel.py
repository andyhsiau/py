# coding=utf-8
import requests
import json
import time
from requests_ntlm import HttpNtlmAuth





time1 = str(time.time())
now = time1.split(".")

print(now[0])

url = "http://dgoa/EMDApi/HRMEMP/GetEmpBaseInfo?EmpCode=631578&Language=zh-TW&_=1538111107"
print(url)

r = requests.get(url,auth=HttpNtlmAuth('delta\\andy.hsiau','ezutw1113Delta7'))

emp = json.loads(r.text)
print(r.text)
print(emp)

print(emp['baseModel']['WorkLevel'])

