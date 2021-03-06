#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-25 19:44:35
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import math
import numpy as np
import matplotlib.pyplot as plt
from pyaibox.base.mathops import fnab


def cplot(ca, lmod=None):
    
    N = len(ca)
    if lmod is None:
        lmod = '-b'
    r = ca.real
    i = ca.imag
    for n in range(N):
        plt.plot([0, r[n]], [0, i[n]], lmod)
    plt.xlabel('real')
    plt.ylabel('imag')


def plots(x, ydict, plotdir='./', xlabel='x', ylabel='y', title='', issave=False, isshow=True):

    legend = []
    plt.figure()
    plt.grid()
    for k, v in ydict.items():
        plt.plot(x, v)
        legend.append(k)
    plt.legend(legend)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if issave:
        plt.savefig(plotdir + ylabel + '_' + xlabel + '.png')
    if isshow:
        plt.show()
    plt.close()


class Plots:

    def __init__(self, plotdir='./', xlabel='x', ylabel='y', title='', figname=None, issave=False, isshow=True):

        self.plotdir = plotdir
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.issave = issave
        self.isshow = isshow
        if figname is None or figname == '':
            self.figname = self.plotdir + self.ylabel + '_' + self.xlabel + '.png'
        else:
            self.figname = figname

    def __call__(self, x, ydict, figname=None):

        if figname is None or figname == '':
            figname = self.figname

        legend = []
        plt.figure()
        plt.grid()
        for k, v in ydict.items():
            plt.plot(x, v)
            legend.append(k)
        plt.legend(legend)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        if self.issave:
            plt.savefig(figname)
        if self.isshow:
            plt.show()
        plt.close()


def imshow(Xs, nrows=None, ncols=None, xlabels=None, ylabels=None, titles=None, figsize=None, outfile=None, **kwargs):
    r"""show images

    This function create an figure and show images in :math:`a` rows and :math:`b` columns.

    Parameters
    ----------
    Xs : array, list or tuple
        list/tuple of image arrays, if the type is not list or tuple, wrap it.
    nrows : int, optional
        show in :attr:`nrows` rows, by default None (auto computed).
    ncols : int, optional
        show in :attr:`ncols` columns, by default None (auto computed).
    xlabels : str, optional
        labels of x-axis
    ylabels : str, optional
        labels of y-axis
    titles : str, optional
        titles
    figsize : tuple, optional
        figure size, by default None
    outfile : str, optional
        save image to file, by default None (do not save).
    kwargs : 
        see :func:`matplotlib.pyplot.imshow`

    Returns
    -------
    plt
        plot handle

    Examples
    ---------

    ::

        x = np.random.rand(3, 100, 100)
        plt = imshow([xi for xi in x])
        plt.show()

    """

    if (type(Xs) is not list) and (type(Xs) is not tuple):
        Xs = [Xs]

    n = len(Xs)
    if (nrows is None) and (ncols is None):
        nrows, ncols = fnab(n)
    nrows = math.ceil(n / ncols) if nrows is None else nrows
    ncols = math.ceil(n / nrows) if ncols is None else ncols

    xlabels = [xlabels] * n if (type(xlabels) is str) or (xlabels is None) else xlabels
    ylabels = [ylabels] * n if (type(ylabels) is str) or (ylabels is None) else ylabels
    titles = [titles] * n if (type(titles) is str) or (titles is None) else titles
    plt.figure(figsize=figsize)
    for i, X, xlabel, ylabel, title in zip(range(n), Xs, xlabels, ylabels, titles):
        plt.subplot(nrows, ncols, i + 1)
        plt.imshow(X, **kwargs)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

    if outfile is not None:
        plt.savefig(outfile)
    return plt


