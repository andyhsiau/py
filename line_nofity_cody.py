import requests

def lineNotify(token, msg):

    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post(url, headers = headers, data = payload)
    print r.status_code

def lineNotifyPic(token, pic_url):

    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': "1",
                'imageThumbnail':pic_url,
                'imageFullsize': pic_url,
                }
    r = requests.post(url, headers = headers, data = payload)
    print r.status_code

token = "7kxQeLiGzyAuHiMvkYWA1naurg0aETk7uOYgKw7SeLu" #andy
token2 = "bAOk8FnEFE06iFGFWec9emYZwfDcpHLXL0fXxeOFAla" #cody

# lineNotify(token, "./123.jpg")

# lineNotifyPic(token, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0auPmUQ3d4eT4FkLa6jApMR_mVsE8sKTzN4AUFJCzT19h0dew")
# lineNotifyPic(token2, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0auPmUQ3d4eT4FkLa6jApMR_mVsE8sKTzN4AUFJCzT19h0dew")



