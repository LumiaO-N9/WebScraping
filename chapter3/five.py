from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re, datetime, random

pages = set()
random.seed(datetime.datetime.now())


def getInternalLinks(bsObj, includeUrl):
    print(includeUrl)
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(
        includeUrl).netloc
    print(includeUrl)
    internalLinks = []
    for link in bsObj.findAll(
            "a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll(
            'a',
            href=re.compile("^(http|https|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
        bsObj = BeautifulSoup(html)
    except (HTTPError, URLError) as e:
        print('urllib.error')
    externalLinks = getExternalLinks(bsObj, startingPage)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        internalLinks = getInternalLinks(bsObj, startingPage)
        if len(internalLinks) == 0:
            print(
                'WebScraping program is stoped because there is no Externalinks or Internalinks in this webpage!'
            )
            return None
        return getRandomExternalLink(internalLinks[random.randint(
            0,
            len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)

    if externalLink is None:
        exit()
    print('Random external link is: ' + externalLink)
    followExternalOnly(externalLink)


def splitAddress(address):
    if "https://" in address:
        addressParts = address.replace("https://", "").split("/")
    else:
        addressParts = address.replace("http://", "").split("/")
    return addressParts


allExtLinks = set()
allIntLinks = set()


def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    print(internalLinks)
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是：" + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)


getAllExternalLinks("https://oreilly.com")
print("getAllExternalLinks is over")
followExternalOnly("http://www.baidu.com")
