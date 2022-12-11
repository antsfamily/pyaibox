#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : draw_shapes.py
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
from pyaibox.base.arrayops import sl


def draw_rectangle(x, rects, edgecolors=[[255, 0, 0]], linewidths=[1], fillcolors=[None], axes=(-3, -2)):
    """Draw rectangles in a tensor


    Parameters
    ----------
    x : numpy array
        The input with any size.
    rects : list or tuple
        The coordinates of the rectangles [[lefttop, rightbottom]].
    edgecolors : list, optional
        The color of edge.
    linewidths : int, optional
        The linewidths of edge.
    fillcolors : int, optional
        The color for filling.
    axes : int, optional
        The axes for drawing the rect (default [(-3, -2)]).

    Returns
    -------
    x : numpy array
        Output image array with rectangle shapes.

    see :func:`fmt_bbox`

    Example
    -------

    Draw rectangles in an figure, and return the result image array.

    .. image:: ./_static/demo_draw_rectangles.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import pyaibox as pl
        import matplotlib.pyplot as plt

        print(pb.__version__)

        x = pb.imread('../../data/images/LenaRGB512.tif')
        print(x.shape)

        # rects, edgecolors, fillcolors, linewidths = [[0, 0, 511, 511]], [None], [[0, 255, 0]], [1]
        # rects, edgecolors, fillcolors, linewidths = [[0, 0, 511, 511]], [[255, 0, 0]], [None], [1]
        # rects, edgecolors, fillcolors, linewidths = [[0, 0, 511, 511]], [[255, 0, 0]], [[0, 255, 0]], [1]
        rects, edgecolors, fillcolors, linewidths = [[64, 64, 128, 128], [200, 200, 280, 400]], [[0, 255, 0], [0, 0, 255]], [None, [255, 255, 0]], [1, 6]

        y = pb.draw_rectangle(x, rects, edgecolors=edgecolors, linewidths=linewidths, fillcolors=fillcolors, axes=[(0, 1)])

        pb.imsave('out.png', y)
        plt.figure()
        plt.imshow(y)
        plt.show()
        
    """

    axes = axes * len(rects) if len(axes) == 1 and len(rects) > 1 else axes

    x = np.array(x)
    d = np.ndim(x)

    for rect, edgecolor, linewidth, fillcolor, axis in zip(rects, edgecolors, linewidths, fillcolors, axes):
        edgecolor = np.array(edgecolor, dtype=x.dtype) if edgecolor is not None else None
        fillcolor = np.array(fillcolor, dtype=x.dtype) if fillcolor is not None else None
        if edgecolor is not None:
            top, left, bottom, right = rect
            for l in range(linewidth):
                x[sl(d, axis, [slice(top, bottom + 1), [left, right]])] = edgecolor
                x[sl(d, axis, [[top, bottom], slice(left, right + 1)])] = edgecolor
                top += 1
                left += 1
                bottom -= 1
                right -= 1
        if fillcolor is not None:
            top, left, bottom, right = rect
            top += linewidth
            left += linewidth
            bottom -= linewidth
            right -= linewidth
            x[sl(d, axis, [slice(top, bottom + 1), slice(left, right + 1)])] = fillcolor
    return x


def draw_eclipse(x, centroids, aradii, bradii, edgecolors=[255, 0, 0], linewidths=1, fillcolors=None, axes=(-2, -1)):

    for centroid, aradius, bradius in centroids, aradii, bradii:
        pass


if __name__ == '__main__':

    x = np.zeros((2, 8, 10, 3))

    rects = [[1, 2, 6, 8]]

    y = draw_rectangle(x, rects, edgecolors=[[100, 125, 255]], linewidths=[2], fillcolors=[None], axes=[(-3, -2)])

    print(x[0, :, :, 0])
    print(x[0, :, :, 1])
    print(x[0, :, :, 2])

    print(y[0, :, :, 0])
    print(y[0, :, :, 1])
    print(y[0, :, :, 2])

    y = draw_rectangle(x, rects, edgecolors=[[100, 125, 255]], linewidths=[2], fillcolors=[[20, 50, 80]], axes=[(-3, -2)])

    print(x[0, :, :, 0])
    print(x[0, :, :, 1])
    print(x[0, :, :, 2])

    print(y[0, :, :, 0])
    print(y[0, :, :, 1])
    print(y[0, :, :, 2])
