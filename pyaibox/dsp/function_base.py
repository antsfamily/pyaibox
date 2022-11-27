#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : function_base.py
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
import pyaibox as pb


def unwrap(x, discont=pb.PI, axis=-1):
    r"""Unwrap by changing deltas between values to :math:`2\pi` complement.

    Unwrap radian phase `x` by changing absoluted jumps greater than
    `discont` to their :math:`2\pi` complement along the given axis.

    Parameters
    ----------
    x : ndarray
        The input.
    discont : float, optional
        Maximum discontinuity between values, default is :math:`\pi`.
    axis : int, optional
        Axis along which unwrap will operate, default is the last axis.

    Returns
    -------
    ndarray
        The unwrapped.
    
    Examples
    --------

    ::

        x = np.array([3.14, -3.12, 3.12, 3.13, -3.11])
        y_np = unwrap(x)
        print(y_np, y_np.shape, type(y_np))

        # output

        tensor([3.1400, 3.1632, 3.1200, 3.1300, 3.1732], dtype=torch.float64) torch.Size([5]) <class 'torch.Tensor'>

    """

    if discont is None:
        discont = pb.PI

    return np.unwrap(x, discont=discont, axis=axis)


def unwrap2(x, discont=pb.PI, axis=-1):
    r"""Unwrap by changing deltas between values to :math:`2\pi` complement.

    Unwrap radian phase `x` by changing absoluted jumps greater than
    `discont` to their :math:`2\pi` complement along the given axis. The elements
    are divided into 2 parts (with equal length) along the given axis.
    The first part is unwrapped in inverse order, while the second part
    is unwrapped in normal order.

    Parameters
    ----------
    x : Tensor
        The input.
    discont : float, optional
        Maximum discontinuity between values, default is :math:`\pi`.
    axis : int, optional
        Axis along which unwrap will operate, default is the last axis.

    Returns
    -------
    Tensor
        The unwrapped.

    see :func:`unwrap`

    Examples
    --------

    ::

        x = np.array([3.14, -3.12, 3.12, 3.13, -3.11])
        y = unwrap(x)
        print(y, y.shape, type(y))

        print("------------------------")
        x = np.array([3.14, -3.12, 3.12, 3.13, -3.11])
        x = np.concatenate((x[::-1], x), axis=0)
        print(x)
        y = unwrap2(x)
        print(y, y.shape, type(y))

        # output
        [3.14       3.16318531 3.12       3.13       3.17318531] (5,) <class 'numpy.ndarray'>
        ------------------------
        [3.17318531 3.13       3.12       3.16318531 3.14       3.14
        3.16318531 3.12       3.13       3.17318531] (10,) <class 'numpy.ndarray'>
    
    """

    d = x.ndim
    s = x.shape[axis]
    i = int(s / 2)
    y1 = np.unwrap(x[pb.sl(d, [axis], [slice(0, i, 1)])][::-1], discont=discont, axis=axis)
    y2 = np.unwrap(x[pb.sl(d, [axis], [slice(i, s, 1)])], discont=discont, axis=axis)
    y = np.concatenate((y1[::-1], y2), axis=axis)
    return y


if __name__ == '__main__':

    x = np.array([3.14, -3.12, 3.12, 3.13, -3.11])
    y = unwrap(x)
    print(y, y.shape, type(y))

    print("------------------------")
    x = np.array([3.14, -3.12, 3.12, 3.13, -3.11])
    x = np.concatenate((x[::-1], x), axis=0)
    y = unwrap2(x)
    print(y, y.shape, type(y))
