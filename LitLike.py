# coding=utf-8
import requests
import json
import os
import time
import random

n = 1
likeround = 1
while True :
    print("==========================新的一輪開始==========================")
    token_post = {

        'Authorization': '92a6aa6be831b87063fead6bec256f4ecc3f87e775f47529dcd81d1eadb080b5ad502b13befef74b1523ff3852fcd78abe84c3426834c1ba7059f2b2c67530cd6f564905d4b3aafca386e7e76c573aab5723ae3993d066cbd1581957f145845f558c8afa942ac9612ed0d09990850572ed23cf6dbd18f8f3d025848e055f99af12c2f97c850e74cdb7275a9112ee1fc27da96e9a204b909b08c97d857a17da4dd1117510bb097c0868ddc41d9f3ba577d4a80659345136bf7da87a18672e866609a912eade43040732e09da983b3bfc5f5b45063a07251a70f0c6ec499df89a55b26ad2b768932414373f84c79fd5e57f4a08c113c8b2c58fecf791a906561a46a7448757e7e024ba68b1f9b19d16f53b1f73d769db0f89c71f53e76acab6244e06c12b29a4df1dcc1d88a890ad4f6af962ba6d0e4154df4bcee319710d715edceedb039699297ea88c84650377f406e4bbee0842db8cbf9ea3f779c4059380be1b3a17ec1e1bdad2d6270b12addb793',
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'


    }
    
    
    discoverurl = 'https://api.lit.live/stories/discover?next='+str(n)
    
    print(discoverurl)

    r = requests.get(discoverurl, headers=token_post)
    piclist = json.loads(r.text)
    r.close()
    n += 1
    for story in piclist:

            stories = story['stories']
            
            for picid in stories:

                if picid['liked'] == False :

                    puturl = str('https://api.lit.live/stories/'+picid['id']+'/like')
                    print('第 ' + str(likeround) + ' 輪，第 ' + str(n-1) +' 頁')
                    print('♡>>>♥')
                    p = requests.put(puturl, headers=token_post)
                    if p.status_code == 204 :
                        print('已成功對 '+str(story['name'])+' 的 '+picid['id']+' 照片按讚\n')
                        liketime = random.randint(2, 8)
                        time.sleep(liketime)
                    else :
                        print('按讚失敗!!!')
                        time.sleep(2)
                else :
                    
                    print('♥')
                    print(str(story['name'])+' 的 '+picid['id']+' 照片已經按過讚了！\n')
                    

    print("==========================已經按完一輪了==========================")
    likeround += 1
    time.sleep(3)
    if n > 10 :
        n = 1
    