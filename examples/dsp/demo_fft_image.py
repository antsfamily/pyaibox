import numpy as np
import pyaibox as pb
import matplotlib.pyplot as plt

ftshift = False
# ftshift = True

X = pb.imread('../../data/images/Einstein256.png')
X = X + 1j * X

Y1 = np.fft.fft(X, axis=0)
Y1 = np.fft.fft(Y1, axis=1)
# Y1 = np.fft.fft(np.fft.fft(X, axis=0), axis=1)
Y1 = np.abs(Y1)

Y2 = pb.fft(X, axis=0, shift=ftshift)
Y2 = pb.fft(Y2, axis=1, shift=ftshift)
Y2 = np.abs(Y2)

print(np.sum(Y1 - Y2))
Y1 = np.log10(Y1)
Y2 = np.log10(Y2)

plt.figure()
plt.subplot(131)
plt.imshow(np.abs(X))
plt.subplot(132)
plt.imshow(Y1)
plt.subplot(133)
plt.imshow(Y2)
plt.show()
