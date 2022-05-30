#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-06 10:38:13
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import os
import pyaibox as pb


seed = 2020
cfgfile = '../../data/files/samples.yaml'

cfg = pb.loadyaml(cfgfile)
print(cfg)

if 'SAR_AF_DATA_PATH' in os.environ.keys():
    datafolder = os.environ['SAR_AF_DATA_PATH']
else:
    datafolder = cfg['SAR_AF_DATA_PATH']


fileTrain = [datafolder + cfg['datafiles'][i] for i in cfg['trainid']]
fileValid = [datafolder + cfg['datafiles'][i] for i in cfg['validid']]
fileTest = [datafolder + cfg['datafiles'][i] for i in cfg['testid']]


X, ca, cr = pb.read_samples(fileTest, keys=[['SI', 'ca', 'cr']], nsamples=[4000], groups=[25], mode='sequentially', axis=0, parts=None, seed=seed)

print(X.shape, ca.shape, cr.shape)
