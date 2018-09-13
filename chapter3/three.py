from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re

pages = set()


def getLinks(pageUrl):
    try:
        html = urlopen('http://en.wikipedia.org' + pageUrl)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html)
    except Exception as e:
        print(e)
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
