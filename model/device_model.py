# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :


class Device:
    def __init__(self, serial, brand, model):
        self._serial = serial
        self._brand = brand
        self._model = model

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
