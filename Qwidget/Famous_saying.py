from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests
import sys
import os
sys.path.append("..")
from Qwidget.famous_saying_ui import Ui_Form
from Qthread.thread_famous_saying import Famous_saying_thread

class Famous_Saying(QWidget,Ui_Form):
    """docstring for Famous_Saying"""
    def __init__(self):
        super(Famous_Saying, self).__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_update)
        self.timer.start(7000)
        self.famous_saying_thread = Famous_saying_thread()
        self.famous_saying_thread.update.connect(self.update_famous)
        self.famous_saying_thread.start()

    def update_famous(self,data):
        self.label_saying.setText(data["hitokoto"]+"\n\t———"+data["source"])

    def time_update(self):
        self.famous_saying_thread.start()

if __name__=='__main__':
    os.chdir("..")
    app = QApplication(sys.argv)
    mywin = Famous_Saying()
    mywin.show()
    sys.exit(app.exec_())

