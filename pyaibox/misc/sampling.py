#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : sampling.py
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
from pyaibox.base.arrayops import sl, cat
from pyaibox.base.randomfunc import setseed, randgrid, randperm
from pyaibox.base.arrayops import arraycomb
from pyaibox.utils.ios import loadmat, loadh5


# def upsampling(X, shape, axis=-1, method='Lanczos'):

#     # Na, Nr = X.shape
#     # Y = np.zeros(shape, dtype=X.dtype)
#     # for a in range(Na):
#     #     Y[a, :] = np.interp(range(shape[1]), range(Nr), X[a, :])
#     # for r in range(Nr):
#     #     Y[:, a] = np.interp(range(shape[0]), range(Na), X[:, r])

#     # return Y

#     print(shape, X.shape)
#     imgXr = Image.fromarray(X[:, :, 0])
#     # imgXr = imgXr.resize((shape[1], shape[0]), Image.LANCZOS)
#     # imgXr = imgXr.resize((shape[1], shape[0]), Image.BILINEAR)
#     imgXr = imgXr.resize((shape[1], shape[0]), Image.NEAREST)
#     # imgXr = imgXr.resize((shape[1], shape[0]), Image.ANTIALIAS)
#     imgXi = Image.fromarray(X[:, :, 1])
#     # imgXi = imgXi.resize((shape[1], shape[0]), Image.LANCZOS)
#     # imgXi = imgXi.resize((shape[1], shape[0]), Image.BILINEAR)
#     imgXi = imgXi.resize((shape[1], shape[0]), Image.NEAREST)
#     # imgXi = imgXi.resize((shape[1], shape[0]), Image.ANTIALIAS)
#     return np.transpose(np.array([np.array(imgXr), np.array(imgXi)]), (1, 2, 0))


def slidegrid(start, stop, step, shake=0, n=None):
    r"""generates sliding grid indexes

    Generates :attr:`n` sliding grid indexes from :attr:`start` to :attr:`stop`
    with step size :attr:`step`.

    Args:
        start (int or list): start sampling point
        stop (int or list): stop sampling point
        step (int or list): sampling stepsize
        shake (float): the shake rate, if :attr:`shake` is 0, no shake, (default),
            if positive, add a positive shake, if negative, add a negative.
        n (int or None): the number of samples (default None, int((stop0 - start0) / step0) * int((stop1 - start1) / step1)...).

    Returns:
        for multi-dimension, return a 2-d tensor, for 1-dimension, return a 1d-tensor.

    Raises:
        TypeError: The number of samples should be an integer or None.

    see :func:`randperm`, :func:`randgrid`.

    """

    starts = [start] if type(start) is int else start
    stops = [stop] if type(stop) is int else stop
    steps = [step] if type(step) is int else step
    shakes = [shake] if type(shake) is int or type(shake) is float else shake
    if (n is not None) and (type(n) is not int):
        raise TypeError('The number of samples should be an integer or None!')
    elif n is None:
        n = float('inf')
    index = []
    for start, stop, step, shake in zip(starts, stops, steps, shakes):
        shakep = shake if abs(shake) >= 1 and type(shake) is int else int(shake * step)
        x = np.array(range(start, stop, step))
        if shakep != 0:
            s = np.random.randint(0, abs(shakep), len(x))
            x = x - s if shakep < 0 else x + s
            x[x >= (stop - step)] = stop - step
            x[x < start] = start
        index.append(x)
    P = arraycomb(index)
    n = min(P.shape[0], n)
    P = P[:n, ...]

    if len(starts) == 1:
        P = P.squeeze(1)
        return P
    else:
        return P.transpose()


