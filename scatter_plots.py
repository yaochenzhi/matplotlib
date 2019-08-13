import matplotlib.pyplot as plt


x = list(range(1, 10))
y = [2, 5, 1, 3, 1, 4, 3, 3, 5]

plt.scatter(x, y, label='skitscat', color='k', marker='*', s=50)

plt.show()