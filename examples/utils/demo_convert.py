#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : demo_convert.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Dec 11 2022
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

import pyaibox as pb

s = '[0, [[[[1], 2.], 33], 4], [5, [6, 2.E-3]], 7, [8]], 1e-3'

print(pb.str2list(s))

print(pb.str2num(s, int))
print(pb.str2num(s, float))
print(pb.str2num(s, 'auto'))

print(2**(pb.str2num('int8', int)[0]))
print(pb.str2num('int', int) == [])

print(pb.str2sec('1:00:0'))
print(pb.str2sec('1:10:0'))
print(pb.str2sec('1:10:6'))
print(pb.str2sec('1:10:30'))

n = -123

bs = pb.int2bstr(n, 4, '<', signed=True)
print(bs)
print(hex(n))
print(pb.bstr2int(bs, '<'))

bs = pb.int2bstr(n, 4, '>', signed=True)
print(bs)
print(hex(n))
print(pb.bstr2int(bs, '>'))

print(pb.str2hash('123456ABCDEFG', 'md5'), 'md5')
print(pb.file2hash('deploy.sh', 'md5'), 'md5')
