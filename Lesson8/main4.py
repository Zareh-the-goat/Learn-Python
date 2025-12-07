import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 300)   # 300 points between -10 and 10
y = 2.5*x + 160
plt.plot(x,y)
plt.title("")
plt.ylabel("y")
plt.xlabel("x")
plt.grid()
plt.show()