#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : normalsignals.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Nov 11 2019
# @version   : 0.0
# @license   : The Apache License 2.0
# @note      : 
# 
# The Apache 2.0 License
# Copyright (C) 2013- Zhi Liu
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#

import numpy as np
from pyaibox.utils.const import *


def hs(x):
    r"""
    Heavyside function :
    .. math::
        hv(x) = {1, if x>=0; 0, otherwise}
    """
    return 0.5 * (np.sign(x) + 1.0)


def ihs(x):
    r"""
    Inverse Heavyside function:
    .. math::
        ihv(x) = {0, if x>=0; 1, otherwise}
    """
    # print(x)
    # print(np.sign(x))
    return 0.5 * (1.0 - np.sign(x))


def rect(x):
    r"""
    Rectangle function:
    .. math::
        rect(x) = {1, if |x|<= 0.5; 0, otherwise}
    """
    # return hs(x + 0.5) * ihs(x - 0.5)
    return np.where(np.abs(x) > 0.5, 0., 1.0)


def chirp(t, T, Kr):
    r"""
    Create a chirp signal:
    .. math::
        S_{tx}(t) = rect(t/T) * exp(1j*pi*Kr*t^2)
    """
    return rect(t / T) * np.exp(1j * np.pi * Kr * t**2)

if __name__ == '__main__':

    import matplotlib.pyplot as plt

    Ns = 1000
    t = np.linspace(-1, 1, Ns)
    yrect = rect(t)

    plt.figure()
    plt.plot(t, yrect, '-r', linewidth=2)
    plt.axis([-1, 1, -0.1, 1.1])
    plt.grid()
    plt.xlabel('Time/s')
    plt.ylabel('Amplitude')
    plt.title('rect')
    plt.show()

    Kr1 = 10
    Kr2 = 20
    T1 = 2.0
    T2 = 4.0
    t = np.linspace(-3, 3, Ns)
    ychirp1 = chirp(t, T1, Kr=Kr1)
    ychirp2 = chirp(t, T2, Kr=Kr1)

    ychirp3 = chirp(t, T1, Kr=Kr2)
    ychirp4 = chirp(t, T2, Kr=Kr2)

    plt.figure()
    plt.subplot(221)
    plt.grid()
    plt.plot(t, ychirp1, '-r')
    plt.xlabel('Time/s')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T1) + "s, K=" + str(Kr1) + "Hz/s")
    plt.subplot(222)
    plt.grid()
    plt.plot(t, ychirp2, '-b')
    plt.xlabel('Time/s')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T2) + "s, K=" + str(Kr2) + "Hz/s")
    plt.subplot(223)
    plt.grid()
    plt.plot(t, ychirp3, '-r')
    plt.xlabel('Time/s')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T1) + "s, K=" + str(Kr1) + "Hz/s")
    plt.subplot(224)
    plt.grid()
    plt.plot(t, ychirp4, '-b')
    plt.xlabel('Time/s')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T2) + "s, K=" + str(Kr2) + "Hz/s")
    plt.show()

    # ==================compute spectral

    ychirp1_fft = np.fft.fft(ychirp1)
    ychirp2_fft = np.fft.fft(ychirp2)
    ychirp3_fft = np.fft.fft(ychirp3)
    ychirp4_fft = np.fft.fft(ychirp4)
    f = np.fft.fftfreq(t.shape[-1])
    ychirp1_fft = np.fft.fftshift(ychirp1_fft)
    ychirp2_fft = np.fft.fftshift(ychirp2_fft)
    ychirp3_fft = np.fft.fftshift(ychirp3_fft)
    ychirp4_fft = np.fft.fftshift(ychirp4_fft)
    f = np.fft.fftshift(np.fft.fftfreq(t.shape[-1]))

    plt.figure()
    plt.subplot(221)
    plt.grid()
    plt.plot(f, np.abs(ychirp1_fft), '-r')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T1) + "s, K=" + str(Kr1) + "Hz/s")
    plt.subplot(222)
    plt.grid()
    plt.plot(f, np.abs(ychirp2_fft), '-b')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T2) + "s, K=" + str(Kr2) + "Hz/s")
    plt.subplot(223)
    plt.grid()
    plt.plot(f, np.abs(ychirp3_fft), '-r')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T1) + "s, K=" + str(Kr1) + "Hz/s")
    plt.subplot(224)
    plt.grid()
    plt.plot(f, np.abs(ychirp4_fft), '-b')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T2) + "s, K=" + str(Kr2) + "Hz/s")
    plt.show()

    plt.figure()
    plt.subplot(221)
    plt.grid()
    plt.plot(f, np.angle(ychirp1_fft), '-r')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T1) + "s, K=" + str(Kr1) + "Hz/s")
    plt.subplot(222)
    plt.grid()
    plt.plot(f, np.angle(ychirp2_fft), '-b')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T2) + "s, K=" + str(Kr2) + "Hz/s")
    plt.subplot(223)
    plt.grid()
    plt.plot(f, np.angle(ychirp3_fft), '-r')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T1) + "s, K=" + str(Kr1) + "Hz/s")
    plt.subplot(224)
    plt.grid()
    plt.plot(f, np.angle(ychirp4_fft), '-b')
    plt.xlabel('Frequency/Hz')
    plt.ylabel('Amplitude')
    plt.title("T=" + str(T2) + "s, K=" + str(Kr2) + "Hz/s")
    plt.show()
