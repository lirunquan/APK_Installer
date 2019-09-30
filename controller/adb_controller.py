# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09-30.
# Copyright (c) 2019 3KWan.
# Description :
#
import os
from model.adb_model import ADBModel
from model.device_model import Device

adb = ADBModel()


class ADBController:

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(ADBModel, '_instance'):
            ADBController._instance = ADBController(*args, **kwargs)
        return ADBController._instance

    def get_devices(self):
        cmd = 'adb devices -l'
        ret = os.popen(cmd).readlines()
        for string in ret[1:-2]:
            string = string.split()
            serial = self.get_serial(string[0])
            brand = self.get_brand(string[-1])
            model = self.get_model(string[-2])
            device = Device(serial, brand, model)
            adb.add_device(device)

    @staticmethod
    def get_serial(string):
        return string.split(':')[-1]

    @staticmethod
    def get_brand(string):
        return string.split(':')[-1]

    @staticmethod
    def get_model(string):
        return string.split(':')[-1]

    @staticmethod
    def install_apk():
        apk = adb.apk_filename
        for device in adb.selected_devices:
            serial = device.serial
            cmd = 'adb -s %s install -r %s' % (serial, apk)
            ret = os.system(cmd)
            if ret:
                pass
