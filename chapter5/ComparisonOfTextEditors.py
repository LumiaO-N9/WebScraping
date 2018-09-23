from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html)
table = bsObj.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')
with open('./editors.csv', 'w', newline='', encoding='utf-8') as csvFile:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        print(csvRow)
        csv.writer(csvFile).writerow(csvRow)
