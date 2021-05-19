#!/usr/bin/env python3

from bs4 import BeautifulSoup as BS
from requests import get
from datetime import datetime
from urllib.parse import urlparse

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

def to_link(url):
    html = get(url, headers=headers).content
    dom = BS(html, features="lxml")
    title = dom.title.text
    host = urlparse(url).netloc
    date = datetime.today()
    date = "%s.%s.%s" % (date.day, date.month, date.year)
    return "%s // %s URL: %s (дата обращения: %s)" % (title, host, url, date)

if __name__ == '__main__':
    import sys
    try:
        url = sys.argv[1]
        print(to_link(url))
    except IndexError:
        print('use %s http://google.com/' % sys.argv[0], file=sys.stderr)

