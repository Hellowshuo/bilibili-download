# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'famous_saying.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(447, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_saying = QtWidgets.QLabel(Form)
        self.label_saying.setText("")
        self.label_saying.setWordWrap(True)
        self.label_saying.setObjectName("label_saying")
        self.verticalLayout.addWidget(self.label_saying)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

