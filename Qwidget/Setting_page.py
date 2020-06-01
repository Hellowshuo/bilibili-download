#PyQt5窗体式例
import sys,os,pickle,platform,shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
sys.path.append("..")
# 调用引入

from Qwidget.setting_page_ui import Ui_Form

class Setting_Page(QWidget,Ui_Form):
    config_update = pyqtSignal(dict)
    def __init__(self):
        super(Setting_Page, self).__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.config_data = self.load_config()
        self.init_widget()

    def init_widget(self):
        self.label_path.setText(self.config_data['download_dir'])
        self.update_img()


    def update_img(self):
        pixmap = QPixmap()
        background_path = os.path.join(self.config_dir,"background")
        with open(background_path,'rb') as f:
            data = f.read()
        pixmap.loadFromData(data)
        pixmap = pixmap.scaled(400,250,aspectRatioMode=Qt.IgnoreAspectRatio)
        self.label_background.setScaledContents(True)
        self.label_background.setPixmap(pixmap)

    def load_config(self):
        if platform.system() == 'Linux':
            print('Linux')
            self.config_path = os.environ['HOME']+'/bilibili/.bilidata'
        else:
            print('Windows')
            self.config_path = 'C:\\ProgramData\\bilibili\\.bilidata'

        # 如果第一次运行这个软件
        self.config_dir = os.path.dirname(self.config_path)
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
            background_path = os.path.join(self.config_dir,"background")
            if not os.path.exists(background_path):
                from data.background import background_data
                with open(background_path,"wb") as f:
                    f.write(background_data)

        if not os.path.exists(self.config_path):
            self.config_data = dict(
                config_dir = self.config_dir,
                download_dir = ".",
                background_dir = ".",
                cookie = "",
                nickname = "",
                vip = "",
                )
            self.save_config()

        with open(self.config_path,"rb") as f:
            data = pickle.load(f)
        return data

    def save_config(self):
        with open(self.config_path,'wb') as f:
            pickle.dump(self.config_data,f)

        self.config_update.emit(self.config_data)

    def change_background(self):
        path = self.config_data['background_dir']
        fileChosen = QFileDialog.getOpenFileName(self, '选择图片作为背景', path,"图片(*.jpg *.png)")
        if fileChosen[0]:
            background_dir = os.path.dirname(fileChosen[0])
            shutil.copyfile(fileChosen[0],os.path.join(self.config_data['config_dir'],"background"))
            self.update_img()
            self.config_data['background_dir'] = background_dir
            self.save_config()

    def change_down_path(self):
        path = self.config_data["download_dir"] 
        folderChosen = QFileDialog.getExistingDirectory(self, '选择下载视频保存路径', path)
        if folderChosen:
            self.label_path.setText(folderChosen)
            self.config_data['download_dir'] = folderChosen
            self.save_config()

if __name__=='__main__':
    os.chdir("..")
    app = QApplication(sys.argv)
    mywin = Setting_Page()
    mywin.show()
    sys.exit(app.exec_())