def dnsampling(x, ratio=1., axis=-1, smode='uniform', omode='discard', seed=None, extra=False):
    r"""down-sampling a tensor

    Args:
        x (ndarray): The input tensor.
        ratio (float, optional): Downsampling ratio.
        axis (int, optional): Downsampling axis (default -1).
        smode (str, optional): Downsampling mode: ``'uniform'``, ``'random'``, ``'random2'``.
        omode (str, optional): output mode: ``'discard'`` for discarding, ``'zero'`` for zero filling.
        seed (int or None, optional): seed for numpy's random.
        extra (bool, optional): If ``True``, also return sampling mask.

    Returns:
        (ndarray): Description

    Raises:
        TypeError: :attr:`axis`
        ValueError: :attr:`ratio`, attr:`smode`, attr:`omode`
    """

    nDims = np.ndim(x)
    if type(axis) is int:
        if type(ratio) is not float:
            raise ValueError('Downsampling ratio should be a number!')
        axis = [axis]
        ratio = [ratio]
    elif type(axis) is list or tuple:
        if len(axis) != len(ratio):
            raise ValueError('You should specify the DS ratio for each axis!')
    else:
        raise TypeError('Wrong type of axis!')

    axis, ratio = list(axis), list(ratio)
    for cnt in range(len(axis)):
        if axis[cnt] < 0:
            axis[cnt] += nDims
        # ratio[cnt] = 1. - ratio[cnt]
        cnt += 1

    if omode in ['discard', 'DISCARD', 'Discard']:
        if smode not in ['uniform', 'UNIFORM', 'Uniform']:
            raise ValueError("Only support uniform mode!")

        index = [slice(None)] * nDims
        for a, r in zip(axis, ratio):
            sa = x.shape[a]
            da = int(round(1. / r))
            index[a] = slice(0, sa, da)
        index = tuple(index)

        if extra:
            return x[index], index
        else:
            return x[index]

    elif omode in ['zero', 'ZERO', 'Zeros']:
        mshape = [1] * nDims
        for a in axis:
            mshape[a] = x.shape[a]
        mask = np.zeros(mshape, dtype=np.uint8)
        if smode in ['uniform', 'UNIFORM', 'Uniform']:
            for a, r in zip(axis, ratio):
                sa = x.shape[a]
                da = int(round(1. / r))
                idx = sl(nDims, a, slice(0, sa, da))
                mask[idx] += 1
            mask[mask < len(axis)] = 0
            mask[mask >= len(axis)] = 1

        elif smode in ['random', 'RANDOM', 'Random']:
            setseed(seed, target='numpy')
            for a, r in zip(axis, ratio):
                d = np.ndim(x)
                s = x.shape[a]
                n = int(round(s * r))
                idx = randperm(0, s, n)
                idx = np.sort(idx)
                idx = sl(d, a, idx)
                mask[idx] += 1
            mask[mask < len(axis)] = 0
            mask[mask >= len(axis)] = 1

        elif smode in ['random2', 'RANDOM2', 'Random2']:
            setseed(seed, target='numpy')
            d = np.ndim(x)
            s0, s1 = x.shape[axis[0]], x.shape[axis[1]]
            n0, n1 = int(round(s0 * ratio[0])), int(round(s1 * ratio[0]))
            idx0 = randperm(0, s0, n0)
            # idx0 = np.sort(idx0)

            for i0 in idx0:
                idx1 = randperm(0, s1, n1)
                mask[sl(d, [axis[0], axis[1]], [[i0], idx1])] = 1

        else:
            raise ValueError('Not supported sampling mode: %s!' % smode)

        if extra:
            return x * mask, mask
        else:
            return x * mask

    else:
        raise ValueError('Not supported output mode: %s!' % omode)


