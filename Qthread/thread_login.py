from PyQt5.QtCore import *
import io,requests,qrcode,time,re,os

class Login_Thread(QThread):
    """docstring for Login_Thread"""
    qrcode_done = pyqtSignal(bytes)
    update = pyqtSignal(dict)
    def __init__(self):
        super(Login_Thread, self).__init__()

    def run(self):
        if self.cookie:
            self.check_login()
        else: 
            self.cookie = self.login()
            self.check_login()


    def login(self):
        url = "https://passport.bilibili.com/qrcode/getLoginUrl"
        data = requests.get(url).json()
        login_url = data['data']['url']
        oauthKey = data['data']['oauthKey']

        img = qrcode.make(login_url)
        img = img.resize((300, 300))
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='JPEG') # format: PNG / JPEG
        img_bytes = imgByteArr.getvalue()

        self.qrcode_done.emit(img_bytes)

        post_data = dict(
            oauthKey = oauthKey,
            gourl = "https://www.bilibili.com/"
            )

        while True:
            response = requests.post("https://passport.bilibili.com/qrcode/getLoginInfo",data=post_data)
            return_data = response.json()
            if return_data['data'] == -4:
                self.update.emit(dict(done=False,info="未扫描"))
            elif return_data['data'] == -5:
                self.update.emit(dict(done=False,info="没确认"))
            elif return_data['data'] == -2:
                self.update.emit(dict(done=False,info="已过期"))
            elif return_data['status'] == True:
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

        verify_url = return_data["data"]["url"]
        info_url = "https://api.bilibili.com/x/web-interface/nav"
        cookie = re.findall("&(SESSDATA=.*?)&bili_jct",verify_url)[0]
        return cookie
  
    def check_login(self):
        info_url = "https://api.bilibili.com/x/web-interface/nav"
        cookie = self.cookie
        headers={
        "Origin": "https://space.bilibili.com",
        "Referer": "https://space.bilibili.com/70588783",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Cookie":cookie
        }

        response = requests.get(info_url,headers=headers)
        try:
            face_url = response.json()['data']['face']
            nickname = response.json()['data']['uname']
            # vip = response.json()['data']["vipType"]
            vip = response.json()['data']['vipStatus']
            data = requests.get(face_url).content

            config_dir = self.config_data['config_dir']
            f_path = os.path.join(config_dir,".face")
            with open(f_path,'wb') as f:
                f.write(data)
            print(nickname,"已经登录")
            return_data = dict(
                done = True,
                nickname = nickname,
                vip = vip,
                info = "成功",
                cookie = cookie,
                )
            self.update.emit(return_data)
        except Exception as e:
            print(e)