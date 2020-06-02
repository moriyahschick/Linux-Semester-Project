#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random
import math
import numpy as np

# create a figure instance that will later be written to a PDF
f = plt.figure()

index = np.arange(1300)

# figue out how many numbers will be plotted
fopen = open("calculateSlopes.txt")
slopes = fopen.readlines()
fopen.close()
N = len(slopes)

#WRAP IN FLOAT
x = [float(show.split("|")[1]) for show in slopes]    #slope1 - before show
y = [float(show.split("|")[2].replace("\n", "")) for show in slopes]    #slope2 - during show

print("X: ", len(x))
print("Y: ", len(y))
#print("Min of x: ", min(x))
#print("Max of x: ", max(x))
#print("Min of y: ", min(y))                                                                                                              
#print("Max of y: ", max(y))

#Min of x:  -0.00000001
#Max of x:  0.00075265
#Min of y:  -0.00000000
#Max of y:  0.00087997

#plt.xlim(-0.0010, 0.0010)
#plt.ylim(-0.0010, 0.0010)
# make a list of 20 random colors
colors = [random.random() for i in range(N)]

# make a list of same sized circles
areas = [1 for i in range(N)]

# do the scatter plot, with specified colors and sizes
plt.scatter(x, y, c = colors, s = areas, alpha = 0.5)

plt.xlim(-0.0001, 0.0001)    #0.0010 old
plt.ylim(-0.0001, 0.0001)
# specify the x and y axis labels
plt.xlabel("s1 - slope of name before show")
plt.ylabel("s2 - slope of name during show")

#plt.show()

# Save the plot into a PDF file
f.savefig("small_plot.pdf")
