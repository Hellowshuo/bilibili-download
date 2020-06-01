#PyQt5窗体式例
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Qwidget.mainwindow_ui import Ui_MainWindow
from Qwidget.Parse_page import Parse_Page
from Qwidget.Setting_page import Setting_Page
from Qwidget.Login_dialog import Login_Dialog
from Qwidget.Main_page import Main_Page
import requests
import os


# https://www.bilibili.com/video/av67964765
# https://www.bilibili.com/video/av15478453
# https://www.bilibili.com/bangumi/play/ep267692

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        # 初始化操作
        self.config_data = {}
        self.m_flag = False
        self.islogin = False
        self.config_dir = ""

        self.init_page()
        self.init_style()
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_status)
        self.change_main_page()
        self.config_data = self.Setting_Page.config_data
        self.check_login()

    def init_style(self):
        # border_transparent = 0.45
        self.setStyleSheet(
        # 主页面
        "QPushButton{border-image:none;border:1px solid rgba(255, 255, 255,0.45);background-color:rgba(100, 100, 100,0.5);color:white;background:rgba(0,0,0,0.1);}"
        "QPushButton:hover{background:rgba(0,0,0,0.5);}"
        "QPushButton:pressed{color:rgba(0,0,0,0.5);background:rgba(255,255,255,0.5);}"
        "MyMainWindow{border-image: url(%s);color:white}"
        "QLineEdit{background:transparent;border:1px solid rgba(255, 255, 255,0.45);color:white;border-radius:5px;}"
        "#label_move:hover{background:rgba(0,0,0,0.1);}"
        "#pushButton_main{border-top-left-radius:10px;border-bottom-left-radius:10px}"
        "#pushButton_setting{border-top-right-radius:10px;border-bottom-right-radius:10px}"
        "#pushButton_mini{border-radius:5px;background:rgba(0,255,0,0.1)}"
        "#pushButton_close{border-radius:5px;background:rgba(255,0,0,0.1)}"
        "#frame{border:1px solid rgba(255, 255, 255,0.45)}"
        "#pushButton_login{border-radius:25px;}"
        "#statusBar{color:white}"


        #解析页面
        # "#lineEdit_url{border:1px solid rgba(255,255,255,0.45)}"
        "#pushButton_download{border-radius:5px;}"
        "#checkBox{background:transparent;color:white;}"
        "#checkBox::indicator::unchecked{background:transparent;border:1px solid white}"
        "#checkBox::indicator::checked{background:rgba(255,255,255,1)}"

        "Parse_Page{background:transparent;}"
        "#listWidget{color:white;background:transparent;}"
        "Progress_Ui{background:transparent;color:white;}"
        "QLabel{color:white;background:transparent}"
        "QProgressBar{color:white;background:rgba(0,0,0,0.2)}"
        "QProgressBar::chunk{background:rgba(0,255,0,0.3)}"
        "QScrollBar{background:transparent;width:10px;}"
        "QScrollBar::handle{background:rgba(0,0,0,0.4);border-radius:6px;min-height:60px;}"
        # "QScrollBar::handle:vertical:hover{background:rgba(0,0,0,0.3);}"
        "QScrollBar::add-line:vertical{background:rgba(0,0,0,0.3);}"
        "QScrollBar::sub-line:vertical{background:rgba(0,0,0,0.3);}"
        #设置界面
        "#label_background{border:1px solid rgba(255,255,255,0.45);}"
        "#label_path{border:1px solid rgba(255,255,255,0.45);border-radius:5px;}"
        "#pushButton_download_path{border-radius:5px;}"
        "#pushButton_background_path{border-radius:5px;}"
        % os.path.join(self.config_dir,"background")
        )

    def init_page(self):
        self.Setting_Page = Setting_Page()
        self.Setting_Page.config_update.connect(self.config_update)
        self.config_dir = self.Setting_Page.config_dir

        self.Main_Page = Main_Page()
        self.Parse_Page = Parse_Page(self.Setting_Page.load_config())
        self.Parse_Page.update_status.connect(self.update_status)


    def mousePressEvent(self, event):
        lable_x = self.label_move.geometry().x()
        lable_y = self.label_move.geometry().y()
        lable_width = self.label_move.geometry().width()
        lable_height = self.label_move.geometry().height()
        x = (event.globalPos()-self.pos()).x()
        y = (event.globalPos()-self.pos()).y()
        if event.button() == Qt.LeftButton and lable_x < x < lable_x +lable_width and lable_y < y < lable_y+lable_height:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def change_main_page(self):
        self.Parse_Page.setParent(None)
        self.Setting_Page.setParent(None)
        self.Main_Page.setParent(self.frame)
        self.verticalLayout.addWidget(self.Main_Page)

    def change_parse_page(self):
        self.Main_Page.setParent(None)
        self.Setting_Page.setParent(None)
        self.Parse_Page.setParent(self.frame)
        self.verticalLayout.addWidget(self.Parse_Page)

    def change_setting_page(self):
        self.Main_Page.setParent(None)
        self.Parse_Page.setParent(None)
        self.Setting_Page.setParent(self.frame)
        self.verticalLayout.addWidget(self.Setting_Page)

    def login(self):
        if self.islogin:
            result = QMessageBox().information(None, "提示", "用户已经登录,是否重新登录", 
                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);
            if result == 16384:
                self.login_dialog = Login_Dialog(self.config_data)
                self.login_dialog.login_done.connect(self.login_done)
                self.login_dialog.exec_()
            else:
                print("取消")
        else:
            self.login_dialog = Login_Dialog(self.config_data)
            self.login_dialog.login_done.connect(self.login_done)
            self.login_dialog.exec_()

    def check_login(self):
        self.login_dialog = Login_Dialog(self.config_data)
        self.login_dialog.login_done.connect(self.login_done)
        self.login_dialog.check_login()

    def login_done(self,data):  
        self.islogin = True
        self.pushButton_login.setStyleSheet("border-image:url(%s)" % os.path.join(self.config_dir,'.face'))
        self.pushButton_login.setText("")
        self.pushButton_login.setToolTip(data["nickname"])
        if data['vip']:
            self.label_vip.setStyleSheet("#label_vip{background:rgba(255,192,203,0.3);color:white;border-radius:10px}")
            self.label_vip.setText("大会员")
        else:
            self.label_vip.setStyleSheet("#label_vip{background:transparent;color:white;border-radius:10px}")
            self.label_vip.setText("")

        self.Setting_Page.config_data['vip'] = data['vip']
        self.Setting_Page.config_data['nickname'] = data['nickname']
        self.Setting_Page.config_data['cookie'] = data['cookie']
        self.Setting_Page.save_config()

    def config_update(self,data):
        self.config_data = data
        self.init_style()
        self.Parse_Page.config_data = data

    def update_status(self,data):
        if data['code'] == 1:
            self.status_str = data['info']
            self.now_str = self.status_str.replace(".","")
            self.timer.start(100)
        elif data['code'] == 0:
            self.timer.stop()
            self.statusBar.showMessage(data['info'])

    def show_status(self):
        if self.now_str == self.status_str:
            self.now_str = self.status_str.replace(".","")
        else:
            self.now_str += "."
        self.statusBar.showMessage(self.now_str)

if __name__=='__main__':
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())
