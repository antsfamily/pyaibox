#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 16:36:03
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$
from __future__ import division, print_function, absolute_import
import copy


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


if __name__ == '__main__':

    D = {'a': 1, 'b': 2, 'c': 3}
    Ds = {'b': 6}
    print(D)
    dmka(D, Ds)
    print(D)
