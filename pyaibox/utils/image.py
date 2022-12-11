#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : image.py
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

from skimage.io import imread as skimread
from skimage.io import imsave as skimsave
from skimage.transform import resize as skimresize

import numpy as np


def imread(imgfile):
    return skimread(imgfile)


def imsave(outfile, img):
    return skimsave(outfile, img, check_contrast=False)


def histeq(img, nbins=256):
    dshape = img.shape
    imhist, bins = np.histogram(img.flatten(), nbins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255.0 * cdf / cdf[-1]
    # 使用累积分布函数的线性插值，计算新的像素值
    img = np.interp(img.flatten(), bins[:-1], cdf)
    return img.reshape(dshape)


def imresize(img, oshape=None, odtype=None, order=1, mode='constant', cval=0, clip=True, preserve_range=False):
    r"""resize image to oshape

    see :func:`skimage.transform.resize`.

    Parameters
    ----------
    img : ndarray
        Input image.
    oshape : tulpe, optional
        output shape (the default is None, which is the same as the input)
    odtype : str, optional
        output data type, ``'uint8', 'uint16', 'int8', ...`` (the default is None, float)
    order : int, optional
        The order of the spline interpolation, default is 1. The order has to
        be in the range 0-5. See `skimage.transform.warp` for detail.
    mode : str, optional
        Points outside the boundaries of the input are filled according
        to the given mode. {``'constant'``, ``'edge'``, ``'symmetric'``, ``'reflect'``, ``'wrap'``},
        Modes match the behaviour of `numpy.pad`.  The
        default mode is 'constant'.
    cval : float, optional
        Used in conjunction with mode 'constant', the value outside
        the image boundaries.
    clip : bool, optional
        Whether to clip the output to the range of values of the input image.
        This is enabled by default, since higher order interpolation may
        produce values outside the given input range.
    preserve_range : bool, optional
        Whether to keep the original range of values. Otherwise, the input
        image is converted according to the conventions of `img_as_float`.

    Returns
    -------
    resized : ndarray
        Resized version of the input.

    Notes
    -----
    Modes 'reflect' and 'symmetric' are similar, but differ in whether the edge
    pixels are duplicated during the reflection.  As an example, if an array
    has values [0, 1, 2] and was padded to the right by four values using
    symmetric, the result would be [0, 1, 2, 2, 1, 0, 0], while for reflect it
    would be [0, 1, 2, 1, 0, 1, 2].

    Examples
    --------
    ::

        >>> from skimage import data
        >>> from skimage.transform import resize
        >>> image = data.camera()
        >>> resize(image, (100, 100), mode='reflect').shape
        (100, 100)

    """

    oimage = skimresize(img, output_shape=oshape, order=1, mode=mode,
                        cval=cval, clip=clip, preserve_range=preserve_range)

    if odtype is not None:
        oimage = oimage.astype(odtype)

    return oimage
