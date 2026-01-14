
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Red','Green','Blue','Yellow'])
y = np.array([60,80,87,91])


plt.title("Semester Result")
plt.xlabel("House")
plt.ylabel("Percentage (%)")

plt.bar(x,y,width = 0.5)

plt.show()