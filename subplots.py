import pandas as pd
from matplotlib import pyplot as plt


# plt.style.use('seaborn')

# data = pd.read_csv('data.csv')
# ages = data['Ages']
# dev_salaries = data['All_devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']


# plt.plot(ages, py_salaries, label='')
# plt.plot(ages, js_salaries, label='')

# plt.plot(ages, dev_salaries, color='#444444',
#          linestyple='--', label='All devs')

# plt.legend()
# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')

# plt.tight_layout()
# plt.show()



fig, ax = plt.subplots()
fig, (ax1, ax2) = plt.subplots()
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=2, sharex=True)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot()
ax2.plot()

ax1.legend()

ax1.set_title()
ax1.set_xlabel()
ax1.set_ylabel()

ax2.set_title()
ax2.set_xlabel()
ax2.set_ylabel()

plt.tight_layout()
plt.show()

fig1.savefig('fig1.png')
fig2.savefig('fig2.png')