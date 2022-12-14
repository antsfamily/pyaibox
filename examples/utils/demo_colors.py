#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-23 07:01:55
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import pyaibox as pb
import matplotlib.pyplot as plt
import numpy as np

cmap = 'jet'
# cmap = 'hsv'
# cmap = 'hot'
# cmap = 'parula'
gray = pb.imread('data/images/oi/LenaGRAY256.png')
print(gray.shape)

rgb = pb.gray2rgb(gray, cmap, [0, 1], False)  # rgb --> double, [0, 1]
rgb = pb.gray2rgb(gray, cmap, [0, 255], False)  # rgb --> double, [0., 255.]
# rgb = pb.gray2rgb(gray, cmap, [0, 255], 'uint8')  # rgb --> uint8, [0, 255]

print(gray.shape, np.min(gray), np.max(gray), gray.dtype)
print(rgb.shape, np.min(rgb), np.max(rgb), rgb.dtype)

plt.figure()
plt.subplot(121)
plt.imshow(gray, cmap=pb.parula if cmap == 'parula' else cmap)
plt.subplot(122)
plt.imshow(rgb)
plt.show()
