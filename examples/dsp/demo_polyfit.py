import numpy as np
import pyaibox as pb
import matplotlib.pyplot as plt

Ns, k, b = 100, 6.2, 3.0
x = np.linspace(0, 1, Ns)
y = x * k + b + np.random.randn(Ns)
# x, y = x.to('cuda:1'), y.to('cuda:1')

deg = 1
deg = 2
# deg = (2, 2)

w = pb.polyfit(x, y, deg=deg)
print(w)
w = pb.polyfit(x, y, deg=deg, C=5)
print(w)
yy = pb.polyval(w, x, deg=deg)
print(yy)

print(np.sum(np.abs(y - yy)))

plt.figure()
plt.plot(x, y, 'ob')
plt.plot(x, yy, '-r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('polynomial fitting')
plt.legend(['noised data', 'fitted'])
plt.show()
