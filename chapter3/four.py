from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re

pages = set()


def getLinks(pageUrl):
    global pages
    try:
        html = urlopen('http://en.wikipedia.org' + pageUrl)
    except (HTTPError, URLError) as e:
        print('urllib.error')
    try:
        bsObj = BeautifulSoup(html)
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print('AttributeError')

    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('------------------------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