def sample_tensor(x, n, axis=0, groups=1, mode='sequentially', seed=None, extra=False):
    r"""sample a tensor

    Sample a tensor sequentially/uniformly/randomly.

    Args:
        x (ndarray): a numpy or torch tensor to be sampled
        n (int): sample number
        axis (int, optional): the axis to be sampled (the default is 0)
        groups (int, optional): number of groups in this tensor (the default is 1)
        mode (str, optional): - ``'sequentially'``: evenly spaced (default)
            - ``'uniformly'``: [0, int(n/groups)]
            - ``'randomly'``: randomly selected, non-returned sampling
        seed (None or int, optional): only work for ``'randomly'`` mode (the default is None)
        extra (bool, optional): If ``True``, also return the selected indexes, the default is ``False``.

    Returns:
        y (ndarray): Sampled numpy or torch tensor.
        idx (list): Sampled indexes, if :attr:`extra` is ``True``, this will also be returned.


    Example:

        ::

            setseed(2020, 'numpy')

            x = np.randint(1000, (20, 3, 4))
            y1, idx1 = sample_tensor(x, 10, axis=0, groups=2, mode='sequentially', extra=True)
            y2, idx2 = sample_tensor(x, 10, axis=0, groups=2, mode='uniformly', extra=True)
            y3, idx3 = sample_tensor(x, 10, axis=0, groups=2, mode='randomly', extra=True)

            print(x.shape)
            print(y1.shape)
            print(y2.shape)
            print(y3.shape)
            print(idx1)
            print(idx2)
            print(idx3)

            the outputs are as follows:

            torch.Size([20, 3, 4])
            torch.Size([10, 3, 4])
            torch.Size([10, 3, 4])
            torch.Size([10, 3, 4])
            [0, 1, 2, 3, 4, 10, 11, 12, 13, 14]
            [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
            [3, 1, 5, 8, 7, 17, 18, 13, 16, 10]


    Raises:
        ValueError: The tensor does not has enough samples.


    """

    N = x.shape[axis]
    M = int(N / groups)  # each group has M samples
    m = int(n / groups)  # each group has m sampled samples

    if (M < m):
        raise ValueError('The ndarray does not has enough samples')

    idx = []
    if mode in ['sequentially', 'Sequentially']:
        for g in range(groups):
            idx += list(range(int(M * g), int(M * g) + m))
    if mode in ['uniformly', 'Uniformly']:
        for g in range(groups):
            idx += list(range(int(M * g), int(M * g + M), int(M / m)))[:m]
    if mode in ['randomly', 'Randomly']:
        setseed(seed, target='numpy')
        for g in range(groups):
            idx += list(randperm(int(M * g), int(M * g + M), m))

    if extra:
        return x[sl(np.ndim(x), axis=axis, idx=[idx])], idx
    else:
        return x[sl(np.ndim(x), axis=axis, idx=[idx])]


def shuffle_tensor(x, axis=0, groups=1, mode='inter', seed=None, extra=False):
    r"""shuffle a tensor

    Shuffle a tensor randomly.

    Args:
        x (ndarray): A numpy or torch tensor to be shuffled.
        axis (int, optional): The axis to be shuffled (default 0)
        groups (number, optional): The number of groups in this tensor (default 1)
        mode (str, optional):
            - ``'inter'``: between groups (default)
            - ``'intra'``: within group
            - ``'whole'``: the whole
        seed (None or number, optional): random seed (the default is None)
        extra (bool, optional): If ``True``, also returns the shuffle indexes, the default is ``False``.

    Returns:
        y (ndarray): Shuffled numpy or torch tensor.
        idx (list): Shuffled indexes, if :attr:`extra` is ``True``, this will also be returned.


    Example:

        Shuffle a tensor randomly with different modes (``'intra'``, ``'inter'``, ``'whole'``).

        ::

            setseed(2020, 'numpy')

            x = np.randint(1000, (20, 3, 4))
            y1, idx1 = shuffle_tensor(x, axis=0, groups=4, mode='intra', extra=True)
            y2, idx2 = shuffle_tensor(x, axis=0, groups=4, mode='inter', extra=True)
            y3, idx3 = shuffle_tensor(x, axis=0, groups=4, mode='whole', extra=True)

            print(x.shape)
            print(y1.shape)
            print(y2.shape)
            print(y3.shape)
            print(idx1)
            print(idx2)
            print(idx3)

            the outputs are as follows:

            torch.Size([20, 3, 4])
            torch.Size([20, 3, 4])
            torch.Size([20, 3, 4])
            torch.Size([20, 3, 4])
            [1, 0, 3, 4, 2, 8, 6, 5, 9, 7, 13, 11, 12, 14, 10, 18, 15, 17, 16, 19]
            [0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19]
            [1, 13, 12, 5, 19, 9, 11, 6, 4, 16, 17, 3, 8, 18, 7, 10, 15, 0, 14, 2]


    """

    N = x.shape[axis]
    M = int(N / groups)  # each group has M samples

    idx = []
    setseed(seed, target='numpy')
    if mode in ['whole', 'Whole', 'WHOLE']:
        idx = list(randperm(0, N, N))

    if mode in ['intra', 'Intra', 'INTRA']:
        for g in range(groups):
            idx += list(randperm(int(M * g), int(M * g + M), M))
    if mode in ['inter', 'Inter', 'INTER']:
        for g in range(groups):
            idx += [list(range(int(M * g), int(M * g + M)))]
        groupidx = list(randperm(0, groups, groups))

        iidx = idx.copy()
        idx = []
        for i in groupidx:
            idx += iidx[i]

    if extra:
        return x[sl(np.ndim(x), axis=axis, idx=[idx])], idx
    else:
        return x[sl(np.ndim(x), axis=axis, idx=[idx])]


