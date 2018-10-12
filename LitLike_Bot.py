# coding=utf-8
import requests
import json
import time
import random
from bs4 import BeautifulSoup


tokens = [
    '1264565c1caaa1259e414dc598798449daefa1909ddddfe9b39e6620fe3bfb94ef2f0e740f3550927fa81d6820d33063203f1f85d64cf220ec759632822ed4d21e814bfb941349a40bf47f86c6007d7ae5ec61c2abd8adf65168256213bd6d4053956806b91e9db09b5d17e73068f134596de460c1271887da5fd38deac732e39935a35061aa2a6be67d4f67a9fa012caa7e11061356cc877b6cd095e84ed2e0675616f1f6cbe785d6fe8bc06124b2e6a4b811b92ac82263c7a19db0d2a584485955018084e68e0833d8dcb19f24ae323a0c8e0fd40747480bf2702969cc2240dffb7667735dd7e0c3dab35ab4074edbed89e812e9957ef6224b272d89a29d7dea9c16407cb799f15f5af9fe5d5477e645c5212ea7854550b850a540d5b55ed9204a4a04bf68643e77a92aaa3f923022d696615b13cd36d53a298d4e81946ee7d14d7232d2381db4f7b311419b2dfa3534d1a5b3c0773eb314b0d6dc9e787ba78e2fc127baf216b4c4b17ad4441f9ef1',
    #[0]  rock7817@hotmail.com
    '89d84756c7f42832eb69950fd56003211c7f3f35dd4b29f4b5760fff8c6906c8569756c32786b20ef537c212b4c6de8b436ea44d88447a03fcd038b48dd5517bbab9aabfc223ca1841f2e8912621beeb2a9b7dac3351299ba2be578116b594c1e39bbb97463285f54da62bbe7527eeefa3a505cc4ca12dcede729fc980e81dffe19df8c64233171d4226304dc0555f8cbbd6805b3e4ebe58b17e41bbf325fb97fcc6d39deeef7a93a7dcb3978b1584a043a70511a4a2817ca58410f73743830e50b4ab9bd7846abd7f6826bd9b392bce322856029cb8a84b0eb6c330a9bbc5f08fdbeab1f08bb1828c726569802a5f9061544136c164d45d70723ac52eb448037c670a9b11ec3297972a031f60af503339b43f39ed68842f8a8d3ece66157711bb5a15e42ac83bd7e4722b1c5117928ccc483118ef6090f8fa5c218a96067706a9baa62a478f2ad7f39e26bcd554670f0960988406cef530be2a33863b0170e716176f33450a4f108cb62bbfd3191545',
    #[1]  koet0312
    'b303a83cc69798cfe9589ec12e7c07f7486e78e838ae684fef868689ae3c2f6d9b67600e1b0801a3da92877521ee134e4ebe71f25f97410e70de46f02a1c7a91f54e1e4aae06099d1f07e5cc7680e6fb8b2ab59dc1a5e3d18301a9973ef5cd9d1cc7ec1076cbe6f9698ca3a2bb166d31b18680b9d18b320eb6e73c5f54bca47810d748b3d90df30f995d830cb4ef2f253e796b121de1ca1f43c487ed6a4e46d157df9007fbf249f2ee8e31ad09fbaa43d88b8e83760715f7b2978d2387116278b0c7f8a970938ffdba8549a490dde6143826a2c8ceae49221ec4a34f25062ab86cdbf44ec9e24a01a6c1046018ed0bb7b78546dd968a299f804e7069d12f158d2b7fb22322e7732a7554447168d9d7bbc8e6b6a6093115b47e7fb2cb87e1ee4cbeca0f2e9a2716537bea4aafd49eb77819730e408e3ea2676e9d4b76b812f73aa6790149fdd75a0df7a90657a1e2f2641985ea29362299d31d23ae2fee9b466cc2e0555b427ffda8f3d5f6c1a32fb668'
    #[2] 0979808751
    
]


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

def pic_list(user,nextf) :
    
    header = {

        'Authorization': tokens[user],
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'

    }

    r = requests.get('https://api.lit.live/stories/discover?next=', headers=header)
    piclist = json.loads(r.text)
    r.close()

    if len(piclist) < 8 :
        
        r = requests.get('https://api.lit.live/stories/featured?next='+featured_next(user,nextf), headers=header)
        piclist = json.loads(r.text)
        r.close()

    
        

    return piclist

def featured_next(user,nextf) :

    header = {
        'Authorization': tokens[user],
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'
    }    
    
    r = requests.get('https://api.lit.live/stories/featured?next='+nextf, headers=header)
    try:
        nextlocation = str(r.headers['X-Pagination-Next'])    
    except :        
        nextlocation = ''
    r.close()        

    return nextlocation



def like_pic(user, picid) :
    
    header = {

        'Authorization': tokens[user],
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'

    }

    puturl = str('https://api.lit.live/stories/'+picid+'/like')
    p = requests.put(puturl, headers=header)    

    return p.status_code

def follow(user,storyid) :
                  
    header = {

        'Authorization': tokens[user],
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'

    }
    f = requests.put('https://api.lit.live/users/'+storyid+'/follow', headers = header)

    return f.status_code