def mesh(Zs, nrows=None, ncols=None, xlabels=None, ylabels=None, zlabels=None, titles=None, figsize=None, outfile=None, **kwargs):
    r"""mesh

    This function create an figure and show some 2d-arrays in :math:`a` rows and :math:`b` columns with 3d projection.

    Parameters
    ----------
    Zs : array, list or tuple
        list/tuple of image arrays, if the type is not list or tuple, wrap it.
    nrows : int, optional
        show in :attr:`nrows` rows, by default None (auto computed).
    ncols : int, optional
        show in :attr:`ncols` columns, by default None (auto computed).
    xlabels : str, optional
        labels of x-axis
    ylabels : str, optional
        labels of y-axis
    zlabels : str, optional
        labels of z-axis
    titles : str, optional
        titles
    figsize : tuple, optional
        figure size, by default None
    outfile : str, optional
        save image to file, by default None (do not save).
    kwargs : 
        Xs : list or tuple
        Ys : list or tuple
        
        for others, see :func:`matplotlib.pyplot.plot_surface`

    Returns
    -------
    plt
        plot handle

    Examples
    ---------

    ::

        x, y = np.meshgrid(np.arange(0, 10), np.arange(0, 20))
        z = np.random.rand(20, 10)

        plt = mesh(z, 1, 2)
        plt.show()
        
        plt = mesh(z, 1, 2, Xs=[np.arange(30, 40)])
        plt.show()

    """

    if (type(Zs) is not list) and (type(Zs) is not tuple):
        Zs = [Zs]

    n = len(Zs)
    if (nrows is None) and (ncols is None):
        nrows, ncols = fnab(n)
    nrows = math.ceil(n / ncols) if nrows is None else nrows
    ncols = math.ceil(n / nrows) if ncols is None else ncols

    xlabels = [xlabels] * n if (type(xlabels) is str) or (xlabels is None) else xlabels
    ylabels = [ylabels] * n if (type(ylabels) is str) or (ylabels is None) else ylabels
    zlabels = [zlabels] * n if (type(zlabels) is str) or (zlabels is None) else zlabels
    titles = [titles] * n if (type(titles) is str) or (titles is None) else titles

    if 'Xs' in kwargs:
        Xs = kwargs['Xs']
        del(kwargs['Xs'])
    else:
        Xs = [None]
    if 'Ys' in kwargs:
        Ys = kwargs['Ys']
        del(kwargs['Ys'])
    else:
        Ys = [None]

    Xs = Xs * n if len(Xs) == 1 else Xs
    Ys = Ys * n if len(Ys) == 1 else Ys

    fig = plt.figure(figsize=figsize)
    
    axs = []
    for cnt in range(n):
        ax = fig.add_subplot(nrows, ncols, cnt + 1, projection='3d')
        axs.append(ax)

    for ax, X, Y, Z, xlabel, ylabel, zlabel, title in zip(axs, Xs, Ys, Zs, xlabels, ylabels, ylabels, titles):
        H, W = Z.shape
        X0, Y0 = np.meshgrid(np.arange(0, W, 1), np.arange(0, H, 1), indexing='xy')
        X = X0 if X is None else X
        Y = Y0 if Y is None else Y

        ax.plot_surface(X, Y, Z, **kwargs)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        ax.set_title(title)

    if outfile is not None:
        plt.savefig(outfile)
    return plt
    
