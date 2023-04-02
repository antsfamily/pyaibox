#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : demo_mnist_pca.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Dec 18 2022
# @version   : 0.0
# @license   : The GNU General Public License (GPL) v3.0
# @note      : 
# 
# The GNU General Public License (GPL) v3.0
# Copyright (C) 2013- Zhi Liu
#
# This file is part of pyaibox.
#
# pyaibox is free software: you can redistribute it and/or modify it under the 
# terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
#
# pyaibox is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with pyaibox. 
# If not, see <https://www.gnu.org/licenses/>. 
#

import numpy as np
import pyaibox as pb

rootdir, dataset = '/mnt/d/DataSets/oi/dgi/mnist/official/', 'test'
x, _ = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
print(x.shape)
N, M2, _ = x.shape

u, s, k = pb.pca(x, axisn=0, ncmpnts='auto90%', algo='svd')
print(u.shape, s.shape, k)
u = u[:, :k]
y = x.reshape(N, -1) @ u  # N-k
z = y @ u.T.conj()
z = z.reshape(N, M2, M2)
print(pb.nmse(x, z, axis=(1, 2)))
xp = np.pad(x[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
plt = pb.imshow(pb.patch2tensor(xp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Orignal'])
plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(90%)'])

u, s, k = pb.pca(x, axisn=0, ncmpnts='auto0.7', algo='svd')
print(u.shape, s.shape, k)
u = u[:, :k]
y = x.reshape(N, -1) @ u  # N-k
z = y @ u.T.conj()
z = z.reshape(N, M2, M2)
print(pb.nmse(x, z, axis=(1, 2)))
zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(70%)'])
plt.show()

u, s = pb.pca(x, axisn=0, ncmpnts=2, algo='svd')
print(u.shape, s.shape)
y = x.reshape(N, -1) @ u  # N-k
z = y @ u.T.conj()
z = z.reshape(N, M2, M2)
print(pb.nmse(x, z, axis=(1, 2)))
