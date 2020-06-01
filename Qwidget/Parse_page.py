#PyQt5窗体式例
import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
sys.path.append("..")
# 调用引入

from Qwidget.parse_page_ui import Ui_Form
from Qwidget.Progress_ui import Progress_Ui
from Qthread.thread_parse import ParseThread
from Qthread.thread_download import Download_thread


class Parse_Page(QWidget,Ui_Form):
    update_status = pyqtSignal(dict)
    def __init__(self,config_data):
        super(Parse_Page, self).__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.config_data = config_data
        self.parse_work = ParseThread()
        self.parse_work.parse_done.connect(self.parse_done)
        self.download_work = Download_thread()
        self.download_work.update.connect(self.update)
        self.download_work.download_done.connect(self.update_download_status)
        self.download_work.combine_done.connect(self.update_combine_status)

    def all_select(self,check):
        for index in range(len(self.data['data'])):
            item = self.listWidget.item(index)
            item_widget =self.listWidget.itemWidget(item)
            item_widget.checkBox.setChecked(check)
    
    def parse_done(self,data):
        self.update_status.emit({"code":0,"info":"解析完成"})
        self.listWidget.clear()
        self.checkBox.setEnabled(True)
        self.pushButton_download.setEnabled(True)
        self.data = data

        for item in data['data']:
            progressitem = Progress_Ui()
            progressitem.label_title.setText(item["title"])
            if data['type'] == 'bangumi':
                if item["vip"]:
                    progressitem.label_vip.setText(item["vip"])
                    progressitem.label_vip.setStyleSheet("background:rgba(255,0,0,0.1);border-radius:5px")
            listitem = QListWidgetItem()
            listitem.setSizeHint(QSize(10, 100))
            self.listWidget.addItem(listitem)
            self.listWidget.setItemWidget(listitem,progressitem)


    def start_parse(self):
        url = self.lineEdit_url.text()
        if url:
            self.update_status.emit({"code":1,"info":"解析中....."})
            self.parse_work.url = url
            self.parse_work.config_data = self.config_data
            self.parse_work.start()

    def start_download(self):
        download = False
        for index in range(len(self.data['data'])):
            item = self.listWidget.item(index)
            item_widget =self.listWidget.itemWidget(item)
            if item_widget.checkBox.isChecked():
                download = True
                self.data['data'][index]['select'] = True
            else:
                self.data['data'][index]['select'] = False

        if download:
            self.update_status.emit({"code":1,"info":"正在下载....."})
            self.download_work.data = self.data
            self.download_work.data['download_dir'] = self.config_data.get('download_dir','.')
            self.download_work.start()
        else:
            QMessageBox().about(self,"提示",'我不知道下什么?')

    def update(self,data):
        item = self.listWidget.item(data['index'])
        item_widget =self.listWidget.itemWidget(item)
        item_widget.progressBar.setValue(data['progress'])

    def update_download_status(self):
        self.update_status.emit({"code":0,"info":"下载完成"})

    def update_combine_status(self,status):
        if status:
            self.update_status.emit({"code":0,"info":"合成完成"})
        else:
            self.update_status.emit({"code":1,"info":"正在合成视频....."})


if __name__=='__main__':
    os.chdir("..")
    app = QApplication(sys.argv)
    mywin = Parse_Page({"download_dir":"/home/wshuo/Desktop"})
    mywin.show()
    sys.exit(app.exec_())
