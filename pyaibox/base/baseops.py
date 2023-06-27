#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : baseops.py
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

import copy


def redim(ndim, dim, cdim, keepcdim):
    r"""re-define dimensions

    Parameters
    ----------
    ndim : int
        the number of dimensions
    dim : int, tuple or list
        dimensions to be re-defined
    cdim : int, optional
        If data is complex-valued but represented as real tensors, 
        you should specify the dimension. Otherwise, set it to None, defaults is None.
        For example, :math:`{\bm X}_c\in {\mathbb C}^{N\times C\times H\times W}` is
        represented as a real-valued tensor :math:`{\bm X}_r\in {\mathbb R}^{N\times C\times H\times W\ times 2}`,
        then :attr:`cdim` equals to -1 or 4.
    keepcdim : bool
        If :obj:`True`, the complex dimension will be keeped. Only works when :attr:`X` is complex-valued tensor 
        but represents in real format. Default is :obj:`False`.

    Returns
    -------
    int, tuple or list
         re-defined dimensions
        
    """

    if (cdim is None) or (keepcdim):
        return dim
    if type(dim) is int:
        posdim = dim if dim >= 0 else ndim + dim
        poscdim = cdim if cdim >= 0 else ndim + cdim
        newdim = dim if poscdim > posdim else posdim - 1 if dim >= 0 else posdim - 1 - (ndim - 1)
        return newdim
    else:
        newdim = []
        poscdim = cdim if cdim >= 0 else ndim + cdim
        for d in dim:
            posdim = d if d >= 0 else ndim + d
            newdim.append(d if poscdim > posdim else posdim - 1)
        for i in range(len(dim)):
            if dim[i] < 0:
                newdim[i] -= (ndim - 1)
        return newdim

def upkeys(D, mode='-', k='module.'):
    r"""update keys of a dictionary

    Parameters
    ----------
    D : dict
        the input dictionary
    mode : str, optional
        ``'-'`` for remove key string which is specified by :attr:`k`, by default '-'
        ``'+'`` for add key string which is specified by :attr:`k`, by default '-'
    k : str, optional
        key string pattern, by default 'module.'

    Returns
    -------
    dict
        new dictionary with keys updated
    """

    X = {}
    for key, value in D.items():
        if mode == '-':
            newkey = key.replace(k, '')
        if mode == '+':
            newkey = k + key
        X[newkey] = value
    
    return X


def dreplace(d, fv=None, rv='None', new=False):
    fvtype = type(fv)
    if new:
        d = copy.deepcopy(d)
    for k, v in d.items():
        if type(v) is dict:
            dreplace(v, fv=fv, rv=rv)
        else:
            if type(v) == fvtype:
                if v == fv:
                    d[k] = rv
    return d


def dmka(D, Ds):
    """Multi-key value assign

    Multi-key value assign

    Parameters
    ----------
    D : dict
        main dict.
    Ds : dict
        sub dict
    """

    for k, v in Ds.items():
        D[k] = v
    return D


def strfind(mainstr, patnstr):
    """find all patterns in string

    Parameters
    ----------
    mainstr :  str
        the main string
    patnstr :  str
        the pattern string
    """
    
    pos = []
    i = 0
    idx = mainstr.find(patnstr)
    while idx > -1:
        pos.append(idx)
        idx = mainstr.find(patnstr, idx+1)

    return pos


if __name__ == '__main__':

    D = {'a': 1, 'b': 2, 'c': 3}
    Ds = {'b': 6}
    print(D)
    dmka(D, Ds)
    print(D)
    print(strfind('/*asdxxs*/3356/*', '/*'))