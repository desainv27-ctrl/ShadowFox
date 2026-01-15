
import matplotlib.pyplot as plt
import numpy as np

x = np.array([101,102,103,104,105,106])
y = np.array([67,89,65,55,99,45])

plt.scatter(x,y,color ="red")

font1 = {'family': 'serif','color': 'black' ,'size':20}
font2 = {'family': 'serif','color': 'black' ,'size':10}

plt.title("Result",fontdict = font1)
plt.xlabel("SerialNo",fontdict = font2)
plt.ylabel("Marks")

plt.show()


