#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-23 07:01:55
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import numpy as np
import pyaibox as pb

n = -123456
bs = n.to_bytes(8, 'little', signed=True)
print(bs)
print(hex(n))
print(pb.bstr2int(bs, '<'))

print("===========================")
x = np.array([[251, 200, 210], [220, 5, 6]]).astype('uint8')
print('peak value:', pb.peakvalue(x))
x = np.array([[251, 200, 210], [220, 5, 6]]).astype('uint16')
print('peak value:', pb.peakvalue(x))
