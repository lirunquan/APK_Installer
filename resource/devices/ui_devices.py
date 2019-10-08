# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_devices.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Devices_Form(object):
    def setupUi(self, Devices_Form):
        Devices_Form.setObjectName("Devices_Form")
        Devices_Form.resize(400, 180)
        self.widget = QtWidgets.QWidget(Devices_Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_devices = QtWidgets.QListWidget(self.widget)
        self.listWidget_devices.setObjectName("listWidget_devices")
        self.verticalLayout.addWidget(self.listWidget_devices)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_all = QtWidgets.QCheckBox(self.widget)
        self.checkBox_all.setObjectName("checkBox_all")
        self.horizontalLayout.addWidget(self.checkBox_all)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_refresh = QtWidgets.QPushButton(self.widget)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Devices_Form)
        QtCore.QMetaObject.connectSlotsByName(Devices_Form)

    def retranslateUi(self, Devices_Form):
        _translate = QtCore.QCoreApplication.translate
        Devices_Form.setWindowTitle(_translate("Devices_Form", "Form"))
        self.checkBox_all.setText(_translate("Devices_Form", "全选"))
        self.pushButton_refresh.setText(_translate("Devices_Form", "刷新"))
