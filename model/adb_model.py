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

    def clear_devices(self):
        self._device_list.clear()

    def add_device(self, device):
        if not isinstance(device, Device):
            raise ValueError('Not an instance of Device')
        else:
            self._device_list.append(device)

    def clear_selected(self):
        self._selected_devices.clear()

    def add_selected(self, device):
        self._selected_devices.append(device)

    def set_apk_file(self, name):
        self._apk_filename = name

    @property
    def device_list(self):
        return self._device_list

    @property
    def selected_devices(self):
        return self._selected_devices

    @property
    def apk_filename(self):
        return self._apk_filename

