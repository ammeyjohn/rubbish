__author__ = 'yuanjie'

from datetime import date
import pandas as pd


def load_sample(start_date, end_date, exp=2):

    # Read data from csv files
    df1 = pd.read_csv('data/series_xc_1.csv', index_col=0, header=0, parse_dates=0)
    df2 = pd.read_csv('data/series_xc_2.csv', index_col=0, header=0, parse_dates=0)

    # Generate date range from start to end
    drange = pd.date_range(start_date, end_date, freq='1H', closed='left')

    # Slice the sample data from start to end
    df1 = df1.reindex(drange)
    df1.columns = ['value1']
    print "==========Series 1=========="
    print df1.head()

    df2 = df2.reindex(drange)
    df2.columns = ['value2']
    print "==========Series 2=========="
    print df2.head()

    # Combine df1 and df2
    df = df1.join(df2)

    # Calculate the sum of the every column
    df = df.assign(
        Target=lambda t: t.value1 + t.value2
    )
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    df.index.names = ['date']
    print "==========Demand data=========="
    print df.head()

    # Load weather date
    wh = pd.read_csv('data/weather_suzhou.csv', index_col=0, header=0, parse_dates=0)

    # Slice the weather data from start to end
    wh = wh.resample('1H')
    print "==========Weather=========="
    print wh.head()

    # Combine df and wh
    df = df.join(wh[['TemperatureC', 'Humidity']])
    print "==========Sample Data with weather=========="
    print df.head()

    # Generate the exp
    cols = df.columns.size
    for e in range(2, exp+1):
        for j in range(1, cols):
            newcol = df[df.columns[j]] ** e
            df = df.join(newcol, rsuffix=str(exp))
    print "==========Input data=========="
    print df.head()

    # Normalize
    for col_name in df.columns:
        print 'Normalizing the column %s ...' % col_name
        col_min = df[col_name].min()
        col_std = df[col_name].std()
        df[col_name] = (df[col_name] - col_min) / col_std

    # Fill all nan
    df.fillna(method='bfill', inplace=True)

    return df
