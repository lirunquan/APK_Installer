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

# adb = ADBModel()


class ADBController:

    def __init__(self, *args, **kwargs):
        self.adb = ADBModel()

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(ADBModel, '_instance'):
            ADBController._instance = ADBController(*args, **kwargs)
        return ADBController._instance

    def get_devices(self):
        cmd = 'adb devices -l'
        ret = os.popen(cmd).read()
        print(ret)
        serials = re.findall(r"\n(.+?)\s{2,}device", ret)
        models = re.findall(r"model:(.+?) ", ret)
        print(serials)
        print(models)
        for s, m in zip(serials, models):
            device = Device(s, m)
            self.adb.add_device(device)

    # @staticmethod
    # def install_apk():
    #     apk = adb.apk_filename
    #     for device in adb.selected_devices:
    #         serial = device.serial
    #         cmd = 'adb -s %s install -r %s' % (serial, apk)
    #         ret = os.system(cmd)
    #         if ret:
    #             pass


class Installing(QThread):
    ret = pyqtSignal(str)

    def __init__(self, obj, serial, apk):
        super(Installing, self).__init__(obj)
        self.serial = serial
        self.apk = apk

    def run(self) -> None:
        cmd = 'adb -s %s install -r %s' % (self.serial, self.apk)
        opt = os.system(cmd)
        self.ret.emit(str(opt))
        time.sleep(1)
