__author__ = 'patrick'


from datetime import date, datetime, timedelta
from dateutil import parser
from io import StringIO
import urllib2
import pandas as pd


# Defines the global const value
ROOT_DOMAIN = 'http://www.wunderground.com'
PART_DOMAIN = '/history/station'


def get_url(code, date):
    """Generate the url for weather downloading.
    :param code: The code of weather station.
    :param date: The date string of weather to download.
    :return: Returns the url which point to the weather download page.
    """

    url = ROOT_DOMAIN + PART_DOMAIN
    url += '/%s' % code
    url += '/%d/%d/%d' % (date.year, date.month, date.day)
    url += '/DailyHistory.html?format=1'
    return url


def download(url):
    """Download html from given url
    :param url: The url of the page to download.
    :return: Returns the html string.
    """

    req = urllib2.Request(url)
    return urllib2.urlopen(req).read()


if __name__ == '__main__':

    df = None

    code = 'zsss'           # The code of weather station
    sdate = parser.parse('2013-09-01')    # Start date
    edate = parser.parse('2013-09-30')    # End date
    cdate = sdate           # Current date

    url_str = get_url(code, cdate)
    print 'Downloading from %s' % url_str

    html_str = download(url_str)
    html_str = html_str.strip()
    html_str = html_str.replace('<br />', '')
    print html_str

    # Create the DateFrame from csv string wrapped by StringIO
    io_html = StringIO(unicode(html_str))
    df0 = pd.DataFrame.from_csv(io_html)

    # Arrange the weather data
    st_today = date.today()
    ed_today = st_today + timedelta(days=1)
    rng1 = pd.date_range(start=st_today, end=ed_today, freq='30min', closed='left')
    df1 = df0.reindex(rng1)
    print df1.head()

    # Reset datetime index
    st_date = cdate
    ed_date = st_date + timedelta(days=1)
    rng2 = pd.date_range(start=st_date, end=ed_date, freq='30min', closed='left')
    df2 = df1.set_index(rng2)
    print df2.head()

    if df is None:
        df = df2


