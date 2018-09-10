from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except (HTTPError, URLError) as e:
    html = None
try:
    bsObj = BeautifulSoup(html)
except AttributeError as e:
    print(e)
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    "print(name)"
    print(name.get_text())
