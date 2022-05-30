#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-15 10:34:16
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.1$

import numpy as np
import pyaibox as pb

X = np.random.randn(1, 3, 4, 2)
S = pb.entropy(X, caxis=-1, mode='shannon')
print(S)

X = X[:, :, :, 0] + 1j * X[:, :, :, 1]
S = pb.entropy(X, caxis=None, mode='shannon')
print(S)