def split_tensor(x, ratios=[0.7, 0.2, 0.1], axis=0, shuffle=False, seed=None, extra=False):
    r"""split a tensor

    split a tensor into some parts.

    Args:
        x (ndarray): A numpy array or torch tensor.
        ratios (list, optional): Split ratios (the default is [0.7, 0.2, 0.05])
        axis (int, optional): Split axis (the default is 0)
        shuffle (bool, optional): Whether shuffle (the default is False)
        seed (int, optional): Shuffule seed (the default is None)
        extra (bool, optional): If ``True``, also return the split indexes, the default is ``False``.

    Returns:
        (list of ndarray): Splitted ndarrays.
    """

    y, idxes = [], []

    N, ns = x.shape[axis], 0
    if shuffle:
        setseed(seed, target='numpy')
        idx = randperm(0, N, N)
    else:
        idx = list(range(N))

    for ratio in ratios:
        n = int(ratio * N)
        idxes.append(idx[ns:ns + n])
        y.append(x[idx[ns:ns + n]])
        ns += n

    if extra:
        return y, idxes
    else:
        return y


def tensor2patch(x, n=None, size=(256, 256), axis=(0, 1), start=(0, 0), stop=(None, None), step=(1, 1), shake=(0, 0), mode='slidegrid', seed=None):
    r"""sample patch from a tensor

    Sample some patches from a tensor, tensor and patch can be any size.

    Args:
        x (ndarray): A tensor to be sampled.
        n (int, optional): The number of pactches, the default is None, auto computed,
            equals to the number of blocks with specified :attr:`step`
        size (tuple or int, optional): The size of patch (the default is (256, 256))
        axis (tuple or int, optional): The sampling axis (the default is (0, 1))
        start (tuple or int, optional): Start sampling index for each axis (the default is (0, 0))
        stop (tuple or int, optional): Stopp sampling index for each axis. (the default is (None, None), which [default_description])
        step (tuple or int, optional): Sampling stepsize for each axis  (the default is (1, 1), which [default_description])
        shake (tuple or int or float, optional): float for shake rate, int for shake points (the default is (0, 0), which means no shake)
        mode (str, optional): Sampling mode, ``'slidegrid'``, ``'randgrid'``, ``'randperm'`` (the default is 'slidegrid')
        seed (int, optional): Random seed. (the default is None, which means no seed.)

    Returns:
        (ndarray): A tensor of sampled patches.
    
    see :func:`patch2tensor`.

    Example:

        Sample patches from a tensor with different mode (randperm, randgrid, slidegrid), 
        and then reform these patches into an image.

        .. image:: ./_static/demo_sample_patch.png
           :scale: 100 %
           :align: center

        The results shown in the above figure can be obtained by the following codes.

        ::

            import math
            import numpy as np
            import pyaibox as pl
            import matplotlib.pyplot as plt

            filename = '../../data/images/Lotus512.png'
            filename = '../../data/images/LenaRGB512.tif'

            x = pb.imread(filename)
            xshape = x.shape
            xshape = xshape[:2]

            n, size = 64, (64, 64)

            y1 = pb.tensor2patch(x, n=n, size=size, axis=(0, 1), step=(1, 1), shake=(0, 0), mode='randperm', seed=2020)
            y2 = pb.tensor2patch(x, n=n, size=size, axis=(0, 1), step=(64, 64), shake=(0, 0), mode='randgrid', seed=2020)
            y3 = pb.tensor2patch(x, n=n, size=size, axis=(0, 1), step=(64, 64), shake=(0, 0), mode='slidegrid', seed=2020)
            y4 = pb.tensor2patch(x, n=n, size=size, axis=(0, 1), step=(64, 64), shake=(32, 32), mode='slidegrid', seed=2020)

            print(y1.shape, y2.shape, y3.shape, y4.shape)

            Y1 = pb.patch2tensor(y1, size=xshape, axis=(1, 2), mode='nfirst')
            Y2 = pb.patch2tensor(y2, size=xshape, axis=(1, 2), mode='nfirst')
            Y3 = pb.patch2tensor(y3, size=xshape, axis=(1, 2), mode='nfirst')
            Y4 = pb.patch2tensor(y4, size=xshape, axis=(1, 2), mode='nfirst')

            plt.figure()
            plt.subplot(221)
            plt.imshow(Y1)
            plt.title('randperm, shake=(0, 0)')
            plt.subplot(222)
            plt.imshow(Y2)
            plt.title('randgrid, shake=(0, 0)')
            plt.subplot(223)
            plt.imshow(Y3)
            plt.title('slidegrid, shake=(0, 0)')
            plt.subplot(224)
            plt.imshow(Y4)
            plt.title('slidegrid, shake=(32, 32)')
            plt.show()

    """

    axis = [axis] if type(axis) is int else list(axis)
    naxis = len(axis)
    sizep = [size] * naxis if type(size) is int else list(size)
    start = [start] * naxis if type(start) is int else list(start)
    stop = [stop] * naxis if type(stop) is int else list(stop)
    step = [step] * naxis if type(step) is int else list(step)
    shake = [shake] * naxis if type(shake) is float else list(shake)

    dimx = np.ndim(x)
    dimp = len(axis)
    sizex = np.array(x.shape)
    sizep = np.array(sizep)

    npatch = []
    npatch = np.uint32(sizex[axis] / sizep)
    N = int(np.prod(npatch))
    n = N if n is None else int(n)

    yshape = list(x.shape)
    for a, p in zip(axis, sizep):
        yshape[a] = p
    yshape = [n] + yshape

    for i in range(naxis):
        if stop[i] is None:
            stop[i] = sizex[axis[i]]

    y = np.zeros(yshape, dtype=x.dtype)

    if mode in ['slidegrid', 'SLIDEGRID', 'SlideGrid']:
        assert n <= N, ('n should be slower than ' + str(N + 1))
        seppos = slidegrid(start, stop, step, shake, n)
    if mode in ['randgrid', 'RANDGRID', 'RandGrid']:
        assert n <= N, ('n should be slower than ' + str(N + 1))
        setseed(seed, target='numpy')
        seppos = randgrid(start, stop, step, shake, n)

    if mode in ['randperm', 'RANDPERM', 'RandPerm']:
        setseed(seed, target='numpy')
        stop = [x - y for x, y in zip(stop, sizep)]
        seppos = randgrid(start, stop, [1] * dimp, [0] * dimp, n)

    for i in range(n):
        indexi = []
        for j in range(dimp):
            indexi.append(slice(seppos[j][i], seppos[j][i] + sizep[j]))
        t = x[sl(dimx, axis, indexi)]
        y[i] = t
    return y


