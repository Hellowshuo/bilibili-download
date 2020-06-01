#PyQt5窗体式例
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
try:
    from progress_ui_ui import Ui_Form_progress as Ui_Form
except Exception:
    from Qwidget.progress_ui_ui import Ui_Form_progress as Ui_Form

class Progress_Ui(QListWidget,Ui_Form):
    def __init__(self):
        super(Progress_Ui, self).__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)

if __name__=='__main__':
    app = QApplication(sys.argv)
    mywin = Progress_Ui()
    # mywin = QListWidget()
    # mywin.addItem(Progress_Ui())
    mywin.show()
    sys.exit(app.exec_())
