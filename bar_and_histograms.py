import matplotlib.pyplot as plt


# x = [1, 3, 5, 7, 9]
# y = [2, 4, 6, 3, 5]

# x2 = [2, 4, 6, 8, 10]
# y2 = [2, 7, 9, 8, 6]

# plt.bar(x, y, label='First Bar', color='r')
# plt.bar(x2, y2, label='Second Bar', color='b')

# plt.xlabel('x')
# plt.ylabel('y - f(x)')
# plt.title('Interesting Graph')

# plt.legend()

# plt.show()



# population_ages = [22, 67, 92, 11,23, 43, 76, 23, 22, 38, 25, 76, 43, 9, 29, 27, 21]
# ids = [ i for i, v in enumerate(population_ages) ]

# plt.bar(ids, population_ages)
# plt.show()


population_ages = [22, 67, 92, 11,23, 43, 76, 23, 22, 38, 25, 76, 43, 9, 29, 27, 21]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.show()
