import requests
import time
from bs4 import BeautifulSoup



def lineNotify(msg):
     
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer KPPU8DVSXOQ8gtmMBLEhKC1MvGAIMSbZ5ahYIkADV8q", 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code

def boo_bot_click(id,url):
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
        'Referer': 'http://boo.tw/%s'%id,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    headers3 = {

        
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://b00.tw/%s?l=zh-TW'%id,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'

    }

    

    s = requests.Session()    
    boo = s.get("http://boo.tw/%s"%id, headers = headers)
    print("boo status : %d"%boo.status_code)
    print("進入短網址boo.tw/%s 等候點擊…"%id)
    time.sleep(2)
    b00 = s.get("http://b00.tw/%s?l=zh-TW"%id,headers = headers2)
    print("b00 status : %d"%b00.status_code)
    print("進入短網址b00.tw/%s 等候點擊…"%id)
    time.sleep(2)
    delta = s.get(url,headers = headers3)
    s.close()

    print(url+" status code : %d"%delta.status_code)

    info = {
        "path" : id,
        "boo" : str(boo.status_code),
        "b00" : str(b00.status_code),
        "targetSite" : str(delta.status_code)
    }   


    return info


def get_public_ip() :

    headers4 = {

        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.google.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }



    ip = requests.get("https://myip.com.tw/",headers = headers4)
    soup = BeautifulSoup(ip.text,'html.parser')
    ip_info = soup.find("h1", align="center")
    

    return ip_info.text.split(' ')[3]



link = [

    {"path" : "9acL5","target": "https://www.deltaww.com","times" : 1},
    {"path" : "dHf8N","target": "https://www.deltaww.com","times" : 1}
    
    ]



past_pub_ip = ''

while True :
    
    
    while True :
        try :
            now_pub_ip = get_public_ip()
            break
        except :
            print("無法取得IP，1秒後重試")
            time.sleep(1)
        

    
    if now_pub_ip != past_pub_ip :

        text_file = open("ip_log.txt", "a")
        text_file.write("\n"+now_pub_ip)
        text_file.close()

        past_pub_ip = now_pub_ip

        for i in link :
                
            while True :    
                try :
                    msg = "IP :"+now_pub_ip+"\n"+str(boo_bot_click(i['path'],i['target']))+"\n點擊數 : "+str(i['times'])
                    print(msg)
                    
                    if i['times'] == 1 :
                        lineNotify(msg)
                    elif i['times']%10 == 0:
                        lineNotify(msg)
                    

                    i['times'] += 1                    
                    break
                except :
                    print("點擊失敗1秒後重試")
                    time.sleep(1)                
        
    else :
        print("IP 重覆2秒後重試")
        time.sleep(2)

   
    
