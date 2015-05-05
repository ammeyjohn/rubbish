__author__ = 'yuanjie'


from datetime import date
import pandas as pd
import matplotlib.pyplot as plt


# Read data from csv files
df1 = pd.read_csv('data/series_xc_1.csv', index_col=0, header=0, parse_dates=0)
df2 = pd.read_csv('data/series_xc_2.csv', index_col=0, header=0, parse_dates=0)

# Generate date range from start to end
start_date = date(2014, 5, 1)
end_date = date(2014, 5, 12)
drange = pd.date_range(start_date, end_date, freq='1H', closed='left')

# Slice the sample data from start to end
df1 = df1.reindex(drange)
df1.columns = ['value1']
print df1.head()

df2 = df2.reindex(drange)
df2.columns = ['value2']
print df2.head()

# Combine df1 and df2
df = df1.join(df2)
print df.head()

# DEBUG: print plot
df.plot()
plt.show()