def report_mith(user) :

    header = {

        'Authorization': tokens[user],
        'Host': 'api.lit.live',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0'

    }

    m = requests.get('https://api.lit.live/me/stories', headers = header)
    mith_list = json.loads(m.text)
    m.close()
    mith_count = 0
    for mith in mith_list:
        mith_stories = mith['mithril']
        mith_count += mith_stories

    if earncount[user] == 0:
        earn[user] = mith_count
        earncount[user] = 1
    
    time.sleep(1)
    print('======User '+str(user+1)+' 即時回報======')
    print('目前累記按了 '+str(likecount[user])+' 個讚')
    print('重覆瀏覽 '+str(alreadylike[user])+' 張照片')
    print('此次運行賺了 '+str(mith_count-earn[user])+' 顆秘銀幣')
    print('目前累記賺了 '+str(mith_count)+' 顆秘銀幣')

    me = requests.get('https://api.lit.live/me' , headers = header)    
    me_list = json.loads(me.text)
    me.close()
    try:
        print('帳號秘銀幣餘額：'+str(me_list['vault_mithril'])+' 顆')
        print('財產試算：'+str(me_list['vault_mithril']+mith_count)+' 顆'+' 相當於台幣：'+ str((me_list['vault_mithril']+mith_count)*getmithcurrency())+' 元')
    except:
        print('帳號秘銀幣餘額：未知')
    
    print("粉絲："+str(me_list['#followers'])+" 好友："+str(me_list['#followings'])+" 我的照片："+str(me_list['#stories']))
    print('舊朋友：'+str(friend[user])+" 新朋友："+str(unfriend[user]))
    print('Error Occur : '+str(errorcount)+"\n==========================\n")
    if mith_count-earn[user] < 0 :
        lineNotify(linetoken, '帳號 ' + str(user+1) + ' 需要補充照片')

    return

def lineNotify(token, msg):
     
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code

linetoken = "7kxQeLiGzyAuHiMvkYWA1naurg0aETk7uOYgKw7SeLu"

#######################################################################

print('\nLit Like Bot Ver2.0\nDesign by AndyHsiau\nStart Running...\n')

earncount = []
likecount = []
alreadylike = []
friend = []
unfriend = []
earn = []
nextlocation = ''
errorcount = 0

for i in range(len(tokens)):
    earncount.append(0)
    likecount.append(0)
    friend.append(0)
    unfriend.append(0)
    earn.append(0)
    alreadylike.append(0)
try :
    for k in range(len(tokens)):
            
        report_mith(k)
except:
    print("Error Occur, retry after 10s...")
    time.sleep(10)
time.sleep(3)

while True :   
    
    try :
        for i in range(len(tokens)) :        
            
            
            
            print('======= User '+ str(i+1) + " Start Running ======")
            print("Find "+str(len(pic_list(i,nextlocation)))+" users")
            totalusers = len(pic_list(i,nextlocation))
            usercount = 1
            
            for story in pic_list(i,featured_next(i,nextlocation)) :            
                    
                
                #print("nextlocation= "+nextlocation)
                stories = story['stories']
                        
                if story["followed"] == False :
                    print("Start "+str(usercount)+"/"+str(totalusers)+" user...")
                    print(str(story['name'])+' is not your friend.\nAlready sent invitation...')

                    if follow(i,str(story['id'])) == 201 :
                        time.sleep(2)
                        print("\nFollow Succed !\n")
                        
                        unfriend[i] += 1
                    else :
                        print("Follow Error !\n")
                        time.sleep(2)
                else :
                    print("Start "+str(usercount)+"/"+str(totalusers)+" user...")
                    print("You and "+str(story['name'])+ " already friend.")
                    friend[i] += 1

                userpicno = 1
                
                for picid in stories :

                    print("User "+str(i+1)+" running..."+str(usercount)+"/"+str(totalusers))
                    print('Find  '+str(len(stories))+'  pictures from '+str(story['name']))                

                    if picid['liked'] == False :

                        print('/////////////////\n//             //\n//             //\n//             //\n//      '+str(userpicno)+'      /\n//             //\n//             //\n//             //\n/////////////////')                    

                        if like_pic(i,picid['id']) == 204 :
                            
                            #print('Already put like to '+str(story['name'])+"'s <<"+str(userpicno)+'>> pictures\n♥\n')
                            time.sleep(1)
                            print('              ❤\n')
                            userpicno += 1
                            likecount[i] += 1
                                        
                            time.sleep(random.randint(2,7))
                        else :
                            print('              ♡\nPut like error!!!')
                            time.sleep(1)
                            userpicno += 1
                    else :
                        print('/////////////////\n//             //\n//             //\n//             //\n//      '+str(userpicno)+'      /\n//             //\n//             //\n//             //\n/////////////////\n              ❤')
                        print("This picture already like\n")
                        alreadylike[i] += 1
                        userpicno += 1
                        time.sleep(1)

                usercount += 1

                for j in range(len(tokens)):
            
                    report_mith(j)
            
                time.sleep(3)

            if totalusers < 5 :
                print("User "+str(i+1)+" done so quick !\nWill strat next user after 5 mins...\n")
                time.sleep(300)
            else :
                print("User "+str(i+1)+" work very hard, switch to next user after 10s...")
                time.sleep(10)

        nextlocation = featured_next(i,nextlocation)    
    except :
        print("Error Occur, retry after 10s...")
        time.sleep(10)
        errorcount += 1    
    

    
      
    time.sleep(3)