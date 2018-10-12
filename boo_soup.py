import requests
from bs4 import BeautifulSoup
import json

headers = {

    'Connection': 'keep-alive',
    'Content-Length': '226',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://boo.tw',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://boo.tw/users/sign_in',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'

}

headers2 = {

    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://boo.tw/users/sign_in',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'


}

data = {
    
    "user[email]" : "koet0312@gmail.com",
    "user[password]" : "ezutw1113",
    
}
j = json.dumps(data)
s = requests.Session()
p = s.post("http://boo.tw/users/sign_in", headers = headers ,data = j)
r = s.get("http://boo.tw/member/backstage", headers = headers2)
print(p)
s.close()
s.post("http://boo.tw/users/sign_out")

