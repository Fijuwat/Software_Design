import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,100)
y1 = float(100)**1.4 * (4**float(100))
y2 = 100**200 * 3.99**100
print(y1, y2)
plt.plot(x, y1, '-r', label='f1 = (2^10)(x) + 2^10')
plt.plot(x, y2, '-b', label='f2 = (x^3.5) - 1000')
plt.title('Graph of f1, f2, f3')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')


plt.grid()
plt.show()