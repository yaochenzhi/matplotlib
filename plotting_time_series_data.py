import pandas as pd 
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


# plt.style.use('seaborn')

# dates = [
#     datetime(2019, 8, 1),
#     datetime(2019, 8, 2),
#     datetime(2019, 8, 3),
#     datetime(2019, 8, 4),
#     datetime(2019, 8, 5),
#     datetime(2019, 8, 6),
#     datetime(2019, 8, 7),
# ]

# y = [0, 1, 5, 3, 7, 6, 8 ]

# plt.plot_date(dates, y, linestyle='solid')

# plt.gcf().autofmt_xdate()

# date_format = mpl_dates.DateFormatter('%b, %d %Y')
# plt.gca().xaxis.set_major_formatter(date_format)

# plt.show()


plt.style.use('seaborn')

data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, ;linestyle='solid')
plt.gcf().autofmt_xdate()

plt.title()
plt.xlabel()
plt.ylabel()

plt.show()