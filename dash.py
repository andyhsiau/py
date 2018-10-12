
import requests
import json
 
 
#m3u8的文件路径
path = input("https://asia.messages.swag.live/5b9666acaccb04002c80b8b6.m3u8").replace('\\','/')
#print(path)
file = open(path,'r')
operation = 'n'
pre_link = ''
if operation == 'y':
    pre_link = input("请输入前缀：").strip()
links = []
for i in file:
    if '#' not in i:
        i = i.strip()
        links.append(pre_link+i)
file.close()
l = len(links)
print("总共有%d个片段..."%l)
length = len(str(len(links)))
n = 0
txt = ""
for link in links:
    n = n + 1
    print("还剩%d个片段未下载..."%(l-n))
    if len(str(n)) < length:
        name = '0'*(length-len(str(n))) + str(n) + ".ts"
    else:
        name = str(n)+".ts"
    txt = txt + "file \'" + name + "\'\n"
    jsonreq = json.dumps({'jsonrpc':'2.0', 'id':1,
               'method':'aria2.addUri',
               'params':[[link],{"out":name,"split":"5","max-connection-per-server":"16","seed-ratio":"0"}]})
    c = requests.post('http://localhost:6800/jsonrpc', jsonreq)
file = open("D:\\py\\1.txt","w")
file.write(txt)
file.close()
