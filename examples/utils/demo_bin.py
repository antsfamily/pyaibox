#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-02-23 07:01:55
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$


import pyaibox as pb


datafile = 'data/data.bin'

x = [1, 3, 6, 111]
pb.savebin('./data.bin', x, dtype='i', endian='L', mode='o')

y = pb.loadbin('./data.bin', dbsize=4, dtype='i', endian='L')

print(y)

x = (1.3, 3.6)
pb.savebin('./data.bin', x, dtype='f', endian='B', offsets=16, mode='a')

y = pb.loadbin('./data.bin', dbsize=4, dtype='f', endian='B', offsets=16)

print(y)
