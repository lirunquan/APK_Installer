# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from resource.main.ui_main import Ui_Main_Form


class MainWindow(QMainWindow, Ui_Main_Form):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
