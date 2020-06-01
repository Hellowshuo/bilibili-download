from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time,sys,os
sys.path.append("..")
from Qthread.thread_login import Login_Thread

class Login_Dialog(QDialog):
    """docstring for Login_dialog"""
    login_done = pyqtSignal(dict)
    def __init__(self,config_data):
        super(Login_Dialog, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("用手机b站客户端扫描此二维码")
        self.label = QLabel("正在加载二维码.....")
        self.layout = QVBoxLayout(self) #实例化一个水平布局
        self.label_info = QLabel("")
        self.layout.addWidget(self.label) #在软件布局中添加按钮控件
        self.layout.addWidget(self.label_info)
        self.login_work = Login_Thread()

        self.login_work.qrcode_done.connect(self.loadqrcode)
        self.login_work.update.connect(self.update)
        self.islogin = False
        self.config_data = config_data
        self.login()

    def login(self):
        self.login_work.cookie = ""
        self.login_work.config_data = self.config_data
        self.login_work.start()

    def loadqrcode(self,data):
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.label.setPixmap(pixmap)

    def update(self,data):
        if data['done']:
            self.login_done.emit(data)
            self.close()
        else:
            self.label_info.setText(data['info'])
            
    def check_login(self):
        cookie = self.config_data['cookie']
        self.login_work.cookie = cookie
        self.login_work.config_data = self.config_data
        self.login_work.start()

if __name__=='__main__':
    os.chdir("..")
    app = QApplication(sys.argv)
    mywin = Login_Dialog({"cookie":"1"})
    mywin.show()
    sys.exit(app.exec_())

