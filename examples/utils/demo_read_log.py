#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-05-13 07:01:55
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import pyaibox as pb


logma = 'data/files/log/matlab_lenet_gpu.log'
logpy = 'data/files/log/python_lenet_gpu.log'
logjl = 'data/files/log/julia_lenet_gpu.log'


x = pb.readcsv(logma, sep='|', vfn=None, nlines=100)
print(x, len(x))

x = pb.readsec(logma, pmain='|', psub='', vfn=float, nshots=100)
print(x, len(x))

x = pb.readnum(logpy, pmain='Train', psub='time: ', vfn=float, nshots=100)
print(x, len(x))

x = pb.readnum(logjl, pmain='Train', psub='time: ', vfn=float, nshots=100)
print(x, len(x))


