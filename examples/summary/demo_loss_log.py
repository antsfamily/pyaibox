#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-24 18:29:48
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$


import pyaibox as pb

loslog = pb.LossLog(plotdir='./', xlabel='xlabel', ylabel='ylabel')
loslog = pb.LossLog(plotdir=None, xlabel='Epoch', ylabel='Loss', title=None, filename='LossEpoch', logdict={'train': [], 'valid': []})
for n in range(100):
    loslog.add('train', n)
    loslog.add('valid', n - 1)

loslog.plot()
