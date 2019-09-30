# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09-30.
# Copyright (c) 2019 3KWan.
# Description :
#
import os

class ADBController:
    def __init__(self):
        pass
    def get_devices(self):
        cmd = 'adb devices -l'
        os.popen(cmd)

