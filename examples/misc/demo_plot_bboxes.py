#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-06 09:32:16
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import pyaibox as pb
import matplotlib.pyplot as plt

bboxes = [[100, 100, 200, 200], [300, 300, 400, 500]]
labels = ['dog', 'cat']
scores = [0.987, None]
edgecolors = [list(pb.DISTINCT_COLORS_RGB_NORM.values())[0], None]
edgecolors = list(pb.DISTINCT_COLORS_RGB_NORM.values())[0:2]
linewidths = [2, 4]

fontdict = {'family': 'Times New Roman',
            'style': 'italic',
            'weight': 'normal',
            'color': 'darkred',
            'size': 12,
            }

x = pb.imread('../../data/images/oi/LenaRGB512.tif')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.imshow(x)

pb.plot_bbox(bboxes, labels=labels, scores=scores, edgecolors=edgecolors, linewidths=linewidths, fontdict=fontdict, textpos='TopLeft', ax=ax)
plt.axis('off')
plt.savefig('./bbbox.png', bbox_inches='tight', pad_inches=0)
plt.show()
