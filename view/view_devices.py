# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from resource.devices.ui_devices import Ui_Devices_Form
from view.view_device_item import DeviceItemWidget
from controller.adb_controller import ADBController
from model.adb_model import ADBModel


class DevicesWidget(QWidget, Ui_Devices_Form):
    def __init__(self):
        super(DevicesWidget, self).__init__()
        self.setupUi(self)
        self.data = ADBModel()
        self.load_devices()
        self.pushButton_refresh.clicked.connect(self.load_devices)

    def load_devices(self):
        self.listWidget_devices.clear()
        ADBController.get_devices()
        for device in self.data.device_list:
            print(device)
            item = QListWidgetItem(self.listWidget_devices)
            item.setSizeHint(QSize(0, 20))
            widget = DeviceItemWidget(item, device.serial, device.model)
            self.listWidget_devices.setItemWidget(item, widget)
