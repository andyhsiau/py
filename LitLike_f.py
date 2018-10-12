# coding=utf-8
import requests
import json
import os
import time
import random


likeround = 1
nextlocation = ''
likecount = 0
while True :
    print("==========================新的一輪開始==========================")
    token_post = {

        'Authorization': '89d84756c7f42832eb69950fd56003211c7f3f35dd4b29f4b5760fff8c6906c8569756c32786b20ef537c212b4c6de8b436ea44d88447a03fcd038b48dd5517bbab9aabfc223ca1841f2e8912621beeb2a9b7dac3351299ba2be578116b594c1e39bbb97463285f54da62bbe7527eeefa3a505cc4ca12dcede729fc980e81dffe19df8c64233171d4226304dc0555f8cbbd6805b3e4ebe58b17e41bbf325fb97fcc6d39deeef7a93a7dcb3978b1584a043a70511a4a2817ca58410f73743830e50b4ab9bd7846abd7f6826bd9b392bce322856029cb8a84b0eb6c330a9bbc5f08fdbeab1f08bb1828c726569802a5f9061544136c164d45d70723ac52eb448037c670a9b11ec3297972a031f60af503339b43f39ed68842f8a8d3ece66157711bb5a15e42ac83bd7e4722b1c5117928ccc483118ef6090f8fa5c218a96067706a9baa62a478f2ad7f39e26bcd554670f0960988406cef530be2a33863b0170e716176f33450a4f108cb62bbfd3191545',
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'


    }
    
    
    discoverurl = 'https://api.lit.live/stories/featured?next='+nextlocation
    
    print(discoverurl)


    try:
        r = requests.get(discoverurl, headers=token_post)
    except :
        print('Time Out...10秒後重新開始...')
        time.sleep(10)
        r = requests.get('https://api.lit.live/stories/featured?next=', headers=token_post)
        nextlocation = ''

    piclist = json.loads(r.text)
    r.close()
   
    
    
    for story in piclist:
            print('找到 '+str(len(piclist))+' 個Lit使用者')
            stories = story['stories']
            if story["followed"] == False :
                
                print('還沒與 '+str(story['name'])+' 成為好友，已送出邀請。')
                f = requests.put('https://api.lit.live/users/'+str(story['id']+'/follow'), headers = token_post)
                if f.status_code == 201 :
                    print('邀請成功')
                    time.sleep(3)
                else:
                    print('邀請失敗')
                    time.sleep(3)
            else :
                print('和 '+ str(story['name'])+ ' 已經是好友')

            for picid in stories:
                print('找到'+str(story['name'])+'的'+str(len(stories))+'張照片')
                
                if picid['liked'] == False :
                    
                    puturl = str('https://api.lit.live/stories/'+picid['id']+'/like')
                    print('第 ' +str(likeround)+' 輪' + ' nextID= ' + str(nextlocation))
                    print('♡>>>♥')
                    p = requests.put(puturl, headers=token_post)
                    if p.status_code == 204 :
                        print('已成功對 '+str(story['name'])+' 的 '+picid['id']+' 照片按讚\n')
                        likecount +=1
                        liketime = random.randint(2, 8)
                        time.sleep(liketime)
                    else :
                        print('按讚失敗!!!')
                        time.sleep(2)
                else :
                    
                    print('♥')
                    print(str(story['name'])+' 的 '+picid['id']+' 照片已經按過讚了！\n')
                    

    print("==========================已經按完一輪了==========================")
    print('目前累記按了 '+str(likecount)+' 個讚')

    m = requests.get('https://api.lit.live/me/stories', headers = token_post)
    mith_list = json.loads(m.text)
    m.close()
    mith_count = 0
    for mith in mith_list:
        mith_stories = mith['mithril']
        mith_count += mith_stories
    
    print('目前總共有 '+str(mith_count)+' 顆秘銀幣')

    me = requests.get('https://api.lit.live/me' , headers = token_post)
    
    me_list = json.loads(me.text)
    me.close()

    print("粉絲："+str(me_list['#followers'])+" 好友："+str(me_list['#followings'])+" 我的照片："+str(me_list['#stories']))

    try:
        nextlocation = str(r.headers['X-Pagination-Next'])
    
    except :
        print('已經最後一頁了，休息15分鐘再開始')
        nextlocation = ''
        for i in range(1,16):
            mins = 16 - i
            print('還有 '+ str(mins)+' 分鐘...')
            time.sleep(60)
    
    
    likeround += 1
    time.sleep(5)
    
    