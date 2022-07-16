#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-23 07:01:55
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import numpy as np
import pyaibox as pb


datafolder = pb.data_path('optical')
xr = pb.imread(datafolder + 'Einstein256.png')
xi = pb.imread(datafolder + 'LenaGRAY256.png')

x = xr + 1j * xi

y = pb.ct2rt(x, axis=0)
z = pb.rt2ct(y, axis=0)

print(x.shape, y.shape, z.shape)
print(x.dtype, y.dtype, z.dtype)

print(np.min(np.abs(x)), np.max(np.abs(x)))
print(np.min(np.abs(y)), np.max(np.abs(y)))
print(np.min(np.abs(z)), np.max(np.abs(z)))


plt = pb.imshow([x.real, x.imag, y.real, y.imag, z.real, z.imag], nrows=3, ncols=2,
                titles=['original(real)', 'original(imag)', 'converted(real)', 
                'converted(imag)', 'reconstructed(real)', 'reconstructed(imag)'])
plt.show()
