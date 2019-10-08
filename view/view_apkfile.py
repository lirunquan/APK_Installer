# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
from PyQt5.QtCore import pyqtSignal

from resource.apkfile.ui_apkfile import Ui_APK_File_Form
from PyQt5.QtWidgets import QWidget, QFileDialog


class ApkWidget(QWidget, Ui_APK_File_Form):
    filename = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(ApkWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.frame_drag.setStyleSheet('background-color : #B9F9C5')
        self.pushButton_file.clicked.connect(self.open_file_window)

    def open_file_window(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Install apk', '.', '*.apk')
        self.lineEdit_filename.setText(file)
        self.filename.emit(file)
