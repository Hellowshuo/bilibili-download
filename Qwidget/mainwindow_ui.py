# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 662)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1057, 662))
        MainWindow.setMaximumSize(QtCore.QSize(1057, 662))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_move = QtWidgets.QLabel(self.centralwidget)
        self.label_move.setGeometry(QtCore.QRect(0, 0, 931, 51))
        self.label_move.setStyleSheet("")
        self.label_move.setText("")
        self.label_move.setObjectName("label_move")
        self.pushButton_mini = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mini.setGeometry(QtCore.QRect(970, 10, 31, 31))
        self.pushButton_mini.setObjectName("pushButton_mini")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(1010, 10, 31, 31))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_main = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_main.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.pushButton_main.setObjectName("pushButton_main")
        self.pushButton_parse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_parse.setGeometry(QtCore.QRect(110, 60, 101, 41))
        self.pushButton_parse.setObjectName("pushButton_parse")
        self.pushButton_setting = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setting.setGeometry(QtCore.QRect(210, 60, 101, 41))
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 110, 1031, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(980, 50, 50, 50))
        self.pushButton_login.setObjectName("pushButton_login")
        self.label_vip = QtWidgets.QLabel(self.centralwidget)
        self.label_vip.setGeometry(QtCore.QRect(919, 61, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_vip.setFont(font)
        self.label_vip.setText("")
        self.label_vip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vip.setObjectName("label_vip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pushButton_mini.clicked.connect(MainWindow.showMinimized)
        self.pushButton_close.clicked.connect(MainWindow.close)
        self.pushButton_setting.clicked.connect(MainWindow.change_setting_page)
        self.pushButton_parse.clicked.connect(MainWindow.change_parse_page)
        self.pushButton_main.clicked.connect(MainWindow.change_main_page)
        self.pushButton_login.clicked.connect(MainWindow.login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_mini.setText(_translate("MainWindow", "-"))
        self.pushButton_close.setText(_translate("MainWindow", "×"))
        self.pushButton_main.setText(_translate("MainWindow", "主页"))
        self.pushButton_parse.setText(_translate("MainWindow", "解析"))
        self.pushButton_setting.setText(_translate("MainWindow", "设置"))
        self.pushButton_login.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))

