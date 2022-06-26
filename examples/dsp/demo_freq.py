import numpy as np
import pyaibox as pb

n = 10
print(np.fft.fftfreq(n, d=0.1), 'numpy')
print(pb.fftfreq(n, fs=10., norm=False), 'fftfreq, norm=False, shift=False')
print(pb.fftfreq(n, fs=10., norm=True), 'fftfreq, norm=True, shift=False')
print(pb.fftfreq(n, fs=10., shift=True), 'fftfreq, norm=False, shift=True')
print(pb.freq(n, fs=10., norm=False), 'freq, norm=False, shift=False')
print(pb.freq(n, fs=10., norm=True), 'freq, norm=True, shift=False')
print(pb.freq(n, fs=10., shift=True), 'freq, norm=False, shift=True')

print('-------------------')

n = 11
print(np.fft.fftfreq(n, d=0.1), 'numpy')
print(pb.fftfreq(n, fs=10., norm=False), 'fftfreq, norm=False, shift=False')
print(pb.fftfreq(n, fs=10., norm=True), 'fftfreq, norm=True, shift=False')
print(pb.fftfreq(n, fs=10., shift=True), 'fftfreq, norm=False, shift=True')
print(pb.freq(n, fs=10., norm=False), 'freq, norm=False, shift=False')
print(pb.freq(n, fs=10., norm=True), 'freq, norm=True, shift=False')
print(pb.freq(n, fs=10., shift=True), 'freq, norm=False, shift=True')
