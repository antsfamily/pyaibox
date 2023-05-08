#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : contrast.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Nov 11 2020
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
from pyaibox.utils.colors import gray2rgb
import matplotlib.pyplot as plt


def categorical2onehot(X, nclass=None):
    r"""converts categorical to onehot

    Parameters
    ----------
    X : list or array
        the categorical list or array
    nclass : int, optional
        the number of classes, by default None (auto detected)

    Returns
    -------
    array
        the one-hot matrix
    """    
    X = np.array(X)
    X = X.astype('int')
    if nclass is None:
        nclass = len(np.unique(X))
    
    offset = np.min(X)
    X -= offset
    return np.eye(nclass)[X]

def onehot2categorical(X, axis=-1, offset=0):
    r"""converts onehot to categorical

    Parameters
    ----------
    X : list or array
        the one-hot array
    axis : int, optional
        the axis for one-hot encoding, by default -1
    offset : int, optional
        category label head, by default 0

    Returns
    -------
    array
        the category label
    """    
    return np.argmax(X, axis=axis) + offset

def accuracy(P, T, axis=None):
    r"""computes the accuracy

    .. math::
       A = \frac{\rm TP+TN}{TP+TN+FP+FN}

    Parameters
    ----------
    P : list or array
        predicted label (categorical or one-hot)
    T : list or array
        target label (categorical or one-hot)
    axis : int, optional
        the one-hot encoding axis, by default None, which means :attr:`P` and :attr:`T` are categorical.

    Returns
    -------
    float
        the accuracy

    Raises
    ------
    ValueError
        :attr:`P` and :attr:`T` should have the same shape!
    ValueError
        You should specify the one-hot encoding axis when :attr:`P` and :attr:`T` are in one-hot formation!

    Examples
    --------

    ::

        import pyaibox as pb

        T = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 5])
        P = np.array([1, 2, 3, 4, 1, 6, 3, 2, 1, 4, 5, 6, 1, 2, 1, 4, 5, 6, 1, 5])

        print(pb.accuracy(P, T))

        #---output
        0.8 

    """
    P = np.array(P) if (type(P) is list) or (type(P) is tuple) else P
    T = np.array(T) if (type(T) is list) or (type(T) is tuple) else T

    if P.shape != T.shape:
        raise ValueError("P and T should have the same shape!")

    if ((np.prod(P.shape) != np.max(P.shape)) or (np.prod(T.shape) != np.max(T.shape))) and (axis is None):
        raise ValueError("You should specify the one-hot encoding axis!")
    
    if axis is not None:
       P = np.argmax(P, axis=axis) if np.prod(P.shape) != np.max(P.shape) else P
       T = np.argmax(T, axis=axis) if np.prod(T.shape) != np.max(T.shape) else T

    return np.sum(P==T) / len(P)


