# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
from PyQt5 import QtGui

from resource.apkfile.ui_apkfile import Ui_APK_File_Form
from PyQt5.QtWidgets import QWidget, QFileDialog
from controller.adb_controller import ADBController


class ApkWidget(QWidget, Ui_APK_File_Form):

    def __init__(self, *args, **kwargs):
        super(ApkWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.frame_drag.setStyleSheet('background-color : #B9F9C5')
        self.pushButton_file.clicked.connect(self.open_file_window)
        self.setAcceptDrops(True)

    def open_file_window(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Install apk', '.', '*.apk')
        self.lineEdit_filename.setText(file)
        ADBController.add_apk(file)

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        self.label.setText('拖拽apk文件到这里')
        a0.accept()

    def dragMoveEvent(self, a0: QtGui.QDragMoveEvent) -> None:
        pass

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        if self.frame_drag.pos().x() <= a0.pos().x() <= self.frame_drag.pos().x() + self.frame_drag.width() \
                and self.frame_drag.pos().y() <= a0.pos().y() <= self.frame_drag.pos().y() + self.frame_drag.height():
            name = a0.mimeData().text().replace('file:///', '')
            print(name)
            if not name.endswith('.apk'):
                self.label.setText('需要.apk后缀的文件')
            else:
                self.lineEdit_filename.setText(name)
                # self.filename.emit(name)
                ADBController.add_apk(name)

