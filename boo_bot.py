import requests
import time


headers = {
    'Host': 'boo.tw',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'

}

headers2 = {

    'Host': 'b00.tw',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://boo.tw/4PlCt',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

headers3 = {

    'Host': 'www.deltaww.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://b00.tw/4PlCt?l=zh-TW',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'

}

s = requests.Session()
boo = s.get("http://boo.tw/4PlCt", headers = headers)
print("boo status : %d"%boo.status_code)
print("進入短網址boo.tw/4PlCt 等候點擊…")
time.sleep(5)
b00 = s.get("http://b00.tw/4PlCt?l=zh-TW",headers = headers2)
print("b00 status : %d"%b00.status_code)
print("進入短網址b00.tw/4PlCt 等候點擊…")
time.sleep(5)
delta = s.get("https://www.deltaww.com/",headers = headers3)
s.close()

print("DELTA status code : %d"%delta.status_code)