# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QMessageBox
from resource.main.ui_main import Ui_Main_Form
from view.view_apkfile import ApkWidget
from view.view_devices import DevicesWidget
from controller.adb_controller import ADBController


class MainWindow(QMainWindow, Ui_Main_Form):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.apk_form = ApkWidget()
        # self.apk_form.filename.connect(ADBController.add_apk)
        apk_h_box = QHBoxLayout(self.widget_apk)
        apk_h_box.addWidget(self.apk_form)
        self.devices_form = DevicesWidget()
        dvc_h_box = QHBoxLayout(self.widget_devices)
        dvc_h_box.addWidget(self.devices_form)
        self.pushButton_install.clicked.connect(self.do_install)

    def do_install(self):
        ADBController.clear_select()
        l = self.devices_form.tableWidget_devices.selectedItems()
        for i in range(int(len(l)/2)):
            item = self.devices_form.tableWidget_devices.item(i, 0)
            print(item.text())
            ADBController.add_selected(item.text())
        if not ADBController.has_devices():
            msg = QMessageBox.warning(self, '警告', '未获取到设备', QMessageBox.Ok, QMessageBox.Ok)
        elif not ADBController.has_selected():
            msg = QMessageBox.warning(self, '警告', '未选取设备', QMessageBox.Ok, QMessageBox.Ok)
        elif not ADBController.has_apk():
            msg = QMessageBox.critical(self, '错误', '未获取到apk文件', QMessageBox.Ok, QMessageBox.Ok)
        else:
            ADBController.install_apk()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m_win = MainWindow()
    m_win.show()
    sys.exit(app.exec_())
