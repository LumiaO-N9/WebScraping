from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"


def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = "http://" + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://' + source[4:]
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = downloadDirectory + absoluteUrl.replace('www.', '').replace(
        baseUrl, '')
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl,
                    getDownloadPath(baseUrl, fileUrl, downloadDirectory))
