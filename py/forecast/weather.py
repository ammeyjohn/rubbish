__author__ = 'patrick'


from datetime import datetime
from io import StringIO
import urllib2
import pandas as pd


# Defines the global const value
ROOT_DOMAIN = 'http://www.wunderground.com'
PART_DOMAIN = '/history/station'


def get_url(code, date_str):
    """Generate the url for weather downloading.
    :param code: The code of weather station.
    :param date_str: The date string of weather to download.
    :return: Returns the url which point to the weather download page.
    """

    d = datetime.strptime(date_str, '%Y-%m-%d')

    url = ROOT_DOMAIN + PART_DOMAIN
    url += '/%s' % code
    url += '/%d/%d/%d' % (d.year, d.month, d.day)
    url += '/DailyHistory.html?format=1'
    return url


def download(url):
    """Download html from given url
    :param url: The url of the page to download.
    :return: Returns the html string.
    """

    req = urllib2.Request(url)
    html = urllib2.urlopen(req).read()
    return html

def download_to_csv(url):
    """
    :param url:
    :return:
    """
    return pd.read_csv(url)


if __name__ == '__main__':

    df = None

    url =  get_url('zsss', '2013-04-25')
    print 'Downloading from %s' % url

    html = download(url)
    html = html.strip()
    html = html.replace('<br />', '')
    print html

    str = StringIO(unicode(html))
    print str

    df = pd.DataFrame.from_csv(str)
    rng = pd.date_range(start='2015-04-08', end='2015-04-09', freq='30min', closed='left')
    df1 = df.reindex(rng)
    print df1.head(60)
    rng2 = pd.date_range(start='2013-04-25', end='2013-04-26', freq='30min', closed='left')
    for r in rng2:
        print r
    df2 = df1.set_index(rng2)
    print df2.head()


