from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen(
    "https://en.wikipedia.org/wiki/Kevin_Bacon")  # no great fxxk wall
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

for link in bsObj.find("div", {
        "id": "bodyContent"
}).findAll(
        "a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
