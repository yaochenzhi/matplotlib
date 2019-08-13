import matplotlib.pyplot as plt
import csv


'''
x = []
y= []

with open("example.txt") as csvfile:
    plot_rows = csv.reader(csvfile, delimiter=',')
    for row in plot_rows:
        x.append(row[0])
        y.append(row[1])

plt.plot(x, y, label="Loaded from file via csv.reader")
'''

import numpy as np
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x, y, label="Loaded from file via np.loadtxt")
plt.show()