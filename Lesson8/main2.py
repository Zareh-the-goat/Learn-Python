import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')

plt.title("Basketball Game")
plt.ylabel("Amount of point")
plt.xlabel("Minutes")
plt.show()


