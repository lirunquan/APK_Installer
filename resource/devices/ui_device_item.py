# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_device_item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Device_Item_Form(object):
    def setupUi(self, Device_Item_Form):
        Device_Item_Form.setObjectName("Device_Item_Form")
        Device_Item_Form.resize(350, 20)
        self.label_serial = QtWidgets.QLabel(Device_Item_Form)
        self.label_serial.setGeometry(QtCore.QRect(20, 2, 120, 16))
        self.label_serial.setObjectName("label_serial")
        self.label_model = QtWidgets.QLabel(Device_Item_Form)
        self.label_model.setGeometry(QtCore.QRect(180, 2, 120, 16))
        self.label_model.setObjectName("label_model")

        self.retranslateUi(Device_Item_Form)
        QtCore.QMetaObject.connectSlotsByName(Device_Item_Form)

    def retranslateUi(self, Device_Item_Form):
        _translate = QtCore.QCoreApplication.translate
        Device_Item_Form.setWindowTitle(_translate("Device_Item_Form", "Form"))
        self.label_serial.setText(_translate("Device_Item_Form", "设备序列号"))
        self.label_model.setText(_translate("Device_Item_Form", "设备品牌"))
