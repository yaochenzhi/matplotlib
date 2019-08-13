import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 7, 10, 9]
eating =   [2, 3, 4, 3, 2]
working =  [7, 8, 7, 8, 7]
playing =  [8, 5, 6, 3, 6]


plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

# Fake lables for stackplot
plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)
plt.legend()

plt.show()