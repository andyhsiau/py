# coding:utf-8
import requests
import json
import urllib3
from json.decoder import JSONDecodeError

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getAPInfo(ip) :
    
    headers = {
        'Host': 'cpi.deltaww.com',
        'Connection': 'keep-alive',
        'Content-Length': '143',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://cpi.deltaww.com',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://cpi.deltaww.com/webacs/pages/common/login.jsp',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    data = {
        'j_username': 'andy.hsiau',
        'j_password': 'ezutw1113Delta7'
    }

    login_url = 'https://cpi.deltaww.com/webacs/j_spring_security_check'
    search_url = "https://cpi.deltaww.com/webacs/searchClientAction.do?json=true&itemsPerPage=25&pager.offset=0&filterConjunction=and&isAscending=true&orderByColumn=connectionTypeString&ipAddress=*%s*&_FILTER_CONJUNCTION=and&start=0&count=25&sort=connectionTypeString" %ip
    
       
    #s = requests.Session()
    #s.post(login_url, headers = headers, data = data, verify=False)   
    
    with requests.Session() as s:
        s.post(login_url, headers = headers, data = data, verify=False)
        r = s.get(search_url)
    
    try:
        device = json.loads(r.text)
    except JSONDecodeError :
        print("Locked!")
    
    s.keep_alive = False
    s.close()
    s.get("https://cpi.deltaww.com/webacs/j_spring_security_logout", verify=False)
    print(device)
    if len(device['items']) != 0 :
        try :
            switch_device_temp = device['items'][0]['mapHierarchy'].split(" > ")
            switch_device = switch_device_temp[-1]
        except :
            switch_device = device['items'][0]['mapHierarchy']
        
        try :
            User_name = device['items'][0]['userName'].split('/')
        except:
            User_name = device['items'][0]['userName']
        
        info = {
            
            "Actions": "",
            "Switch_Device": device['items'][0]['exportLradName'],
            "Switch_Hostname": device['items'][0]['exportLradIpAddress'],
            "ED_IP_Address": device['items'][0]['ipAddress'],
            "ED_MAC_Address": device['items'][0]['macAddress'],
            "Vendor_Name": device['items'][0]['clientVendor'],
            "Port_Number": "",
            "Port_Name": "",
            "VLAN_ID": device['items'][0]['clientVlanId'],
            "VLAN_Name": device['items'][0]['clientInterface'],
            "Last_Scan_Date**": device['items'][0]['exportLastSessionTime'],
            "User_name": User_name[-1]

        }
    else :

        info = {
            
            "_result":"No Data"
        }
        
    return info


