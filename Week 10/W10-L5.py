# Introduction to Matplotlib Library

# Used for data visualization

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9])
y = np.array([99,86,87,111,86,103,87,94,78,77,85,86])

#plt.scatter(x,y)
#plt.show()

#plt.bar(x,y)
#plt.show()

# -------------------------------------------
# Histogram
x = np.random.normal(170,10,250)

plt.hist(x)
plt.show()

#--------------------------------------------
#Pie chart

y = np.array([35,25,25,15])
mylabels = ["Apples", "Bananas","Cherries","Dates"]
plt.pie(y,labels = mylabels, startangle = 90)
plt.show()

# -------------------------------------------
# Subplot

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,1)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,2)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,3)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,4)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,5)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()