def confusion(P, T, axis=None, cmpmode='...'):
    r"""computes the confusion matrix

    Parameters
    ----------
    P : list or array
        predicted label (categorical or one-hot)
    T : list or array
        target label (categorical or one-hot)
    axis : int, optional
        the one-hot encoding axis, by default None, which means :attr:`P` and :attr:`T` are categorical.
    cmpmode : str, optional
        ``'...'`` for one-by one mode, ``'@'`` for multiplication mode (:math:`P^TT`), by default '...'

    Returns
    -------
    array
        the confusion matrix

    Raises
    ------
    ValueError
        :attr:`P` and :attr:`T` should have the same shape!
    ValueError
        You should specify the one-hot encoding axis when :attr:`P` and :attr:`T` are in one-hot formation!

    Examples
    --------

    ::

        import pyaibox as pb

        T = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 5])
        P = np.array([1, 2, 3, 4, 1, 6, 3, 2, 1, 4, 5, 6, 1, 2, 1, 4, 5, 6, 1, 5])

        C = pb.confusion(P, T, cmpmode='...')
        print(C)
        C = pb.confusion(P, T, cmpmode='@')
        print(C)

        #---output
        [[3. 0. 2. 0. 1. 0.]
        [0. 3. 0. 0. 0. 0.]
        [1. 0. 1. 0. 0. 0.]
        [0. 0. 0. 3. 0. 0.]
        [0. 0. 0. 0. 3. 0.]
        [0. 0. 0. 0. 0. 3.]]
        [[3. 0. 2. 0. 1. 0.]
        [0. 3. 0. 0. 0. 0.]
        [1. 0. 1. 0. 0. 0.]
        [0. 0. 0. 3. 0. 0.]
        [0. 0. 0. 0. 3. 0.]
        [0. 0. 0. 0. 0. 3.]]

    """    
    P = np.array(P) if (type(P) is list) or (type(P) is tuple) else P
    T = np.array(T) if (type(T) is list) or (type(T) is tuple) else T

    if P.shape != T.shape:
        raise ValueError("P and T should have the same shape!")

    if ((np.prod(P.shape) != np.max(P.shape)) or (np.prod(T.shape) != np.max(T.shape))) and (axis is None):
        raise ValueError("You should specify the one-hot axis!")
    
    if axis is not None:
       P = np.argmax(P, axis=axis) if np.prod(P.shape) != np.max(P.shape) else P
       T = np.argmax(T, axis=axis) if np.prod(T.shape) != np.max(T.shape) else T

    T = T.astype('int')
    P = P.astype('int')
    if cmpmode.lower() in ['...', 'for']:
        nclass = len(np.unique(T))
        offset = np.min(T)
        T -= offset
        P -= offset
        C = np.zeros((nclass, nclass))
        for p, t in zip(P, T):
            C[p, t] += 1

    if cmpmode.lower() in ['@', 'mul', 'matmul']:
        P = categorical2onehot(P, nclass=None)
        T = categorical2onehot(T, nclass=None)
        C = P.T @ T

    return C

def kappa(C):
    r"""computes kappa

    .. math::
       K = \frac{p_o - p_e}{1 - p_e}

    where :math:`p_o` and :math:`p_e` can be obtained by

    .. math::
        p_o = \frac{\sum_iC_{ii}}{\sum_i\sum_jC_{ij}} 
    
    .. math::
        p_e = \frac{\sum_j\left(\sum_iC_{ij}\sum_iC_{ji}\right)}{\sum_i\sum_jC_{ij}} 

    Parameters
    ----------
    C : array
        The confusion matrix

    Returns
    -------
    float
        The kappa value.

    Examples
    --------

    ::

        import pyaibox as pb

        T = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 5])
        P = np.array([1, 2, 3, 4, 1, 6, 3, 2, 1, 4, 5, 6, 1, 2, 1, 4, 5, 6, 1, 5])

        C = pb.confusion(P, T, cmpmode='...')
        print(pb.kappa(C))
        print(pb.kappa(C.T))

        #---output
        0.7583081570996979
        0.7583081570996979

    """

    nsamples = np.sum(C)
    po = np.sum(np.diag(C)) / nsamples
    pe = np.sum(np.sum(C, axis=0) * np.sum(C.T, 0)) / nsamples / nsamples
    K = (po - pe) / (1 - pe)
    return K

