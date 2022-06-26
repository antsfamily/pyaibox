#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-06-13 22:38:13
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import pyaibox as pb

datafolder = pb.data_path('optical')
xr = pb.imread(datafolder + 'Einstein256.png')
xi = pb.imread(datafolder + 'LenaGRAY256.png')

x = xr + 1j * xi
print(x.shape)

xnp15, np15 = pb.awgns(x, snrv=15, extra=True)
xn0, n0 = pb.awgns(x, snrv=0, extra=True)
xnn5, nn5 = pb.awgns(x, snrv=-5, extra=True)

print(pb.snr(x, np15))
print(pb.snr(x, n0))
print(pb.snr(x, nn5))

x = pb.abs(x)
xnp15 = pb.abs(xnp15)
xn0 = pb.abs(xn0)
xnn5 = pb.abs(xnn5)

plt = pb.imshow([x, xnp15, xn0, xnn5], titles=['original', 'noised(15dB)', 'noised(0dB)', 'noised(-5dB)'])
plt.show()


datafolder = pb.data_path('optical')
xr = pb.imread(datafolder + 'Einstein256.png')
xi = pb.imread(datafolder + 'LenaGRAY256.png')

x = xr + 1j * xi
x = pb.c2r(x, cdim=-1)
print(x.shape)

xnp15, np15 = pb.awgns2(x, snrv=15, cdim=-1, dim=(0, 1), extra=True)
xn0, n0 = pb.awgns2(x, snrv=0, cdim=-1, dim=(0, 1), extra=True)
xnn5, nn5 = pb.awgns2(x, snrv=-5, cdim=-1, dim=(0, 1), extra=True)

print(pb.snr(x, np15, cdim=-1, dim=(0, 1)))
print(pb.snr(x, n0, cdim=-1, dim=(0, 1)))
print(pb.snr(x, nn5, cdim=-1, dim=(0, 1)))

x = pb.abs(x, cdim=-1)
xnp15 = pb.abs(xnp15, cdim=-1)
xn0 = pb.abs(xn0, cdim=-1)
xnn5 = pb.abs(xnn5, cdim=-1)

plt = pb.imshow([x, xnp15, xn0, xnn5], titles=['original', 'noised(15dB)', 'noised(0dB)', 'noised(-5dB)'])
plt.show()
