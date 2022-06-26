#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-06 10:38:13
# @Author  : Yan Liu & Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$

import numpy as np
import pyaibox as pb
import matplotlib.pyplot as plt

shift = True
frq = [10, 10]
amp = [0.8, 0.6]
Fs = 80
Ts = 2.
Ns = int(Fs * Ts)

t = np.linspace(-Ts / 2., Ts / 2., Ns).reshape(Ns, 1)
f = pb.freq(Ns, Fs, shift=shift)
f = pb.fftfreq(Ns, Fs, norm=False, shift=shift)

# ---complex vector in real representation format
x = amp[0] * np.cos(2. * np.pi * frq[0] * t) + 1j * amp[1] * np.sin(2. * np.pi * frq[1] * t)

# ---do fft
Xc = pb.fft(x, n=Ns, caxis=None, axis=0, keepcaxis=False, shift=shift)

# ~~~get real and imaginary part
xreal = pb.real(x, caxis=None, keepcaxis=False)
ximag = pb.imag(x, caxis=None, keepcaxis=False)
Xreal = pb.real(Xc, caxis=None, keepcaxis=False)
Ximag = pb.imag(Xc, caxis=None, keepcaxis=False)

# ---do ifft
x̂ = pb.ifft(Xc, n=Ns, caxis=None, axis=0, keepcaxis=False, shift=shift)
 
# ~~~get real and imaginary part
x̂real = pb.real(x̂, caxis=None, keepcaxis=False)
x̂imag = pb.imag(x̂, caxis=None, keepcaxis=False)

plt.figure()
plt.subplot(131)
plt.grid()
plt.plot(t, xreal)
plt.plot(t, ximag)
plt.legend(['real', 'imag'])
plt.title('signal in time domain')
plt.subplot(132)
plt.grid()
plt.plot(f, Xreal)
plt.plot(f, Ximag)
plt.legend(['real', 'imag'])
plt.title('signal in frequency domain')
plt.subplot(133)
plt.grid()
plt.plot(t, x̂real)
plt.plot(t, x̂imag)
plt.legend(['real', 'imag'])
plt.title('reconstructed signal')
plt.show()

# ---complex vector in real representation format
x = pb.c2r(x, caxis=-1)

# ---do fft
Xc = pb.fft(x, n=Ns, caxis=-1, axis=0, keepcaxis=False, shift=shift)

# ~~~get real and imaginary part
xreal = pb.real(x, caxis=-1, keepcaxis=False)
ximag = pb.imag(x, caxis=-1, keepcaxis=False)
Xreal = pb.real(Xc, caxis=-1, keepcaxis=False)
Ximag = pb.imag(Xc, caxis=-1, keepcaxis=False)

# ---do ifft
x̂ = pb.ifft(Xc, n=Ns, caxis=-1, axis=0, keepcaxis=False, shift=shift)
 
# ~~~get real and imaginary part
x̂real = pb.real(x̂, caxis=-1, keepcaxis=False)
x̂imag = pb.imag(x̂, caxis=-1, keepcaxis=False)

plt.figure()
plt.subplot(131)
plt.grid()
plt.plot(t, xreal)
plt.plot(t, ximag)
plt.legend(['real', 'imag'])
plt.title('signal in time domain')
plt.subplot(132)
plt.grid()
plt.plot(f, Xreal)
plt.plot(f, Ximag)
plt.legend(['real', 'imag'])
plt.title('signal in frequency domain')
plt.subplot(133)
plt.grid()
plt.plot(t, x̂real)
plt.plot(t, x̂imag)
plt.legend(['real', 'imag'])
plt.title('reconstructed signal')
plt.show()
