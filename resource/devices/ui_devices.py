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
        Devices_Form.resize(400, 200)
        self.tableWidget_devices = QtWidgets.QTableWidget(Devices_Form)
        self.tableWidget_devices.setGeometry(QtCore.QRect(10, 10, 381, 150))
        self.tableWidget_devices.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget_devices.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_devices.setRowCount(0)
        self.tableWidget_devices.setColumnCount(2)
        self.tableWidget_devices.setObjectName("tableWidget_devices")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_devices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_devices.setHorizontalHeaderItem(1, item)
        self.tableWidget_devices.horizontalHeader().setCascadingSectionResizes(False)
        self.checkBox_all = QtWidgets.QCheckBox(Devices_Form)
        self.checkBox_all.setGeometry(QtCore.QRect(20, 167, 47, 16))
        self.checkBox_all.setObjectName("checkBox_all")
        self.pushButton_refresh = QtWidgets.QPushButton(Devices_Form)
        self.pushButton_refresh.setGeometry(QtCore.QRect(310, 163, 75, 23))
        self.pushButton_refresh.setObjectName("pushButton_refresh")

        self.retranslateUi(Devices_Form)
        QtCore.QMetaObject.connectSlotsByName(Devices_Form)

    def retranslateUi(self, Devices_Form):
        _translate = QtCore.QCoreApplication.translate
        Devices_Form.setWindowTitle(_translate("Devices_Form", "Form"))
        item = self.tableWidget_devices.horizontalHeaderItem(0)
        item.setText(_translate("Devices_Form", "设备序列号"))
        item = self.tableWidget_devices.horizontalHeaderItem(1)
        item.setText(_translate("Devices_Form", "设备品牌"))
        self.checkBox_all.setText(_translate("Devices_Form", "全选"))
        self.pushButton_refresh.setText(_translate("Devices_Form", "刷新"))