def patch2tensor(p, size=(256, 256), axis=(1, 2), mode='nfirst'):
    r"""merge patch to a tensor


    Args:
        p (tensor): A tensor of patches.
        size (tuple, optional): Merged tensor size in the dimension (the default is (256, 256)).
        axis (tuple, optional): Merged axis of patch (the default is (1, 2))
        mode (str, optional): Patch mode ``'nfirst'`` or ``'nlast'`` (the default is 'nfirst',
            which means the first dimension is the number of patches)

    Returns:
        ndarray: Merged tensor.
    
    see :func:`tensor2patch`.

    """

    naxis = len(axis)
    sizep = list(p.shape)
    sizex = list(p.shape)
    dimp = np.ndim(p)
    axisp = list(range(0, dimp))
    npatch = []
    steps = sizep.copy()
    for a, s in zip(axis, size):
        npatch.append(int((s * 1.) / sizep[a]))
        sizex[a] = s
        steps[a] = sizep[a]

    if mode in ['nfirst', 'Nfirst', 'NFIRST']:
        axisn = 0
        N = p.shape[0]
        sizex = sizex[1:]
        steps = sizep[1:]
    if mode in ['nlast', 'Nlast', 'NLAST']:
        axisn = -1
        N = p.shape[-1]
        sizex = sizex[:-1]
        steps = sizep[:-1]

    x = np.zeros(sizex, dtype=p.dtype)

    dimx = np.ndim(x)
    axisx = list(range(dimx))

    index = []
    for a, stop, step in zip(axisx, sizex, steps):
        idx = np.array(range(0, stop, step))
        index.append(idx)
    index = arraycomb(index)
    naxisx = len(axisx)
    for n in range(N):
        indexn = []
        for a in axisx:
            indexn.append(slice(index[n, a], index[n, a] + steps[a], 1))
        x[sl(dimx, axisx, indexn)] = p[sl(dimp, axisn, n)]
    return x


