#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : entropy.py
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
from pyaibox.utils.const import EPS


def entropy(X, caxis=None, axis=None, mode='shannon', reduction='mean'):
    r"""compute the entropy of the inputs

    .. math::
        {\rm ENT} = -\sum_{n=0}^N p_i{\rm log}_2 p_n

    where :math:`N` is the number of pixels, :math:`p_n=\frac{|X_n|^2}{\sum_{n=0}^N|X_n|^2}`.

    Parameters
    ----------
    X : numpy array
        The complex or real inputs, for complex inputs, both complex and real representations are surpported.
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`caxis` is ignored. If :attr:`X` is real-valued and :attr:`caxis` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`caxis` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued
    axis : int or None
        The dimension axis (:attr:`caxis` is not included) for computing entropy. The default is :obj:`None`, which means all. 
    mode : str, optional
        The entropy mode: ``'shannon'`` or ``'natural'`` (the default is 'shannon')
    reduction : str, optional
        The operation in batch dim, :obj:`None`, ``'mean'`` or ``'sum'`` (the default is ``'mean'``)

    Returns
    -------
    S : scalar or numpy array
        The entropy of the inputs.

    Examples
    ---------

    ::

        np.random.seed(2020)
        X = np.random.randn(5, 2, 3, 4)

        # real
        S1 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction=None)
        S2 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='sum')
        S3 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='mean')
        print(S1, S2, S3)

        # complex in real format
        S1 = entropy(X, caxis=1, axis=(-2, -1), mode='shannon', reduction=None)
        S2 = entropy(X, caxis=1, axis=(-2, -1), mode='shannon', reduction='sum')
        S3 = entropy(X, caxis=1, axis=(-2, -1), mode='shannon', reduction='mean')
        print(S1, S2, S3)

        # complex in complex format
        X = X[:, 0, ...] + 1j * X[:, 1, ...]
        S1 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction=None)
        S2 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='sum')
        S3 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='mean')
        print(S1, S2, S3)

        # ---output
        [[2.76482544 2.38657794]
        [2.85232291 2.33204624]
        [2.26890769 2.4308547 ]
        [2.50283407 2.56037192]
        [2.76608007 2.47020486]] 25.33502585795305 2.533502585795305
        [3.03089227 2.84108823 2.93389666 3.00868855 2.8229912 ] 14.637556915006513 2.9275113830013026
        [3.03089227 2.84108823 2.93389666 3.00868855 2.8229912 ] 14.637556915006513 2.9275113830013026

    """

    if mode in ['Shannon', 'shannon', 'SHANNON']:
        logfunc = np.log2
    if mode in ['Natural', 'natural', 'NATURAL']:
        logfunc = np.log

    if np.iscomplex(X).any():  # complex in complex
        X = X.real*X.real + X.imag*X.imag
    else:
        if caxis is None:  # real
            X = X**2
        else:  # complex in real
            X = np.sum(X**2, axis=caxis)

    P = np.sum(X, axis, keepdims=True)
    p = X / (P + EPS)
    S = -np.sum(p * logfunc(p + EPS), axis)
    if reduction in ['mean', 'MEAN']:
        S = np.mean(S)
    if reduction in ['sum', 'SUM']:
        S = np.sum(S)

    return S


if __name__ == '__main__':

    np.random.seed(2020)
    X = np.random.randn(5, 2, 3, 4)

    # real
    S1 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction=None)
    S2 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='sum')
    S3 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='mean')
    print(S1, S2, S3)

    # complex in real format
    S1 = entropy(X, caxis=1, axis=(-2, -1), mode='shannon', reduction=None)
    S2 = entropy(X, caxis=1, axis=(-2, -1), mode='shannon', reduction='sum')
    S3 = entropy(X, caxis=1, axis=(-2, -1), mode='shannon', reduction='mean')
    print(S1, S2, S3)

    # complex in complex format
    X = X[:, 0, ...] + 1j * X[:, 1, ...]
    S1 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction=None)
    S2 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='sum')
    S3 = entropy(X, caxis=None, axis=(-2, -1), mode='shannon', reduction='mean')
    print(S1, S2, S3)
