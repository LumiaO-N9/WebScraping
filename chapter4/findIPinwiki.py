from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime, random, re, json

random.seed(datetime.datetime.now())


def getCountry(ipAddress):
    with open('/home/lumia/Desktop/AccessKey.txt', 'r') as f:
        name, MyAccess_key = f.read().split(':')
        try:
            response = urlopen('http://api.ipstack.com/' + ipAddress +
                               '?access_key=' +
                               MyAccess_key).read().decode('utf-8')
        except HTTPError:
            return None
        return json.loads(response).get('country_code')


def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {
        "id": "bodyContent"
    }).findAll("a", {'href': re.compile('^(/wiki/)((?!:).)*$')})


def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title=' + pageUrl + '&action=history'
    print('history url is : ' + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipAddresses = bsObj.findAll('a', {'class': 'mw-userlink mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


links = getLinks('/wiki/Python_(programming_language)')

while (len(links) > 0):
    for link in links:
        print('-------------------------')
        historyIPS = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPS:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + ' is from ' + country)
    newLink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLink)
