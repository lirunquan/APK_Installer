# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :

from controller.adb_controller import Installing

threads = []
for i in range(0, 10):
    thread = Installing('', '')
    threads.append(thread)
for t in threads:
    t.start()