def read_samples(datafiles, keys=[['SI', 'ca', 'cr']], nsamples=[10], groups=[1], mode='sequentially', axis=0, parts=None, seed=None):
    r"""Read samples

    Args:
        datafiles (list): list of path strings
        keys (list, optional): data keys to be read
        nsamples (list, optional): number of samples for each data file
        groups (list, optional): number of groups in each data file
        mode (str, optional): sampling mode for all datafiles
        axis (int, optional): sampling axis for all datafiles
        parts (None, optional): number of parts (split samples into some parts)
        seed (None, optional): the seed for random stream

    Returns:
        tensor: samples

    Raises:
        ValueError: :attr:`nsamples` should be large enough
    """

    nfiles = len(datafiles)
    if len(keys) == 1:
        keys = keys * nfiles
    if len(nsamples) == 1:
        nsamples = nsamples * nfiles
    if len(groups) == 1:
        groups = groups * nfiles

    nkeys = len(keys[0])

    if parts is None:
        outs = [[]] * nkeys
    else:
        nparts = len(parts)
        outs = [[[]] * nparts] * nkeys

    for datafile, key, n, group in zip(datafiles, keys, nsamples, groups):

        if datafile[datafile.rfind('.'):] == '.mat':
            data = loadmat(datafile)
        if datafile[datafile.rfind('.'):] in ['.h5', '.hdf5']:
            data = loadh5(datafile)

        N = data[key[0]].shape[axis]
        M = int(N / group)  # each group has M samples
        m = int(n / group)  # each group has m sampled samples

        if (M < m):
            raise ValueError('The tensor does not has enough samples')

        idx = []
        if mode in ['sequentially', 'Sequentially']:
            for g in range(group):
                idx += list(range(int(M * g), int(M * g) + m))
        if mode in ['uniformly', 'Uniformly']:
            for g in range(group):
                idx += list(range(int(M * g), int(M * g + M), int(M / m)))[:m]
        if mode in ['randomly', 'Randomly']:
            setseed(seed)
            for g in range(group):
                idx += randperm(int(M * g), int(M * g + M), m)

        for j, k in enumerate(key):
            d = np.ndim(data[k])
            if parts is None:
                outs[j] = cat((outs[j], data[k][sl(d, axis, [idx])]), axis=axis)
            else:
                nps, npe = 0, 0
                for i in range(nparts):
                    part = parts[i]
                    npe = nps + int(part * group)
                    outs[j][i] = cat((outs[j][i], data[k][sl(d, axis, [idx[nps:npe]])]), axis=axis)
                    nps = npe

    return outs


