# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_apkfile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_APK_File_Form(object):
    def setupUi(self, APK_File_Form):
        APK_File_Form.setObjectName("APK_File_Form")
        APK_File_Form.resize(400, 210)
        self.frame_drag = QtWidgets.QFrame(APK_File_Form)
        self.frame_drag.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.frame_drag.setAutoFillBackground(True)
        self.frame_drag.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_drag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_drag.setObjectName("frame_drag")
        self.label = QtWidgets.QLabel(self.frame_drag)
        self.label.setGeometry(QtCore.QRect(140, 70, 102, 12))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_filename = QtWidgets.QLineEdit(APK_File_Form)
        self.lineEdit_filename.setGeometry(QtCore.QRect(10, 180, 291, 23))
        self.lineEdit_filename.setReadOnly(True)
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.pushButton_file = QtWidgets.QPushButton(APK_File_Form)
        self.pushButton_file.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.pushButton_file.setObjectName("pushButton_file")

        self.retranslateUi(APK_File_Form)
        QtCore.QMetaObject.connectSlotsByName(APK_File_Form)

    def retranslateUi(self, APK_File_Form):
        _translate = QtCore.QCoreApplication.translate
        APK_File_Form.setWindowTitle(_translate("APK_File_Form", "Form"))
        self.label.setText(_translate("APK_File_Form", "拖拽apk文件到这里"))
        self.pushButton_file.setText(_translate("APK_File_Form", "浏览"))
