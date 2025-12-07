import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Lunch1", "Lunch2", "Dinner1", "Dinner2"])
y = np.array([9.8, 9.5, 9.5, 9.1])

plt.bar(x,y)
plt.show()