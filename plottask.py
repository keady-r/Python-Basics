
# importing the required module 
from tkinter import font
from turtle import left
import matplotlib.pyplot as plt
import numpy as np

#Defining fucntions for g(x) and h(x) 
def gfunction(x):
    return x * 2

def hfunction(x):
    return x * 3

# Plot design size, xlabel, y label, title 
fig = plt.figure(1,figsize = (10,10))
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('PANDS Graph task week 8', size=20, color = "blue", fontweight='bold')

#Plot parameters 
plt.xlim([0,11])
plt.ylim([0,4])
plt.minorticks_on()
plt.tick_params(direction = 'in', left = True, top = True)
plt.tick_params (labelsize = 12)
plt.tick_params(direction='in', which ='minor', length = 5, bottom = True)
plt.tick_params(direction='in', which ='major', length = 15, bottom = True)
plt.grid(linestyle = 'dashdot', color = "grey", linewidth = 0.9)
plt.legend()

# x and y plot
x = np.array(range(0,4))
y = np.array(range(0,4))
plt.plot (x, y, label = "f(x)",linestyle ='solid', marker='^', mfc = "pink", markersize = 15, color = "purple", linewidth = 3)

# gfunction plot
x = gfunction(np.array(range(0,4)))
y = np.array(range(0,4))
plt.plot(x, y, linestyle = '-', marker='s',mfc = "yellow", markersize = 15, label = "g(x)", color = "orange", linewidth = 3)

# hfuction plot
x = hfunction(np.array(range(0,4)))
y = np.array(range(0,4))
plt.plot (x, y, linestyle ='dashed', marker='o', mfc = 'blue', markersize = 14, label = "h(x)", color = "green", linewidth = 5)

plt.show()