if __name__ == '__main__':

    setseed(2020)
    x = np.random.randint(0, 1000, (20, 3, 4))

    y1, idx1 = sample_tensor(x, 10, axis=0, groups=2, mode='sequentially', extra=True)
    y2, idx2 = sample_tensor(x, 10, axis=0, groups=2, mode='uniformly', extra=True)
    y3, idx3 = sample_tensor(x, 10, axis=0, groups=2, mode='randomly', extra=True)

    print(x.shape)
    print(y1.shape)
    print(y2.shape)
    print(y3.shape)
    print(idx1)
    print(idx2)
    print(idx3)

    x = np.random.randint(0, 1000, (20, 3, 4))
    y1, idx1 = shuffle_tensor(x, axis=0, groups=4, mode='intra', extra=True)
    y2, idx2 = shuffle_tensor(x, axis=0, groups=4, mode='inter', extra=True)
    y3, idx3 = shuffle_tensor(x, axis=0, groups=4, mode='whole', extra=True)

    print(x.shape)
    print(y1.shape)
    print(y2.shape)
    print(y3.shape)
    print(idx1)
    print(idx2)
    print(idx3)

    y1, y2, y3 = split_tensor(x, ratios=[0.7, 0.2, 0.1], axis=0, shuffle=False, seed=None)
    print(y3)
    y1, y2, y3 = split_tensor(x, ratios=[0.7, 0.2, 0.1], axis=0, shuffle=True, seed=None)
    print(y3)
    y1, y2, y3 = split_tensor(x, ratios=[0.7, 0.2, 0.1], axis=0, shuffle=True, seed=2021)
    print(y3)
    y1, y2, y3 = split_tensor(x, ratios=[0.7, 0.2, 0.1], axis=0, shuffle=True, seed=2021)
    print(y3)
    print(y1.shape, y2.shape, y3.shape)

    Na, Nr, Nc = (9, 12, 2)
    x = np.random.randint(0, 1000, (Na, Nr, Nc))

    print(x[:, :, 0], 'x', x.shape)
    print(x[:, :, 1], 'x', x.shape)

    y = dnsampling(x, ratio=(0.5, 0.5), axis=(0, 1), smode='uniform', omode='discard')
    print(y[:, :, 0], 'discard')
    print(y[:, :, 1], 'discard')

    y = dnsampling(x, ratio=(0.5, 0.5), axis=(0, 1), smode='uniform', omode='zero')
    print(y[:, :, 0], 'zero')
    print(y[:, :, 1], 'zero')

    y = dnsampling(x, ratio=(0.5, 0.5), axis=(0, 1), smode='random', omode='zero')
    print(y[:, :, 0], 'zero')
    print(y[:, :, 1], 'zero')

    y = dnsampling(x, ratio=(0.5, 0.5), axis=(0, 1), smode='random2', omode='zero')
    print(y[:, :, 0], 'zero')
    print(y[:, :, 1], 'zero')

    # y = tensor2patch(x, n=None, size=(2, 3), axis=(0, 1), mode='slide', step=(1, 1), seed=None)
    # print(y.shape, 'slide')
    # print(y[0, :, :, 0], 'slide')
    # print(y[0, :, :, 1], 'slide')
    y = tensor2patch(x, n=None, size=(2, 3), axis=(0, 1), step=(2, 3), shake=(0, 0), mode='randgrid', seed=None)
    print(y.shape, 'randgrid')
    print(y[0, :, :, 0], 'randgrid')
    print(y[0, :, :, 1], 'randgrid')

    y = tensor2patch(x, n=None, size=(2, 3), axis=(0, 1), step=(1, 1), shake=(0, 0), mode='randperm', seed=None)
    print(y.shape, 'randperm')
    print(y[0, :, :, 0], 'randperm')
    print(y[0, :, :, 1], 'randperm')
