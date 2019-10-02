# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :


class Device:
    def __init__(self, serial, model):
        self._serial = serial
        self._model = model

    def __str__(self):
        msg = self.serial + ' : ' + self.model
        return msg

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
