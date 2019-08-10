import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [2, 4, 6]

x2 = [2, 3, 4]
y2 = [2, 7, 9]

# 
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

# 
plt.xlabel('x')
plt.ylabel('y - f(x)')
plt.title('Interesting Graph')
plt.title('Interesting Graph\nsubtitle')

# legend with the label
plt.legend()

#
plt.show()