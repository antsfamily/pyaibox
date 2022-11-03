#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-23 07:01:55
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import numpy as np
import pyaibox as pb

a = np.random.randn(3, 4)
b = 10
c = [1, 2, 3]
d = {'1': 1, '2': a}
s = 'Hello, the future!'
t = (0, 1)

# pb.savemat('./data.mat', {'a': a, 'b': b, 'c': c, 'd': d, 's': s})
# data = pb.loadmat('./data.mat')
# print(data.keys())

# print("==========")
# pb.saveh5('./data.h5', {'a': a, 'b': b, 'c': c, 'd': d, 's': s})
# data = pb.loadh5('./data.h5', keys=['a', 's'])
# print(data.keys())

# print("==========")
# # saveh5('./data.h5', {'t': t}, 'w')
# pb.saveh5('./data.h5', {'t': t}, 'a')
# pb.saveh5('./data.h5', {'t': (2, 3, 4)}, 'a')
# data = pb.loadh5('./data.h5')

# for k, v in data.items():
#     print(k, v)

x = pb.loadyaml('data/files/demo.yaml', 'trainid')
print(x, type(x))
x = pb.loadjson('data/files/demo.json', 'trainid')
print(x, type(x))

x = pb.loadyaml('data/files/demo.yaml')
print(x, type(x))
# x = pb.loadjson('data/files/demo.json')
# print(x, type(x))

pb.saveyaml('data/files/demo1.yaml', x, indent='  ', mode='a')
x = pb.loadyaml('data/files/demo1.yaml')
print(x, type(x))
