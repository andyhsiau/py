# coding=utf-8
import requests
from bs4 import BeautifulSoup


def get_CI_info(hostname):

    headers = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '338',
        'Content-Type': 'application/x-www-form-urlencoded',  
        'Host': 'twtpeasset01:8080',
        'Origin': 'http://twtpeasset01:8080',
        'Referer': 'http://twtpeasset01:8080/AssetHomePage.do?logout=true',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

    }



    data = {
        'j_username': 'andy.hsiau',
        'j_password': 'ezutw1113Delta7',
        'domain': '0',
        'DOMAIN_NAME': 'DELTA',
        'sso_status': 'false',
        'LDAPEnable': 'false',
        'hidden': '選擇一個域',
        'hidden': '域',
        'AdEnable': 'true',
        'DomainCount': '1',
        'LocalAuth': 'No',
        'LocalAuthWithDomain': 'DELTA',
        'dynamicUserAddition_status': 'true',
        'localAuthEnable': 'true',
        'logonDomainName': 'DELTA',
        'LoginBtn': '登錄'
    }

    print("Try to login...")
    with requests.Session() as s:
        s.post('http://twtpeasset01:8080/j_security_check', headers = headers, data = data, verify=False)
    print("Login Succed !\n")
    print("Gen CIID now...")
    search_url = "http://twtpeasset01:8080/SearchN.do?selectName=Workstation&searchText="+hostname+"&submitbutton=%C2%A0"
    search_ciid = s.get(search_url)
    soup = BeautifulSoup(search_ciid.text,'html.parser')
    hover = soup.find("td", class_= " evenRow" )

    CIID = str(hover).split("\"")[5].split("=")[1].split("&")[0]
    print("Get CIID !"+CIID+"\n")
    print("Get CIID info now...")
    info = s.get("http://twtpeasset01:8080/ViewCIDetails.do?ciId=%s&"%CIID)
    soup = BeautifulSoup(info.text,'html.parser')
    f = soup.find_all("tr", height="20")
    #print(CIID)

    data = []
    for i in f :
        data.append(i.text.replace("\n","").replace("\t",""))
    print("Get CIID info Succed !")
    s.get("http://twtpeasset01:8080/AssetHomePage.do?logout=true")
    mac = str(data[4].split(":")[1]+':'+data[4].split(":")[2]+':'+data[4].split(":")[3]+':'+data[4].split(":")[4]+':'+data[4].split(":")[5]+':'+data[4].split(":")[6])
    #print(data)
    CIID_info = {

        "CI_Name" : data[0].split(":")[1],
        "Last_login_user" : data[20].split(":")[1].rstrip(),
        "Site" : data[2].split(":")[1].rstrip(),
        "Mac_address" : mac,
        "IP" : data[11].split(":")[1],
        "OS" : data[5].split(":")[1],
        "Model" : data[9].split(":")[1],
    }

    return CIID_info











