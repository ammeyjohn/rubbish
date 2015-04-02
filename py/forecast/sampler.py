__author__ = 'yuanjie'

import os
import pandas as pd


def load_csv(file_name):
    """Load sample file as Series from csv file.
    :rtype : object
    :param file_name: The csv file name.
    :return: Returns the Series object contains the csv data.
    """
    if not os.path.exists(file_name):
        print 'File "%s" does not exist.' % file_name
        return

    return pd.Series.from_csv(file_name, index_col=0, header=0)