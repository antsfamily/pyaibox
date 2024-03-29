#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : mstar.py
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

import os
import struct
import numpy as np


def mstar_header(filepath):
    r"""read header information of mstar file

    Parameters
    ----------
    filepath : str
        the mstar file path string.

    Returns
    -------
    dict
        header information dictionary.

    Examples
    --------

    The following example shows how to read the header information.

    ::

        import pyaibox as pb

        datapath = pb.data_path('mstar')
        filepath = datapath + 'BTR70_HB03787.004'

        header = pb.mstar_header(filepath)
        for k, v in header.items():
            print(k, v)

    """

    f = open(filepath, 'rb')
    f.seek(1)
    header = {}
    version = f.readline().strip(b'\n').decode('utf-8')
    header['PhoenixHeaderVer'] = version[1+len('PhoenixHeaderVer'):-1]

    while True:
        data = f.readline().strip(b'\n').decode('utf-8')
        if data == '[EndofPhoenixHeader]':
            break
        if data:
            name, value = data.split('= ')
            header[name] = value
    f.close()

    return header


def mstar_raw(filepath, ofmt='c'):
    r"""load mstar raw data

    Each file is constructed with a prepended, variable-length, 
    Phoenix formatted (ASCII) header which contains detailed ground 
    truth and sensor information for the specific chip.  Following 
    the Phoenix header is the data block.  The data block is written 
    in Sun floating point format and is divided into two blocks, a 
    magnitude block followed by a phase block.  Byte swapping may be 
    required for certain host platforms.  Tools for reading and 
    manipulating the header information may be found at 
    https://www.sdms.afrl.af.mil .

    Parameters
    ----------
    filepath : str
        the data file path string.
    ofmt : str, optional
        output data type formation, ``'ap'`` for amplitude and angle,
        ``'c'`` for complex, and ``'r'`` for real and imaginary.

    Returns
    -------
    array
        the raw data with size :math:`{\mathbb C}^{H\times W}` (``'c'``), 
        :math:`{\mathbb R}^{H\times W \times 2}` (``'r'`` or ``'ap'``)

    Examples
    --------

    Read mstar raw amplitude-phase data and show in a figure.

    .. image:: ./_static/SHOW1_BTR70_HB03787.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import pyaibox as pb
        import matplotlib.pyplot as plt

        filepath = datapath + 'BTR70_HB03787.004'
        x = pb.mstar_raw(filepath, ofmt='ap')
        print(x.shape, np.max(x), np.min(x))

        plt.figure()
        plt.subplot(121)
        plt.imshow(x[..., 0])
        plt.title('amplitude')
        plt.subplot(122)
        plt.imshow(x[..., 1])
        plt.title('phase')
        plt.show()


    Read mstar raw complex-valued data and show in a figure.

    .. image:: ./_static/SHOW_BTR70_HB03787.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import pyaibox as pb
        import matplotlib.pyplot as plt

        filepath = datapath + 'BTR70_HB03787.004'
        x = pb.mstar_raw(filepath, ofmt='c')
        print(x.shape, np.max(x), np.min(x))

        plt.figure()
        plt.subplot(221)
        plt.imshow(x.real)
        plt.title('real part')
        plt.subplot(222)
        plt.imshow(x.imag)
        plt.title('imaginary part')
        plt.subplot(223)
        plt.imshow(np.abs(x))
        plt.title('amplitude')
        plt.subplot(224)
        plt.imshow(np.angle(x))
        plt.title('phase')
        plt.show()

    """

    f = open(filepath, 'rb')
    data = f.readline()
    data = f.readline()
    # PhoenixHeaderLength
    _, v = f.readline().strip(b'\n').decode('utf-8').split('= ')
    offsets = int(v)
    for k in range(9):
        f.readline()  # skip
    data, v = f.readline().strip(b'\n').decode('utf-8').split('= ')
    ncols = int(v)
    _, v = f.readline().strip(b'\n').decode('utf-8').split('= ')
    nrows = int(v)
    
    f.seek(offsets)
    # phase, angle
    x = struct.unpack_from('>%df' % (ncols*nrows*2), f.read(), 0)
    x = np.array(x).reshape(2, nrows, ncols)
    f.close()

    if ofmt in ['ap', 'amppha', 'AP', 'AMPPHA']:
        return np.transpose(x, (1, 2, 0))
    if ofmt in ['r', 'real', 'REAL']:
        return np.stack((x[0, ...] * np.cos(x[1, ...]), x[0, ...] * np.sin(x[1, ...])), axis=-1)
    if ofmt in ['c', 'cplx', 'complex', 'C', 'CPLX', 'COMPLEX']:
        return x[0, ...] * (np.cos(x[1, ...]) + 1j * np.sin(x[1, ...]))

# def read_mstar(rootdir, dataset='test', fmt='bin'):
#     pass


if __name__ == '__main__':

    import pyaibox as pb
    import matplotlib.pyplot as plt

    datapath = pb.data_path('mstar')
    filepath = datapath + 'BMP2_HB03787.000'
    filepath = datapath + 'BTR70_HB03787.004'
    # filepath = datapath + 'T72_HB03787.015'

    header = mstar_header(filepath)
    for k, v in header.items():
        print(k, v)

    x = mstar_raw(filepath, ofmt='ap')
    print(x.shape, np.max(x), np.min(x))

    plt.figure()
    plt.subplot(121)
    plt.imshow(x[..., 0])
    plt.title('amplitude')
    plt.subplot(122)
    plt.imshow(x[..., 1])
    plt.title('phase')
    plt.show()

    x = mstar_raw(filepath, ofmt='c')
    print(x.shape, np.max(x), np.min(x))

    plt.figure()
    plt.subplot(221)
    plt.imshow(x.real)
    plt.title('real part')
    plt.subplot(222)
    plt.imshow(x.imag)
    plt.title('imaginary part')
    plt.subplot(223)
    plt.imshow(np.abs(x))
    plt.title('amplitude')
    plt.subplot(224)
    plt.imshow(np.angle(x))
    plt.title('phase')
    plt.show()
