# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09-30.
# Copyright (c) 2019 3KWan.
# Description :
#
import os
import time
import re

from model.adb_model import ADBModel
from model.device_model import Device
from PyQt5.QtCore import QThread, pyqtSignal


adb = ADBModel()


class ADBController:

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get_devices():
        adb.clear_devices()
        cmd = 'adb devices -l'
        ret = os.popen(cmd).read()
        print(ret)
        serials = re.findall(r"\n(.+?)\s{2,}device", ret)
        models = re.findall(r"model:(.+?) ", ret)
        print(serials)
        print(models)
        for s, m in zip(serials, models):
            device = Device(s, m)
            adb.add_device(device)

    @staticmethod
    def add_apk(apk_name):
        adb.set_apk_file(apk_name)

    @staticmethod
    def add_selected(selected_serial):
        adb.add_selected(selected_serial)

    @staticmethod
    def clear_select():
        adb.clear_selected()

    @staticmethod
    def show_test():
        print(adb.selected_devices)

    @staticmethod
    def install_apk():
        for s in adb.selected_devices:
            t = Installing(s, adb.apk_filename)
            t.start()


class Installing(QThread):
    def __init__(self, serial, apk):
        super(Installing, self).__init__()
        self.serial = serial
        self.apk = apk

    def run(self) -> None:
        cmd = 'adb -s %s install -r %s' % (self.serial, self.apk)
        print(cmd)
        opt = os.system(cmd)
        print(opt)
