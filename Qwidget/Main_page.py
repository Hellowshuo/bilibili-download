from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os

sys.path.append("..")
from Qwidget.main_page_ui import Ui_Form
from Qwidget.Famous_saying import Famous_Saying

class Main_Page(QWidget,Ui_Form):
    """docstring for Famous_Saying"""
    def __init__(self):
        super(Main_Page, self).__init__()
        self.setupUi(self)
        self.init_page()

    def init_page(self):
        self.Famous_Saying = Famous_Saying()
        self.Famous_Saying.setParent(self.frame_famous_saying)
        self.verticalLayout.addWidget(self.Famous_Saying)
        
if __name__=='__main__':
    os.chdir("..")
    app = QApplication(sys.argv)
    mywin = Main_Page()
    mywin.show()
    sys.exit(app.exec_())

