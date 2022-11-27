#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : interpolation2d.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Nov 11 2019
# @version   : 0.0
# @license   : The Apache License 2.0
# @note      : 
# 
# The Apache 2.0 License
# Copyright (C) 2013- Zhi Liu
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
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
