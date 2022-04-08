
# importing the required module - (1.)
from tkinter import font
from turtle import left
import matplotlib.pyplot as plt
import numpy as np

#Defining fucntions for g(x) and h(x) - (1.)
def gfunction(x):
    return x * 2

def hfunction(x):
    return x * 3

# Plot design size, xlabel, y label, title (3.)
fig = plt.figure(1,figsize = (10,10))
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('PANDS Graph task week 8', size=20, color = "blue", fontweight='bold')

#Plot parameters (1. 3. 4. )
plt.xlim([0,11])
plt.ylim([0,4])
plt.minorticks_on()
plt.tick_params(direction = 'in', left = True, top = True)
plt.tick_params (labelsize = 12)
plt.tick_params(direction='in', which ='minor', length = 5, bottom = True)
plt.tick_params(direction='in', which ='major', length = 15, bottom = True)
plt.grid(linestyle = 'dashdot', color = "grey", linewidth = 0.9)
plt.legend()

    # plotting the points for f(x) - (1.2. )
x = np.array(range(0,4))
y = np.array(range(0,4))

    #Designing the plot - datapoints,linetype, marker icon, marker face color, markersize, label, line color. - (3. )

plt.plot (x, y, label = "f(x)",linestyle ='solid', marker='^', mfc = "pink", markersize = 15, color = "purple", linewidth = 3)

        # plotting the points for g(x) - (1.2.)
x = gfunction(np.array(range(0,4)))
y = np.array(range(0,4))

        #Designing the plot - datapoints,linetype, marker icon, marker face color, markersize, label, line color. - (3. )

plt.plot(x, y, linestyle = '-', marker='s',mfc = "yellow", markersize = 15, label = "g(x)", color = "orange", linewidth = 3)

             # plotting the points for h(x) - (1.2. )
x = hfunction(np.array(range(0,4)))
y = np.array(range(0,4))

             #Designing the plot - datapoints,linetype, marker icon, marker face color, markersize, label, line color. - (3.5 )
plt.plot (x, y, linestyle ='dashed', marker='o', mfc = 'blue', markersize = 14, label = "h(x)", color = "green", linewidth = 5)

 
# function to show the plot - (1.)
plt.show()

#END

#References:
#1. - Lecture notes 
#2. - W3 Schools "compare plots" https://www.w3schools.com/python/matplotlib_scatter.asp
#3. - Youtube "Python to make a nice figure. Part III: advanced plots" https://www.youtube.com/watch?v=fwZahTYfyxA. 
#4. - W3 Schoool Matplotlib Adding Grid LInes : https://www.w3schools.com/python/matplotlib_grid.asp
#5. - MatPlotLib "Line styles": https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/linestyles.html#:~:text=Simple%20linestyles%20can%20be%20defined,15pt%20space)%20with%20no%20offset.
#6 - MatPlotLib "Marker references" : https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/marker_reference.html

