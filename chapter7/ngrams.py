from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re, string


def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or item.lower() == 'a' or item.lower() == 'i':
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


def constructDict(ngramsList):
    ngramsSet = set()
    ngramsDict = {}
    for i in ngramsList:
        if str(i) not in ngramsSet:
            ngramsSet.add(str(i))
            ngramsDict[str(i)] = 1
        else:
            ngramsDict[str(i)] = ngramsDict[str(i)] + 1
    return ngramsDict


html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html)
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = ngrams(content, 2)
# print(ngrams)
print('2-grams count is : ' + str(len(ngrams)))
ngramsDict = constructDict(ngrams)
print(type(ngramsDict))
ngramsOderedDict = OrderedDict(sorted(ngramsDict.items(), key=lambda t: t[1]))
print(ngramsOderedDict)
print('2-grams count is : ' + str(len(ngramsOderedDict)))
