import requests
import qrcode 
import time
import re

url = "https://passport.bilibili.com/qrcode/getLoginUrl"
data = requests.get(url).json()
login_url = data['data']['url']
oauthKey = data['data']['oauthKey']

img = qrcode.make(login_url)
with open('img/login.png', 'wb') as f:
    img.save(f)

post_data = dict(
    oauthKey = oauthKey,
    gourl = "https://www.bilibili.com/"
    )

while True:
    response = requests.post("https://passport.bilibili.com/qrcode/getLoginInfo",data=post_data)
    return_data = response.json()
    if return_data['data'] == -4:
        print("没扫描")
    elif return_data['data'] == -5:
        print("没确认")
    elif return_data['data'] == -2:
        print("已过期")
    elif return_data['status'] == True:
        print(return_data)
        break
    time.sleep(1)

headers={
"Origin": "https://space.bilibili.com",
"Referer": "https://space.bilibili.com/70588783",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

# session.get(verify_url,headers=headers)
# session.get(verify_url.replace("https://passport.biligame.com/","https://passport.bigfun.cn/"))
# session.get(verify_url.replace("https://passport.biligame.com/","https://passport.bigfunapp.cn/"))
session = requests.session()

verify_url = return_data["data"]["url"]
info_url = "https://api.bilibili.com/x/web-interface/nav"
headers={
"Origin": "https://space.bilibili.com",
"Referer": "https://space.bilibili.com/70588783",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
"Cookie":re.findall("&(SESSDATA=.*?)&bili_jct",verify_url)[0]
}
response = session.get(info_url,headers=headers)
face_url = response.json()['data']['face']
nickname = response.json()['data']['uname']


# https://passport.biligame.com/crossDomain?DedeUserID=70588783&DedeUserID__ckMd5=bac55b07301ecc2e&Expires=2592000&SESSDATA=164f1f8e%2C1581615727%2C7a180b11&bili_jct=573aca659349134f618cbf38bc6438cb&gourl=https%3A%2F%2Fspace.bilibili.com%2F70588783
# https://passport.bigfun.cn/crossDomain?DedeUserID=70588783&DedeUserID__ckMd5=bac55b07301ecc2e&Expires=2592000&SESSDATA=164f1f8e%2C1581615727%2C7a180b11&bili_jct=573aca659349134f618cbf38bc6438cb&gourl=https%3A%2F%2Fspace.bilibili.com%2F70588783
# https://passport.bigfunapp.cn/crossDomain?DedeUserID=70588783&DedeUserID__ckMd5=bac55b07301ecc2e&Expires=2592000&SESSDATA=164f1f8e%2C1581615727%2C7a180b11&bili_jct=573aca659349134f618cbf38bc6438cb&gourl=https%3A%2F%2Fspace.bilibili.com%2F70588783