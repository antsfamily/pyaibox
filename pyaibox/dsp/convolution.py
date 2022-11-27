#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : convolution.py
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
from pyaibox.dsp.ffts import fft, ifft, padfft
from pyaibox.base.mathops import nextpow2, c2r, r2c
from pyaibox.base.arrayops import cut


def conv1(f, g, shape='same', axis=0):
    r"""Convolution

    The convoltuion between f and g can be expressed as

    .. math::
       \begin{aligned}
       (f*g)[n] &= \sum_{m=-\infty}^{+\infty}f[m]g[n-m] \\
                &= \sum_{m=-\infty}^{+\infty}f[n-m]g[m]
       \end{aligned}
       :label: equ-1DConvDiscrete

    Parameters
    ----------
    f : numpy array
        data to be filtered, can be 2d matrix
    g : numpy array
        convolution kernel
    shape : str, optional
        - ``'full'``: returns the full convolution,
        - ``'same'``: returns the central part of the convolution
                that is the same size as x (default).
        - ``'valid'``: returns only those parts of the convolution
                that are computed without the zero-padded edges.
                LENGTH(y)is MAX(LENGTH(x)-MAX(0,LENGTH(g)-1),0).
    shape : int, optional
        convolution axis (the default is 0).
    """

    # if np.ndims(f) > 1:
    #     Nf = f.shape[axis]
    # else:
    #     Nf = len(f)
    # Ns = f.shape[1 - axis]
    Nf = len(f)
    Ng = len(g)
    N = Nf + Ng - 1

    f = np.hstack((np.zeros((Ng - 1)), f, np.zeros((Ng - 1))))
    g = g[::-1]
    y = []
    for n in range(N):
        y.append(np.dot(f[n:n + Ng], g))

    if shape in ['same', 'Same', 'SAME']:
        Ns = np.fix(Ng / 2.)
        Ne = Ns + Nf
    if shape in ['valid', 'Valid', 'VALID']:
        Ns = Ng - 1
        Ne = Ns + Nf - Ng + 1
    if shape in ['full', 'Full', 'FULL']:
        Ns = 0
        Ne = N
    Ns, Ne = np.int32([Ns, Ne])
    return np.array(y[Ns:Ne])


def cutfftconv1(y, nfft, Nx, Nh, shape='same', axis=0, ftshift=False):
    r"""Throwaway boundary elements to get convolution results.

    Throwaway boundary elements to get convolution results.

    Parameters
    ----------
    y : numpy array
        array after ``iff``.
    nfft : int
        number of fft points.
    Nx : int
        signal length
    Nh : int
        filter length
    shape : str
        output shape:
        1. ``'same'`` --> same size as input x, :math:`N_x`
        2. ``'valid'`` --> valid convolution output
        3. ``'full'`` --> full convolution output, :math:`N_x+N_h-1`
        (the default is 'same')
    axis : int
        convolution axis (the default is 0)
    ftshift : bool, optional
        whether to shift the frequencies (the default is False)

    Returns
    -------
    y : numpy array
        array with shape specified by :attr:`same`.
    """

    nfft, Nx, Nh = np.int32([nfft, Nx, Nh])
    N = Nx + Nh - 1
    Nextra = nfft - N

    if nfft < N:
        raise ValueError("~~~To get right results, nfft must be larger than Nx+Nh-1!")

    if ftshift:
        if np.mod(Nx, 2) > 0 and np.mod(Nh, 2) > 0:
            if Nextra > 0:
                Nhead = np.int32(np.fix((Nextra + 1) / 2.))
                Ntail = Nextra - Nhead
                y = cut(y, ((Nhead, np.int32(nfft - Ntail)),), axis=axis)
            else:
                y = cut(y, ((N - 1, N), (0, N - 1)), axis)
        else:
            Nhead = np.int32(np.fix(Nextra / 2.))
            Ntail = Nextra - Nhead
            y = cut(y, ((Nhead, np.int32(nfft - Ntail)),), axis=axis)
    else:
        Nhead = 0
        Ntail = Nextra
        y = cut(y, ((Nhead, np.int32(nfft - Ntail)),), axis=axis)

    if shape in ['same', 'SAME', 'Same']:
        Nstart = np.fix(Nh / 2.)
        Nend = Nstart + Nx
    elif shape in ['valid', 'VALID', 'Valid']:
        Nstart = Nh - 1
        Nend = N - (Nh - 1)
    elif shape in ['full', 'FULL', 'Full']:
        Nstart, Nend = (0, N)
    Nstart, Nend = np.int32([Nstart, Nend])
    y = cut(y, ((Nstart, Nend),), axis=axis)
    return y


