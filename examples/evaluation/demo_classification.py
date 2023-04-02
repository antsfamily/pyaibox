#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : demo_classification.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Wed Dec 14 2022
# @version   : 0.0
# @license   : The GNU General Public License (GPL) v3.0
# @note      : 
# 
# The GNU General Public License (GPL) v3.0
# Copyright (C) 2013- Zhi Liu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

import numpy as np
import pyaibox as pb


T = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 5])
P = np.array([1, 2, 3, 4, 1, 6, 3, 2, 1, 4, 5, 6, 1, 2, 1, 4, 5, 6, 1, 5])
classnames = ['cat', 'dog', 'car', 'cup', 'desk', 'baby']

print(pb.accuracy(P, T))
# print(pb.categorical2onehot(T))

C = pb.confusion(P, T, cmpmode='...')
print(C)
C = pb.confusion(P, T, cmpmode='@')
print(C)
print(pb.kappa(C))
print(pb.kappa(C.T))

plt = pb.plot_confusion(C, xticks=classnames, yticks=classnames, cmap=None, mode='simple')
plt = pb.plot_confusion(C, xticks=classnames, yticks=classnames, cmap='summer', mode='simple')
plt.show()

plt = pb.plot_confusion(C, cmap=None, mode='rich')
plt = pb.plot_confusion(C, cmap='summer', mode='rich')
plt.show()
