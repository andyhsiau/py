# coding=utf-8
import os
import lineTool
import requests
import json
import time
import random

line_token = {
#    'S01': 'KEY',
	'A01': '7kxQeLiGzyAuHiMvkYWA1naurg0aETk7uOYgKw7SeLu'
}
#print(str(len(line_token.values())))

msg = '' 
#lineTool.lineNotify(line_token, msg)
	
api_url = 'https://api.lit.live/me/stories'

token_index = 0

tokens = {
#   'S01': '',
    'A01': 'b303a83cc69798cfe9589ec12e7c07f7486e78e838ae684fef868689ae3c2f6d9b67600e1b0801a3da92877521ee134e4ebe71f25f97410e70de46f02a1c7a91f54e1e4aae06099d1f07e5cc7680e6fb8b2ab59dc1a5e3d18301a9973ef5cd9d1cc7ec1076cbe6f9698ca3a2bb166d31b18680b9d18b320eb6e73c5f54bca47810d748b3d90df30f995d830cb4ef2f253e796b121de1ca1f43c487ed6a4e46d157df9007fbf249f2ee8e31ad09fbaa43d88b8e83760715f7b2978d2387116278b0c7f8a970938ffdba8549a490dde6143826a2c8ceae49221ec4a34f25062ab86cdbf44ec9e24a01a6c1046018ed0bb7b78546dd968a299f804e7069d12f158d2b7fb22322e7732a7554447168d9d7bbc8e6b6a6093115b47e7fb2cb87e1ee4cbeca0f2e9a2716537bea4aafd49eb77819730e408e3ea2676e9d4b76b812f73aa6790149fdd75a0df7a90657a1e2f2641985ea29362299d31d23ae2fee9b466cc2e0555b427ffda8f3d5f6c1a32fb668'
}



def lineNotify(line_token, msg): 
	url = "https://notify-api.line.me/api/notify"
	headers = {
		"Authorization": "Bearer " + list(line_token.values())[token_index], 
		"Content-Type" : "application/x-www-form-urlencoded"
	}

	payload = {'message': msg}
	r = requests.post(url, headers = headers, params = payload)
	return r.status_code

def total_mith():
	print('計算中...')
	token_post = {
		'Accept-Encoding': 'gzip',
		'User-Agent': 'Lit/1.1.1 (com.masterplan.lit; build:1.1.1; iOS 11.4.1) Alamofire/4.6.0',
		'Content-Type': 'application/json',
		'Authorization': list(tokens.values())[token_index]
	}
	try:
		resp = requests.get(api_url, headers=token_post, timeout=10)
		#print(list(tokens.values())[token_index])
		print(resp)
		#print(list(line_token.values())[token_index])
		mith_list = json.loads(resp.text)		
		resp.close()
		mith_count = 0
		mith_msg = ''
		picunt = 1
		if len(mith_list) != 0:
			print('找到 ' + str(len(mith_list)) + ' 筆記錄')			
			for mith in mith_list:
				try:					
					mith_stories = mith['mithril']
					views = mith['#views']
					likes = mith['#likes']
					mith_msg += '\r\n' + '◎ 已有 ' + str(mith_stories) + ' 顆\r\n【View:'+str(views)+',Like:'+str(likes)+'】'
					mith_count += mith_stories				
					print('第' + str(picunt) + '張照片已有' + str(mith_stories) + ' 顆【View:'+str(views)+',Like:'+str(likes)+'】')
					picunt += 1
				except Exception as e:
					print(e)		
			resp.close()			
		print('目前總共有 : '+ str(mith_count) +' 顆')
		#lineTool.lineNotify(list(line_token.values())[token_index], mith_msg + ' \r\n※ 目前總計 : '+ str(mith_count) +' 顆\r\n● 找到( ' + str(len(mith_list)) + ' )筆記錄')
	except Exception as e:
		print(e)
		return

i = 0
while i < int(len(line_token)):
	#print(i)	
	total_mith()
	token_index = token_index + 1	
	i += 1		
	#print(token_index)		