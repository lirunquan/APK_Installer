# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Form(object):
    def setupUi(self, Main_Form):
        Main_Form.setObjectName("Main_Form")
        Main_Form.resize(418, 479)
        self.widget_devices = QtWidgets.QWidget(Main_Form)
        self.widget_devices.setGeometry(QtCore.QRect(0, 0, 411, 201))
        self.widget_devices.setObjectName("widget_devices")
        self.widget_apk = QtWidgets.QWidget(Main_Form)
        self.widget_apk.setGeometry(QtCore.QRect(0, 200, 411, 231))
        self.widget_apk.setObjectName("widget_apk")
        self.pushButton_install = QtWidgets.QPushButton(Main_Form)
        self.pushButton_install.setGeometry(QtCore.QRect(160, 440, 80, 24))
        self.pushButton_install.setObjectName("pushButton_install")

        self.retranslateUi(Main_Form)
        QtCore.QMetaObject.connectSlotsByName(Main_Form)

    def retranslateUi(self, Main_Form):
        _translate = QtCore.QCoreApplication.translate
        Main_Form.setWindowTitle(_translate("Main_Form", "Form"))
        self.pushButton_install.setText(_translate("Main_Form", "安装"))