def plot_confusion(C, cmap=None, mode='rich', xticks='label', yticks='label', xlabel='Target', ylabel='Predicted', title='Confusion matrix', **kwargs):
    r"""plots confusion matrix.

    plots confusion matrix.

    Parameters
    ----------
    C : array
        The confusion matrix
    cmap : None or str, optional
        The colormap, by default :obj:`None`, which means our default configuration (green-coral)
    mode : str, optional
        ``'pure'``, ``'bare'``, ``'simple'`` or ``'rich'``
    xticks : str, tuple or list, optional
        ``'label'`` --> class labels, or you can specify class name list, by default ``'label'``
    yticks : str, tuple or list, optional
        ``'label'`` --> class labels, or you can specify class name list, by default ``'label'``
    xlabel : str, optional
        The label string of axis-x, by default 'Target'
    ylabel : str, optional
        The label string of axis-y, by default 'Predicted'
    title : str, optional
        The title string, by default 'Confusion matrix'
    kwargs :
        linespacing : float
            The line spacing of text, by default ``0.15``
        numftd : dict
            The font dict of integer value, by default ::

                dict(fontsize=12, color='black', 
                     family='Times New Roman', 
                     weight='bold', style='normal')
        pctftd : dict
            The font dict of percent value, by default ::
            
                dict(fontsize=12, color='black', 
                     family='Times New Roman', 
                     weight='light', style='normal')
        restftd : dict
            The font dict of label, title and ticks, by default ::

                dict(fontsize=12, color='black', 
                     family='Times New Roman', 
                     weight='light', style='normal')
        pctfmt : str
            the format of percent value, such as ``'%.xf'`` means formating with two decimal places, by default ``'%.1f'``

    Returns
    -------
    pyplot
        pyplot handle

    Example
    -------

    .. image:: ./_static/ConfusionMatrixSimple.png
       :scale: 100 %
       :align: center

    .. image:: ./_static/ConfusionMatrixRich.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import pyaibox as pb

        T = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 5])
        P = np.array([1, 2, 3, 4, 1, 6, 3, 2, 1, 4, 5, 6, 1, 2, 1, 4, 5, 6, 1, 5])

        C = pb.confusion(P, T, cmpmode='@')

        plt = tb.plot_confusion(C, cmap=None, mode='simple')
        plt = tb.plot_confusion(C, cmap='summer', mode='simple')
        plt.show()

        plt = pb.plot_confusion(C, cmap=None, mode='rich')
        plt = pb.plot_confusion(C, cmap='summer', mode='rich')
        plt.show()

    """    

    nclass, _ = C.shape
    n = np.sum(C)
    linespacing = 0.15
    pctfmt = '%.1f'

    if 'linespacing' in kwargs:
        linespacing = kwargs['linespacing']
        del(kwargs['linespacing'])
    if 'pctfmt' in kwargs:
        pctfmt = kwargs['pctfmt']
        del(kwargs['pctfmt'])

    if 'numftd' in kwargs:
        numftd = kwargs['numftd']
    else:
        numftd = dict(fontsize=12,
                        color='black',
                        family='Times New Roman',
                        weight='bold',
                        style='normal',
                        )
    if 'pctftd' in kwargs:
        pctftd = kwargs['pctftd']
    else:
        pctftd = dict(fontsize=12,
                        color='black',
                        family='Times New Roman',
                        weight='light',
                        style='normal',
                        )
    if 'restftd' in kwargs:
        restftd = kwargs['restftd']
    else:
        restftd = dict(fontsize=12,
                        color='black',
                        family='Times New Roman',
                        weight='light',
                        style='normal',
                        )
        
    xticks = [str(i) for i in range(1, nclass+1)] if xticks == 'label' else list(xticks)
    yticks = [str(i) for i in range(1, nclass+1)] if yticks == 'label' else list(yticks)

    if mode == 'rich':
        xticks = [' '] + xticks + [' ']
        yticks = [' '] + yticks + [' ']
        plt.figure(**kwargs)
        if cmap is not None:
            Cc = gray2rgb(C, cmap=cmap)
            Cc = np.pad(Cc, ((1, 1), (1, 1), (0, 0)))
            Cc = Cc.astype(np.uint8)
        else:
            Cc = np.zeros((nclass+2, nclass+2, 3), dtype=np.uint8)
            Cc[..., 0] = 249; Cc[..., 1] = 196; Cc[..., 2] = 192
            for i in range(1, nclass+1):
                Cc[i, i, :] = [186, 231, 198]
        Cc[-1, :, :] = Cc[:, -1, :] = Cc[0, :, :] = Cc[:, 0, :] = [240, 240, 240]
        Cc[-1, -1, :] = Cc[0, 0, :] = [214, 217, 226]
        plt.imshow(Cc)
        
        for i in range(0, nclass+2):
            plt.plot((-0.5, nclass+1+0.5), (i-0.5, i-0.5), '-k', linewidth=0.5)
            plt.plot((i-0.5, i-0.5), (-0.5, nclass+1+0.5), '-k', linewidth=0.5)

        for i in range(nclass):
            for j in range(nclass):
                s1 = '%d' % C[i, j]
                s2 = pctfmt % (C[i, j] * 100 / n) + '%'
                plt.text(j+1, i+1-linespacing, s1, fontdict=numftd, ha='center', va='center')
                plt.text(j+1, i+1+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        numftd['color'], numftd['weight'] = 'black', 'normal'
        pctftd['color'], pctftd['weight'] = 'coral', 'normal'
        qcol = np.sum(C, axis=0)
        qrow = np.sum(C, axis=1)
        qdiag = np.diag(C)
        j = 0
        for i in range(nclass):
            s1 = '%d' % qrow[i]
            s2 = '%d' % (qrow[i] - qdiag[i])
            plt.text(j, i+1-linespacing, s1, fontdict=numftd, ha='center', va='center')
            plt.text(j, i+1+linespacing, s2, fontdict=pctftd, ha='center', va='center')
        
        i = 0
        for j in range(nclass):
            s1 = '%d' % qcol[j]
            s2 = '%d' % (qcol[j] - qdiag[j])
            plt.text(j+1, i-linespacing, s1, fontdict=numftd, ha='center', va='center')
            plt.text(j+1, i+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        s1 = '%d' % n
        s2 = '%d' % (n - sum(qdiag))
        numftd['weight'] = 'bold'
        pctftd['weight'] = 'bold'
        plt.text(0, 0-linespacing, s1, fontdict=numftd, ha='center', va='center')
        plt.text(0, 0+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        numftd['color'], numftd['weight'] = 'green', 'normal'
        pctftd['color'], pctftd['weight'] = 'coral', 'normal'
        pcol = qdiag / (qcol + 1e-32)
        prow = qdiag / (qrow + 1e-32)
        j = nclass
        for i in range(nclass):
            s1 = pctfmt % (prow[i] * 100) + '%'
            s2 = pctfmt % (100 - prow[i] * 100) + '%'
            plt.text(j+1, i+1-linespacing, s1, fontdict=numftd, ha='center', va='center')
            plt.text(j+1, i+1+linespacing, s2, fontdict=pctftd, ha='center', va='center')
        
        i = nclass
        for j in range(nclass):
            s1 = pctfmt % (pcol[j] * 100) + '%'
            s2 = pctfmt % (100 -  pcol[j] * 100) + '%'
            plt.text(j+1, i+1-linespacing, s1, fontdict=numftd, ha='center', va='center')
            plt.text(j+1, i+1+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        nd = np.trace(C) / n
        s1 = pctfmt % (nd * 100) + '%'
        s2 = pctfmt % (100 -  nd * 100) + '%'
        numftd['weight'] = 'bold'
        pctftd['weight'] = 'bold'
        plt.text(nclass+1, nclass+1-linespacing, s1, fontdict=numftd, ha='center', va='center')
        plt.text(nclass+1, nclass+1+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        plt.xticks(range(0, nclass+2), xticks, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.yticks(range(0, nclass+2), yticks, ha='center', va='center', rotation=90, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.tick_params(left=False, bottom=False)
        plt.xlabel(xlabel, fontdict=restftd)
        plt.ylabel(ylabel, fontdict=restftd)
        plt.title(title, fontdict=restftd)

    if mode == 'simple':
        xticks = xticks + [' ']
        yticks = yticks + [' ']
        plt.figure(**kwargs)
        if cmap is not None:
            Cc = gray2rgb(C, cmap=cmap)
            Cc = np.pad(Cc, ((0, 1), (0, 1), (0, 0)))
            Cc = Cc.astype(np.uint8)
        else:
            Cc = np.zeros((nclass+1, nclass+1, 3), dtype=np.uint8)
            Cc[..., 0] = 249; Cc[..., 1] = 196; Cc[..., 2] = 192
            for i in range(nclass):
                Cc[i, i, :] = [186, 231, 198]
        Cc[-1, :, :] = Cc[:, -1, :] = [240, 240, 240]
        Cc[-1, -1, :] = [214, 217, 226]
        plt.imshow(Cc)
    
        for i in range(nclass+1):
            plt.plot((-0.5, nclass+0.5), (i-0.5, i-0.5), '-k', linewidth=0.5)
            plt.plot((i-0.5, i-0.5), (-0.5, nclass+0.5), '-k', linewidth=0.5)

        for i in range(nclass):
            for j in range(nclass):
                s1 = '%d' % C[i, j]
                s2 = pctfmt % (C[i, j] * 100 / n) + '%'
                plt.text(j, i-linespacing, s1, fontdict=numftd, ha='center', va='center')
                plt.text(j, i+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        numftd['color'], numftd['weight'] = 'green', 'normal'
        pctftd['color'], pctftd['weight'] = 'coral', 'normal'
        pcol = np.diag(C) / (np.sum(C, axis=0) + 1e-32)
        prow = np.diag(C) / (np.sum(C, axis=1) + 1e-32)
        j = nclass
        for i in range(nclass):
            s1 = pctfmt % (prow[i] * 100) + '%'
            s2 = pctfmt % (100 - prow[i] * 100) + '%'
            plt.text(j, i-linespacing, s1, fontdict=numftd, ha='center', va='center')
            plt.text(j, i+linespacing, s2, fontdict=pctftd, ha='center', va='center')
        
        i = nclass
        for j in range(nclass):
            s1 = pctfmt % (pcol[j] * 100) + '%'
            s2 = pctfmt % (100 -  pcol[j] * 100) + '%'
            plt.text(j, i-linespacing, s1, fontdict=numftd, ha='center', va='center')
            plt.text(j, i+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        nd = np.trace(C) / n
        s1 = pctfmt % (nd * 100) + '%'
        s2 = pctfmt % (100 -  nd * 100) + '%'
        numftd['weight'] = 'bold'
        pctftd['weight'] = 'bold'
        plt.text(nclass, nclass-linespacing, s1, fontdict=numftd, ha='center', va='center')
        plt.text(nclass, nclass+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        plt.xticks(range(0, nclass+1), xticks, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.yticks(range(0, nclass+1), yticks, ha='center', va='center', rotation=90, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.tick_params(left=False, bottom=False)
        plt.xlabel(xlabel, fontdict=restftd)
        plt.ylabel(ylabel, fontdict=restftd)
        plt.title(title, fontdict=restftd)

    if mode == 'bare':
        xticks = xticks
        yticks = yticks
        plt.figure(**kwargs)
        if cmap is not None:
            Cc = gray2rgb(C, cmap=cmap)
            Cc = Cc.astype(np.uint8)
        else:
            Cc = np.zeros((nclass, nclass, 3), dtype=np.uint8)
            Cc[..., 0] = 249; Cc[..., 1] = 196; Cc[..., 2] = 192
            for i in range(nclass):
                Cc[i, i, :] = [186, 231, 198]
        plt.imshow(Cc)
    
        for i in range(nclass):
            plt.plot((-0.5, nclass-0.5), (i-0.5, i-0.5), '-k', linewidth=0.5)
            plt.plot((i-0.5, i-0.5), (-0.5, nclass-0.5), '-k', linewidth=0.5)

        for i in range(nclass):
            for j in range(nclass):
                s1 = '%d' % C[i, j]
                s2 = pctfmt % (C[i, j] * 100 / n) + '%'
                plt.text(j, i-linespacing, s1, fontdict=numftd, ha='center', va='center')
                plt.text(j, i+linespacing, s2, fontdict=pctftd, ha='center', va='center')

        plt.xticks(range(0, nclass), xticks, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.yticks(range(0, nclass), yticks, ha='center', va='center', rotation=90, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.tick_params(left=False, bottom=False)
        plt.xlabel(xlabel, fontdict=restftd)
        plt.ylabel(ylabel, fontdict=restftd)
        plt.title(title, fontdict=restftd)

    if mode == 'pure':
        xticks = xticks
        yticks = yticks
        plt.figure(**kwargs)
        if cmap is not None:
            Cc = gray2rgb(C, cmap=cmap)
            Cc = Cc.astype(np.uint8)
        else:
            Cc = np.zeros((nclass, nclass, 3), dtype=np.uint8)
            Cc[..., 0] = 249; Cc[..., 1] = 196; Cc[..., 2] = 192
            for i in range(nclass):
                Cc[i, i, :] = [186, 231, 198]
        plt.imshow(Cc)
    
        for i in range(nclass):
            plt.plot((-0.5, nclass-0.5), (i-0.5, i-0.5), '-k', linewidth=0.5)
            plt.plot((i-0.5, i-0.5), (-0.5, nclass-0.5), '-k', linewidth=0.5)

        for i in range(nclass):
            for j in range(nclass):
                s1 = '%d' % C[i, j]
                plt.text(j, i, s1, fontdict=numftd, ha='center', va='center')

        plt.xticks(range(0, nclass), xticks, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.yticks(range(0, nclass), yticks, ha='center', va='center', rotation=90, fontproperties=restftd['family'], size=restftd['fontsize'])
        plt.tick_params(left=False, bottom=False)
        plt.xlabel(xlabel, fontdict=restftd)
        plt.ylabel(ylabel, fontdict=restftd)
        plt.title(title, fontdict=restftd)

    return plt



if __name__ == '__main__':

    import pyaibox as pb

    T = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 5.0])
    P = np.array([1, 2, 3, 4, 1, 6, 3, 2, 1, 4, 5, 6, 1, 2, 1, 4, 5, 6, 1, 5.0])
    classnames = ['cat', 'dog', 'car', 'cup', 'desk', 'baby']

    print(pb.accuracy(P, T))
    print(pb.categorical2onehot(T))

    C = pb.confusion(P, T, cmpmode='...')
    print(C)
    C = pb.confusion(P, T, cmpmode='@')
    print(C)
    print(pb.kappa(C))
    print(pb.kappa(C.T))

    plt = pb.plot_confusion(C, cmap=None, mode='pure')
    plt = pb.plot_confusion(C, cmap='summer', xticks=classnames, yticks=classnames, mode='pure')
    plt.show()

    plt = pb.plot_confusion(C, cmap=None, mode='bare')
    plt = pb.plot_confusion(C, cmap='summer', xticks=classnames, yticks=classnames, mode='bare')
    plt.show()

    plt = pb.plot_confusion(C, cmap=None, mode='simple')
    plt = pb.plot_confusion(C, cmap='summer', xticks=classnames, yticks=classnames, mode='simple')
    plt = pb.plot_confusion(C, cmap=None, mode='rich')
    plt = pb.plot_confusion(C, cmap='summer', mode='rich')
    plt = pb.plot_confusion(C, cmap=None, mode='simple')
    plt = pb.plot_confusion(C, cmap='summer', mode='simple')
    plt = pb.plot_confusion(C, cmap=None, mode='rich')
    plt = pb.plot_confusion(C, cmap='summer', xticks=classnames, yticks=classnames, mode='rich')
    plt.show()

