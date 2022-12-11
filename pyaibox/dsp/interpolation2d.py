#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : interpolation2d.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Nov 11 2019
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
from scipy import interpolate
from pyaibox.utils.const import *


def interp2d(X, ratio=(2, 2), axis=(0, 1), method='cubic'):

    Hin, Win = X.shape[axis[0]], X.shape[axis[1]]
    Hout, Wout = int(Hin * ratio[0]), int(Win * ratio[1])
    yin, xin = np.mgrid[0:Hin:1, 0:Win:1]
    yout, xout = np.linspace(0, Hout, Hout), np.linspace(0, Wout, Wout)

    print(xin.shape, yin.shape)
    interpfunc = interpolate.interp2d(xin, yin, X, kind=method)

    return interpfunc(xout, yout)


if __name__ == '__main__':

    import pyaibox as pb
    import matplotlib.pyplot as plt

    X = pb.imread('../../data/fig/Lena.png')
    print(X.shape, X.min(), X.max())

    X = pb.dnsampling(X, ratio=(0.125, 0.125), axis=(0, 1), mod='uniform', method='throwaway')
    print(X.shape, X.min(), X.max())

    # X = pb.upsampling(X, (512, 512), axis=(0, 1), method='Lanczos')
    X = pb.interp2d(X, ratio=(2, 2), axis=(0, 1))
    plt.figure()
    plt.imshow(X)
    plt.show()
