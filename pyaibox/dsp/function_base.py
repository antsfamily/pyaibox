#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : function_base.py
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
