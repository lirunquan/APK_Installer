# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from resource.devices.ui_device_item import Ui_Device_Item_Form


class DeviceItemWidget(QWidget, Ui_Device_Item_Form):

    def __init__(self, item, serial, model, *args, **kwargs):
        super(DeviceItemWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.item = item
        self.label_serial.setText(serial)
        self.label_model.setText(model)

