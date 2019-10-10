# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QTableView

from resource.devices.ui_devices import Ui_Devices_Form
from controller.adb_controller import ADBController
from model.adb_model import ADBModel


class DevicesWidget(QWidget, Ui_Devices_Form):
    def __init__(self):
        super(DevicesWidget, self).__init__()
        self.setupUi(self)
        self.data = ADBModel()
        self.tableWidget_devices.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_devices.horizontalHeader().setVisible(False)
        self.tableWidget_devices.setHorizontalHeaderLabels(['设备序列号', '设备品牌'])
        self.tableWidget_devices.setEditTriggers(QTableView.NoEditTriggers)
        self.load_devices()
        self.pushButton_refresh.clicked.connect(self.load_devices)
        self.checkBox_all.clicked.connect(self.select_all)

    def load_devices(self):
        self.tableWidget_devices.clear()
        ADBController.get_devices()
        count = len(self.data.device_list)
        self.tableWidget_devices.setRowCount(count)
        for i in range(count):
            device = self.data.device_list[i]
            item_s = QTableWidgetItem(str(device.serial))
            self.tableWidget_devices.setItem(i, 0, item_s)
            item_m = QTableWidgetItem(str(device.model))
            self.tableWidget_devices.setItem(i, 1, item_m)

    def select_all(self):
        state = self.checkBox_all.checkState()
        if state == Qt.Checked:
            self.tableWidget_devices.selectAll()
        elif state == Qt.Unchecked:
            self.tableWidget_devices.clearSelection()
