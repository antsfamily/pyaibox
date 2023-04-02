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
import matplotlib.pyplot as plt
from pyaibox.utils.convert import str2num
from pyaibox.utils.colors import DISTINCT_COLORS_HEX
from pyaibox.ml.reduction_pca import pca


def visds(x, y=None, labelmap=None, axisn=0, mode='bar(nms)', **kwargs):
    discolors = list(DISTINCT_COLORS_HEX.keys())


    if y is None:
        pass

    else:
        xshape = x.shape
        nsample = len(y)
        key = np.unique(y)
        nclass = len(key)
        value = np.array(range(nclass))
        label = dict(zip(key, value))
        color = discolors[0:nclass] if nclass < len(discolors) else None
        if type(labelmap) is dict:
            labelname = [labelmap[k] for k in key]
        elif labelmap is None:
            labelname = key
        else:
            labelname = labelmap

        axis = list(range(np.ndim(x))); axis.pop(axisn); axis = tuple(axis)
        means_eachsample = np.mean(x, axis=axis)
        stds_eachsample = np.std(x, axis=axis)
        means_eachclass = np.zeros((nclass,))
        stds_eachclass = np.zeros((nclass,))
        ns_eachclass = np.zeros((nclass,), dtype=np.int32)
        for n in range(nsample):
            ns_eachclass[label[y[n]]] += 1
            means_eachclass[label[y[n]]] += means_eachsample[n]
            stds_eachclass[label[y[n]]] += stds_eachsample[n]

        means_eachclass /= ns_eachclass
        stds_eachclass /= ns_eachclass

        if mode == 'bar(nms)':
            plt.figure(**kwargs)
            plt.grid()
            plt.bar(key, ns_eachclass)
            plt.xticks(key, labelname)
            plt.xlabel('Class')
            plt.ylabel('The number of samples')

            plt.figure(**kwargs)
            plt.grid()
            plt.bar(key, means_eachclass)
            plt.xticks(key, labelname)
            plt.xlabel('Class')
            plt.ylabel('Mean of feature')

            plt.figure(**kwargs)
            plt.grid()
            plt.bar(key, stds_eachclass)
            plt.xticks(key, labelname)
            plt.xlabel('Class')
            plt.ylabel('Standard deviation')
            plt.show()

        if mode == 'scatter(ms)':
            plt.figure(**kwargs)
            plt.grid()
            for i, k in enumerate(key):
                plt.scatter(means_eachsample[y==k], stds_eachsample[y==k], color=color[i], marker='.', alpha=0.2)
            scatters = []
            for i, k in enumerate(key):
                scatter = plt.scatter(means_eachclass[label[k]], stds_eachclass[label[k]], s=200, color=color[i], marker='^', edgecolors='k')
                scatters.append(scatter)
            plt.legend(scatters, labelname)
            plt.xlabel('Mean')
            plt.ylabel('Standard deviation')
            plt.show()

        # if ('pca' in mode.lower()) and ('scatter' in mode.lower()):
        #     ncmpnts = str2num(mode, vfn=int)
        #     ncmpnts = 2 if ncmpnts == [] else ncmpnts[0]
        #     xshape = x.shape
        #     N = xshape[axisn]
        #     if axisn != 0:
        #         x = x.transpose(0, axisn)
        #     x = np.reshape(x, (N, -1))
        #     N, M = x.shape
        #     fig = plt.figure(**kwargs)
        #     ax = fig.add_subplot(projection='3d' if ncmpnts == 3 else None)
        #     for i, k in enumerate(key):
        #         xi = x[y==k, :]
        #         U, S = pca(xi, axisn=0, ncmpnts=ncmpnts, algo='svd')
        #         U = U[:, :ncmpnts]
        #         xi = xi @ U  # N-k
        #         xi = tuple([xi[:, i] for i in range(ncmpnts)])
                
        #         ax.scatter(*xi, c=color[i])
        #     plt.grid()

        #     plt.legend(key)
        #     ax.set_xlabel('Component 1')
        #     ax.set_ylabel('Component 2')
        #     if ncmpnts == 3:
        #         ax.set_zlabel('Component 3')
        #     plt.show()

        if ('pca' in mode.lower()) and ('scatter' in mode.lower()):
            ncmpnts = str2num(mode, vfn=int)
            ncmpnts = 2 if ncmpnts == [] else ncmpnts[0]
            xshape = x.shape
            N = xshape[axisn]
            if axisn != 0:
                x = x.transpose(0, axisn)
            x = np.reshape(x, (N, -1))
            N, M = x.shape
            U, S = pca(x, axisn=0, ncmpnts=ncmpnts, algo='svd')
            
            U = U[:, :ncmpnts]
            x = x @ U  # N-k
            fig = plt.figure(**kwargs)
            ax = fig.add_subplot(projection='3d' if ncmpnts == 3 else None)
            for i, k in enumerate(key):
                xi = tuple([x[y==k, i] for i in range(ncmpnts)])
                ax.scatter(*xi, c=color[i])
            plt.grid()

            plt.legend(labelname)
            ax.set_xlabel('Component 1')
            ax.set_ylabel('Component 2')
            if ncmpnts == 3:
                ax.set_zlabel('Component 3')
            plt.show()
        
if __name__ == '__main__':

    import pyaibox as pb
    rootdir = '/mnt/d/DataSets/oi/dgi/mnist/official/'

    dataset = 'test'
    X, Y = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
    print(X.shape, Y.shape)

    # X = pb.standardization(X, axis=(1, 2))

    visds(x=X, y=Y, label=None, mode='bar(nms)')
    visds(x=X, y=Y, label=None, mode='scatter(ms)')
    visds(x=X, y=Y, label=None, mode='scatter(pca2)')
    visds(x=X, y=Y, label=None, mode='scatter(pca3)')
