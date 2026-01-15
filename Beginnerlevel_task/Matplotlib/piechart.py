
import matplotlib.pyplot as plt
import numpy as np

x = np.array([20,30,40,10])
mylabels = ['Blue','Orange','Green','Red']
myexplode = [0.2, 0, 0, 0]

plt.pie(x, labels = mylabels, explode = myexplode, shadow = True)

plt.legend(title = "Color:")

plt.show()
