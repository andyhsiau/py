import requests
from lxml import html
from bs4 import BeautifulSoup as bs

USEREMAIL = 'koet0312@gmail.com'
PASSWORD = 'ezutw1113'

LOGIN_URL = 'http://boo.tw/users/sign_in'

def main():
    URL = 'http://boo.tw/member/backstage'
    session_requests = requests.session()

    h1 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'boo.tw',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    result = session_requests.get(LOGIN_URL,headers = h1)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath('//meta[@name="csrf-token"]/@content')))[0]

    h2 = {
        'Connection': 'keep-alive',
        'Content-Length': '204',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://boo.tw',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': LOGIN_URL,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6'
    }

    h3 = {
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': LOGIN_URL,
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6'
        }

    payload = {
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        'user[email]': USEREMAIL,
        'user[password]': PASSWORD,
        'commit': 'Login'
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = h2)

    result = session_requests.get(URL ,headers = h3)
    soup = bs(result.text, 'html.parser')

    for link in soup.select('.table-responsive a'):
        print(link.get('href'))
if __name__ == '__main__':
    main()