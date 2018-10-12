# coding=utf-8
import requests
import json
import os
import time
import random
from bs4 import BeautifulSoup

likeround = 1
nextlocation = ''
likecount = 0
nextID = 0
friend = 0
unfriend = 0
earncount = 0
while True :

    def getmithcurrency():  

        r = requests.get('https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E7%A7%98%E9%8A%80%E5%B9%A3/twd')
        soup = BeautifulSoup(r.text,'html.parser')
        r.close()
        tw = soup.find_all("div", class_="text-5xl")

        for s in tw:
            nt = s.text

        cu = nt.split('\n')
        cu2 = float(cu[1].split(' ')[1])
    
        return cu2




    print("\n========新的一輪開始========")
    token_post = {

        'Authorization': '89d84756c7f42832eb69950fd56003211c7f3f35dd4b29f4b5760fff8c6906c8569756c32786b20ef537c212b4c6de8b436ea44d88447a03fcd038b48dd5517bbab9aabfc223ca1841f2e8912621beeb2a9b7dac3351299ba2be578116b594c1e39bbb97463285f54da62bbe7527eeefa3a505cc4ca12dcede729fc980e81dffe19df8c64233171d4226304dc0555f8cbbd6805b3e4ebe58b17e41bbf325fb97fcc6d39deeef7a93a7dcb3978b1584a043a70511a4a2817ca58410f73743830e50b4ab9bd7846abd7f6826bd9b392bce322856029cb8a84b0eb6c330a9bbc5f08fdbeab1f08bb1828c726569802a5f9061544136c164d45d70723ac52eb448037c670a9b11ec3297972a031f60af503339b43f39ed68842f8a8d3ece66157711bb5a15e42ac83bd7e4722b1c5117928ccc483118ef6090f8fa5c218a96067706a9baa62a478f2ad7f39e26bcd554670f0960988406cef530be2a33863b0170e716176f33450a4f108cb62bbfd3191545',
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'


    }
    
    if nextID == 0:
        nextID = ''

    discoverurl = 'https://api.lit.live/stories/discover?next='+str(nextID)
    
    print(discoverurl)


    try:
        r = requests.get(discoverurl, headers=token_post)
    except :
        print('Time Out...10秒後重新開始...')
        time.sleep(10)
        r = requests.get('https://api.lit.live/stories/discover?next=', headers=token_post)
        nextlocation = ''

    piclist = json.loads(r.text)
    r.close()
   
    
    
    for story in piclist:
            
            m = requests.get('https://api.lit.live/me/stories', headers = token_post)
            mith_list = json.loads(m.text)
            m.close()
            mith_count = 0
            for mith in mith_list:
                mith_stories = mith['mithril']
                mith_count += mith_stories

            if earncount == 0:
                earn = mith_count
                earncount = 1
            print('======即時回報======')
            print('目前累記按了 '+str(likecount)+' 個讚')
            print('此次運行賺了 '+str(mith_count-earn)+' 顆秘銀幣')
            print('目前累記賺了 '+str(mith_count)+' 顆秘銀幣')

            me = requests.get('https://api.lit.live/me' , headers = token_post)    
            me_list = json.loads(me.text)
            me.close()
            print('帳號秘銀幣餘額：'+str(me_list['vault_mithril'])+' 顆')
            print('財產試算：'+str(me_list['vault_mithril']+mith_count)+' 顆'+' 相當於台幣：'+ str((me_list['vault_mithril']+mith_count)*getmithcurrency())+' 元')
            print("粉絲："+str(me_list['#followers'])+" 好友："+str(me_list['#followings'])+" 我的照片："+str(me_list['#stories']))
            print('舊朋友：'+str(friend)+" 新朋友："+str(unfriend)+"\n====================\n")
            
            print('找到 '+str(len(piclist))+' 個Lit使用者')
            stories = story['stories']
            if story["followed"] == False :
                
                print('還沒與 '+str(story['name'])+' 成為好友，已送出邀請。')
                f = requests.put('https://api.lit.live/users/'+str(story['id']+'/follow'), headers = token_post)
                if f.status_code == 201 :
                    print('邀請成功')
                    unfriend+=1
                    time.sleep(3)
                else:
                    print('邀請失敗')
                    time.sleep(3)
            else :
                print('和 '+ str(story['name'])+ ' 已經是好友')
                friend+=1
            userpicno = 1
            for picid in stories:
                print('找到 '+str(story['name'])+' 的 '+str(len(stories))+' 張照片')
                
                if picid['liked'] == False :
                    
                    puturl = str('https://api.lit.live/stories/'+picid['id']+'/like')
                    print('第 ' +str(likeround)+' 輪' + ' nextID= ' + str(nextID))
                    print('♡>>>♥')
                    p = requests.put(puturl, headers=token_post)
                    if p.status_code == 204 :
                        print('已成功對 '+str(story['name'])+' 的第 '+str(userpicno)+' 張照片按讚\n')
                        userpicno += 1
                        likecount += 1
                        liketime = random.randint(2, 8)
                        time.sleep(liketime)
                    else :
                        print('按讚失敗!!!')
                        time.sleep(2)
                else :
                    
                    print('♥')
                    print(str(story['name'])+' 的 '+picid['id']+' 照片已經按過讚了！\n')
                    

    print("\n========已經按完一輪了========")
    print('目前累記按了 '+str(likecount)+' 個讚')

    
    
    if nextID == '':
        nextID = 0
    
    nextID+=1
    likeround += 1
    time.sleep(5)

    if nextID > 3:
        nextID=0
        delay = random.randint(5,15)

        print('按一段時間了這次休息 '+str(delay)+' 分鐘...')
        timerange = delay + 1
        for i in range(1, timerange):
            print('還有 '+str(delay)+' 分鐘...')
            delay -= 1
            time.sleep(60)
    
    