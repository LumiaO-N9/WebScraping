from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re
try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    html2 = urlopen("http://www.pythonscraping.com/pages/page3.html")
except (HTTPError, URLError) as e:
    html = None
    html2 = None
try:
    bsObj = BeautifulSoup(html)
    bsObj2 = BeautifulSoup(html2)
except AttributeError as e:
    print(e)
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    "print(name)"
    print(name.get_text())

nameList2 = bsObj.findAll(text="the prince")
print(len(nameList2))
alltext = bsObj.findAll(id="text")
print(alltext[0].get_text())

for child in bsObj2.find("table", {"id": "giftList"}).children:
    print(child)

for sibling in bsObj2.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

print(
    bsObj2.find("img", {
        "src": "../img/gifts/img1.jpg"
    }).parent.previous_sibling.get_text())

images = bsObj2.findAll("img",
                        {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image)
