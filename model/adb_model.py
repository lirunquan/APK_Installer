# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :

from model.device_model import Device


class ADBModel(object):
    __instance = None

    def __init__(self, *args, **kwargs):
        self._device_list = []
        self._apk_filename = ''
        self._selected_devices = []

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def add_device(self, device):
        if not isinstance(device, Device):
            raise ValueError('Not an instance of Device')
        else:
            self._device_list.append(device)

    def add_selected(self, device):
        if not isinstance(device, Device):
            raise ValueError('Not an instance of Device')
        else:
            self._selected_devices.append(device)

    @property
    def device_list(self):
        return self._device_list

    @property
    def selected_devices(self):
        return self._selected_devices

    @property
    def apk_filename(self):
        return self._apk_filename

    @apk_filename.setter
    def apk_filename(self, name):
        if not isinstance(name, str):
            raise ValueError('apk filename needs to be an str, please check your apk file.')
        elif not name.endswith('.apk'):
            raise ValueError('\'' + name + '\' is not a normal apk file')
        else:
            self._apk_filename = name

    @selected_devices.setter
    def selected_devices(self, value):
        self._selected_devices = value

