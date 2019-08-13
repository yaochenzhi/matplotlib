import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 7, 10, 9]
eating =   [2, 3, 4, 3, 2]
working =  [7, 8, 7, 8, 7]
playing =  [8, 5, 6, 3, 6]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['m', 'c', 'r', 'g']



plt.pie(slices, 
        labels=activities, 
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%',
        )

plt.title('This is a Pie Chart')
plt.show()