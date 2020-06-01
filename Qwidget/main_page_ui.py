# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(894, 504)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_famous_saying = QtWidgets.QFrame(Form)
        self.frame_famous_saying.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_famous_saying.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_famous_saying.setObjectName("frame_famous_saying")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_famous_saying)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addWidget(self.frame_famous_saying, 0, 1, 1, 2)
        self.frame_setting = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_setting.sizePolicy().hasHeightForWidth())
        self.frame_setting.setSizePolicy(sizePolicy)
        self.frame_setting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_setting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_setting.setObjectName("frame_setting")
        self.gridLayout.addWidget(self.frame_setting, 2, 2, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(202, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.frame_start = QtWidgets.QFrame(Form)
        self.frame_start.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_start.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_start.setObjectName("frame_start")
        self.gridLayout.addWidget(self.frame_start, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(658, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 224, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(8, 180, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(636, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

