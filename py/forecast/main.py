__author__ = 'yuanjie'


from datetime import date
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':

    start_date = date(2013, 5, 1)
    end_date = date(2013, 6, 1)

    # Read data from csv files
    df1 = pd.read_csv('data/series_xc_1.csv', index_col=[0], parse_dates=[0])
    df2 = pd.read_csv('data/series_xc_2.csv', index_col=[0], parse_dates=[0])

    df1.head()

    # Create date ranges
    drange = pd.date_range(start=start_date, end=end_date, freq='2min', closed='left')

    # Combine all data columns index with date
    df = df1.reindex(drange)
    df.head()
    df = df.merge(df2.reindex(drange))

    # DEBUG: head
    df.head()

    # Draw plot
    df.plot()
    plt.show()

    pass