def fftconv1(x, h, shape='same', caxis=None, axis=0, keepcaxis=False, nfft=None, ftshift=False, eps=None):
    """Convolution using Fast Fourier Transformation

    Convolution using Fast Fourier Transformation.

    Parameters
    ----------
    x : numpy array
        data to be convolved.
    h : numpy array
        filter array, it will be expanded to the same dimensions of :attr:`x` first.
    shape : str, optional
        output shape:
        1. ``'same'`` --> same size as input x, :math:`N_x`
        2. ``'valid'`` --> valid convolution output
        3. ``'full'`` --> full convolution output, :math:`N_x+N_h-1`
        (the default is 'same')
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`caxis` is ignored. If :attr:`X` is real-valued and :attr:`caxis` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`caxis` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued.
    axis : int, optional
        axis of convolution operation (the default is 0, which means the first dimension)
    keepcaxis : bool
        If :obj:`True`, the complex dimension will be keeped. Only works when :attr:`X` is complex-valued array 
        and :attr:`axis` is not :obj:`None` but represents in real format. Default is :obj:`False`.
    nfft : int, optional
        number of fft points (the default is :math:`2^{nextpow2(N_x+N_h-1)}`),
        note that :attr:`nfft` can not be smaller than :math:`N_x+N_h-1`.
    ftshift : bool, optional
        whether shift frequencies (the default is False)
    eps : None or float, optional
        x[abs(x)<eps] = 0 (the default is None, does nothing)

    Returns
    -------
    y : numpy array
        Convolution result array.

    """

    CplxRealflag = False
    if np.iscomplex(x).any():  # complex in complex
        pass
    else:
        if caxis is None:  # real
            pass
        else:  # complex in real
            CplxRealflag = True
            x = r2c(x, caxis=caxis, keepcaxis=keepcaxis)
            h = r2c(h, caxis=caxis, keepcaxis=keepcaxis)

    if np.ndim(h) == 1 and axis > 0:
        h = np.expand_dims(h, list(range(axis)))
    Nh = np.size(h, axis)
    Nx = np.size(x, axis)

    N = Nx + Nh - 1
    if nfft is None:
        nfft = 2**nextpow2(N)
    else:
        if nfft < N:
            raise ValueError("~~~To get right results, nfft must be larger than Nx+Nh-1!")

    x = padfft(x, nfft, axis, ftshift)
    h = padfft(h, nfft, axis, ftshift)
    X = fft(x, nfft, caxis=None, axis=axis, keepcaxis=False, norm=None, shift=ftshift)
    H = fft(h, nfft, caxis=None, axis=axis, keepcaxis=False, norm=None, shift=ftshift)
    Y = X * H
    y = ifft(Y, nfft, caxis=None, axis=axis, keepcaxis=False, norm=None, shift=ftshift)
    y = cutfftconv1(y, nfft, Nx, Nh, shape, axis, ftshift)

    if eps is not None:
        y[abs(y) < eps] = 0.

    if CplxRealflag:
        y = c2r(y, caxis=caxis, keepcaxis=not keepcaxis)

    return y


if __name__ == '__main__':

    ftshift = False
    ftshift = True
    x = np.array([1, 2, 3 + 6j, 4, 5])
    h = np.array([1 + 2j, 2, 3, 4, 5, 6, 7])

    y1 = conv1(x, h, shape='same')
    y2 = fftconv1(x, h, axis=0, nfft=None, shape='same', ftshift=ftshift)
    # print(y1)
    # print(y2)
    print(np.sum(np.abs(y1 - y2)), np.sum(np.angle(y1) - np.angle(y2)))

    y1 = conv1(x, h, shape='valid')
    y2 = fftconv1(x, h, axis=0, nfft=None, shape='valid', ftshift=ftshift)
    # print(y1)
    # print(y2)
    print(np.sum(np.abs(y1 - y2)), np.sum(np.angle(y1) - np.angle(y2)))

    y1 = conv1(x, h, shape='full')
    y2 = fftconv1(x, h, axis=0, nfft=None, shape='full', ftshift=ftshift)
    # print(y1)
    # print(y2)
    print(np.sum(np.abs(y1 - y2)), np.sum(np.angle(y1) - np.angle(y2)))
