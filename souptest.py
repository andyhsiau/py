import requests
from bs4 import BeautifulSoup


def getmithcurrency():  

    r = requests.get('https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E7%A7%98%E9%8A%80%E5%B9%A3/twd')
    soup = BeautifulSoup(r.text,'html.parser')
    tw = soup.find_all("div", class_="text-5xl")

    for s in tw:
        nt = s.text

    cu = nt.split('\n')
    cu2 = float(cu[1].split(' ')[1])
    
    return cu2


print(getmithcurrency()*2)
