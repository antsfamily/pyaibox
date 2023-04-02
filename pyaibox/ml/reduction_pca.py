#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : dataset_visualization.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Dec 18 2022
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
# You should have received a copy of the GNU General Public License along with XXXXXX. 
# If not, see <https://www.gnu.org/licenses/>. 
#

import numpy as np
from pyaibox.utils.convert import str2num


def pca(x, axisn=0, ncmpnts='auto99%', algo='svd'):
    r"""Principal Component Analysis (pca) on raw data

    Parameters
    ----------
    x : array
        the input data
    axisn : int, optional
        the axis of number of samples, by default 0
    ncmpnts : int or str, optional
        the number of components, by default ``'auto99%'``
    algo : str, optional
        the kind of algorithms, by default ``'svd'``

    Returns
    -------
    array
        U, S, K (if :attr:`ncmpnts` is integer)

    Examples
    --------

    .. image:: ./_static/MNISTPCA_ORIG.png
       :scale: 100 %
       :align: center

    .. image:: ./_static/MNISTPCA_K70.png
       :scale: 100 %
       :align: center

    .. image:: ./_static/MNISTPCA_K90.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import numpy as np
        import pyaibox as pb

        rootdir, dataset = '/mnt/d/DataSets/oi/dgi/mnist/official/', 'test'
        x, _ = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
        print(x.shape)
        N, M2, _ = x.shape

        u, s, k = pb.pca(x, axisn=0, ncmpnts='auto90%', algo='svd')
        print(u.shape, s.shape, k)
        u = u[:, :k]
        y = x.reshape(N, -1) @ u  # N-k
        z = y @ u.T.conj()
        z = z.reshape(N, M2, M2)
        print(pb.nmse(x, z, axis=(1, 2)))
        xp = np.pad(x[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
        zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
        plt = pb.imshow(pb.patch2tensor(xp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Orignal'])
        plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(90%)'])

        u, s, k = pb.pca(x, axisn=0, ncmpnts='auto0.7', algo='svd')
        print(u.shape, s.shape, k)
        u = u[:, :k]
        y = x.reshape(N, -1) @ u  # N-k
        z = y @ u.T.conj()
        z = z.reshape(N, M2, M2)
        print(pb.nmse(x, z, axis=(1, 2)))
        zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
        plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(70%)'])
        plt.show()

        u, s = pb.pca(x, axisn=0, ncmpnts=2, algo='svd')
        print(u.shape, s.shape)
        y = x.reshape(N, -1) @ u  # N-k
        z = y @ u.T.conj()
        z = z.reshape(N, M2, M2)
        print(pb.nmse(x, z, axis=(1, 2)))

    """

    xshape = x.shape
    N = xshape[axisn]
    if axisn != 0:
        x = x.transpose(0, axisn)
    x = np.reshape(x, (N, -1))
    N, M = x.shape

    x = x - np.mean(x, axis=1, keepdims=True)
    sigma = x.T.conj() @ x / M  # M-M

    if algo.lower() in ['svd']:
        [U, S, V] = np.linalg.svd(sigma)

    if type(ncmpnts) is int:
        return U[:, :ncmpnts], S[:ncmpnts]

    if ncmpnts.lower() in ['all']:
        return U, S

    if 'auto' in ncmpnts.lower():
        pct = str2num(ncmpnts, vfn=float)[0] / 100 if '%' in ncmpnts else str2num(ncmpnts, vfn=float)[0]
        lambd = np.abs(S)
        lambd_sum = np.sum(lambd)
        lambd_sumk, pctk = 0, 0
        K = 0
        for k in range(M):
            lambd_sumk += lambd[k]
            pctk = lambd_sumk / lambd_sum
            if pctk >= pct:
                K = k + 1
                break

        return U, S, K


if __name__ == '__main__':

    import pyaibox as pb

    x = np.array([[1, 2, 3, 4], [1, 1, 1, 1], [2.0, 2, 2, 2], [1, 2, 3, 4], [3, 3, 6, 6], [1, 1, 1, 1]])
    u, s = pca(x, axisn=0, ncmpnts='all', algo='svd')
    print(u, s)

    x = np.random.randn(1000, 32, 32)

    rootdir, dataset = '/mnt/d/DataSets/oi/dgi/mnist/official/', 'test'
    x, _ = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
    print(x.shape)
    N, M2, _ = x.shape

    u, s, k = pca(x, axisn=0, ncmpnts='auto90%', algo='svd')
    print(u.shape, s.shape, k)
    u = u[:, :k]
    y = x.reshape(N, -1) @ u  # N-k
    z = y @ u.T.conj()
    z = z.reshape(N, M2, M2)
    print(pb.nmse(x, z, axis=(1, 2)))
    xp = np.pad(x[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
    zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
    plt = pb.imshow(pb.patch2tensor(xp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Orignal'])
    plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(90%)'])

    u, s, k = pca(x, axisn=0, ncmpnts='auto0.7', algo='svd')
    print(u.shape, s.shape, k)
    u = u[:, :k]
    y = x.reshape(N, -1) @ u  # N-k
    z = y @ u.T.conj()
    z = z.reshape(N, M2, M2)
    print(pb.nmse(x, z, axis=(1, 2)))
    zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
    plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(70%)'])
    plt.show()

    u, s = pca(x, axisn=0, ncmpnts=2, algo='svd')
    print(u.shape, s.shape)
    y = x.reshape(N, -1) @ u  # N-k
    z = y @ u.T.conj()
    z = z.reshape(N, M2, M2)
    print(pb.nmse(x, z, axis=(1, 2)))
