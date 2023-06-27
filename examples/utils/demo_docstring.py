#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : demo_docstring.py
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


# pkgdir = '/home/liu/test/'
pkgdir = '/mnt/e/ws/github/antsfamily/torchcs/torchcs/torchcs/'
pkgdir = '/mnt/e/ws/github/antsfamily/torchtsa/torchtsa/torchtsa/'
pkgdir = '/mnt/e/ws/github/antsfamily/torchbox/torchbox/torchbox/'
pkgdir = '/mnt/e/ws/github/antsfamily/torchsar/torchsar/torchsar/'
pkgdir = '/mnt/e/ws/github/antsfamily/pyaibox/pyaibox/pyaibox/'
# pkgdir = '/mnt/e/ws/github/antsfamily/torchsar/torchsar_deploy/torchsar/'

pb.rmcache(pkgdir, exts='.c')
pb.rmcache(pkgdir, exts='.so')
pb.gpyi(pkgdir, autoskip=True)



