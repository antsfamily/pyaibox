#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-15 10:34:16
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.1$

import numpy as np
from pyaibox import c2r, nextpow2, str2num


def dtypes(t='int'):
    if t in ['int', 'INT', 'Int']:
        return [np.int, np.int8, np.int16, np.int32, np.int64]
    if t in ['uint', 'UINT', 'UInt']:
        return [np.uint, np.uint8, np.uint16, np.uint32, np.uint64]
    if t in ['float', 'FLOAT', 'Float']:
        return [np.float, np.float16, np.float32, np.float64, np.float128]
    if t in ['complex', 'COMPLEX', 'Complex']:
        return [np.complex, np.complex64, np.complex128, np.complex256]


def peakvalue(A):
    r"""Compute the peak value of the input.

    Find peak value in matrix

    Parameters
    ----------
    A : numpy array
        Data for finding peak value

    Returns
    -------
    number
        Peak value.
    """

    if np.iscomplex(A).any():  # complex in complex
        A = c2r(A)

    dtype = A.dtype
    if dtype in dtypes('float'):
        maxv = np.max(A)
        Vpeak = 1 if maxv < 1 else 2**nextpow2(maxv) - 1
    elif dtype in dtypes('uint'):
        datatype = str(dtype)
        Vpeak = 2 ** (str2num(datatype, int)[0]) - 1
    elif dtype in dtypes('int'):
        datatype = str(dtype)
        Vpeak = 2 ** (str2num(datatype, int)[0]) / 2 - 1
    else:
        print("~~~Unknown type, using the maximum value!")
        Vpeak = np.max(A.abs())

    return Vpeak


if __name__ == '__main__':
    pass