def mshow(Zs, nrows=None, ncols=None, xlabels=None, ylabels=None, zlabels=None, titles=None, projections=None, figsize=None, outfile=None, **kwargs):
    r"""show tensors

    This function create an figure and show some 2d-arrays in :math:`a` rows and :math:`b` columns with 2d/3d projection.

    Parameters
    ----------
    Zs : array, list or tuple
        list/tuple of image arrays, if the type is not list or tuple, wrap it.
    nrows : int, optional
        show in :attr:`nrows` rows, by default None (auto computed).
    ncols : int, optional
        show in :attr:`ncols` columns, by default None (auto computed).
    xlabels : str, optional
        labels of x-axis
    ylabels : str, optional
        labels of y-axis
    zlabels : str, optional
        labels of z-axis
    titles : str, optional
        titles
    figsize : tuple, optional
        figure size, by default None
    outfile : str, optional
        save image to file, by default None (do not save).
    kwargs : 
        Xs : list or tuple
        Ys : list or tuple
        
        for others, see :func:`matplotlib.pyplot.plot_surface`

    Returns
    -------
    plt
        plot handle

    Examples
    ---------

    ::

        x, y = np.meshgrid(np.arange(0, 10), np.arange(0, 20))
        z1 = np.random.rand(20, 10)
        z2 = np.random.randn(60, 60)

        plt = mshow([z1, z2], 1, 2, Xs=[np.arange(30, 40)], projections=['3d', '2d'])
        plt.show()


    """

    if (type(Zs) is not list) and (type(Zs) is not tuple):
        Zs = [Zs]

    n = len(Zs)
    if (nrows is None) and (ncols is None):
        nrows, ncols = fnab(n)
    nrows = math.ceil(n / ncols) if nrows is None else nrows
    ncols = math.ceil(n / nrows) if ncols is None else ncols

    xlabels = [xlabels] * n if (type(xlabels) is str) or (xlabels is None) else xlabels
    ylabels = [ylabels] * n if (type(ylabels) is str) or (ylabels is None) else ylabels
    zlabels = [zlabels] * n if (type(zlabels) is str) or (zlabels is None) else zlabels
    titles = [titles] * n if (type(titles) is str) or (titles is None) else titles
    projections = [projections] * n if (type(projections) is str) or (projections is None) else projections

    if 'Xs' in kwargs:
        Xs = kwargs['Xs']
        del(kwargs['Xs'])
    else:
        Xs = [None]
    if 'Ys' in kwargs:
        Ys = kwargs['Ys']
        del(kwargs['Ys'])
    else:
        Ys = [None]

    Xs = Xs * n if len(Xs) == 1 else Xs
    Ys = Ys * n if len(Ys) == 1 else Ys

    fig = plt.figure(figsize=figsize)
    
    axs = []
    for cnt in range(n):
        projection = projections[cnt]
        projection = None if projection == '2d' else projection
        ax = fig.add_subplot(nrows, ncols, cnt + 1, projection=projection)
        axs.append(ax)

    for ax, X, Y, Z, projection, xlabel, ylabel, zlabel, title in zip(axs, Xs, Ys, Zs, projections, xlabels, ylabels, zlabels, titles):
        H, W = Z.shape
        if projection == '3d':
            X0, Y0 = np.meshgrid(np.arange(0, W, 1), np.arange(0, H, 1), indexing='xy')
            X = X0 if X is None else X
            Y = Y0 if Y is None else Y
            ax.plot_surface(X, Y, Z, **kwargs)
            ax.set_zlabel(zlabel)
        else:
            ax.imshow(Z, **kwargs)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

    if outfile is not None:
        plt.savefig(outfile)
    return plt


if __name__ == '__main__':

    N = 3

    r = np.random.rand(N)
    i = -np.random.rand(N)

    print(r)
    print(i)
    x = r + 1j * i

    cplot(x)
    plt.show()

    Ns = 100
    x = np.linspace(-1, 1, Ns)

    y = np.random.randn(Ns)
    f = np.random.randn(Ns)

    plot = Plots(plotdir='./', issave=True)
    plot(x, {'y': y, 'f': f})

    x = np.random.rand(3, 100, 100)
    plt = imshow([xi for xi in x])
    plt.show()

    x, y = np.meshgrid(np.arange(0, 10), np.arange(0, 20))
    z = np.random.rand(20, 10)
    plt = mesh(z, 1, 2, Xs=[np.arange(30, 40)])
    plt.show()

    plt = mshow([z, np.random.randn(60, 60)], 1, 2, Xs=[np.arange(30, 40)], projections=['3d', '2d'])
    plt.show()
