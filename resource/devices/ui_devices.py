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
        Devices_Form.resize(395, 174)
        self.layoutWidget = QtWidgets.QWidget(Devices_Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_devices = QtWidgets.QTableWidget(self.layoutWidget)
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
        self.verticalLayout.addWidget(self.tableWidget_devices)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_all = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_all.setObjectName("checkBox_all")
        self.horizontalLayout.addWidget(self.checkBox_all)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_refresh = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

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
