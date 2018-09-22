from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen(
    'http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode(
        'ascii', 'ignore')

dataFile1 = StringIO(data)
dataFile2 = StringIO(data)
csvReader = csv.reader(dataFile1)
for row in csvReader:
    print(row)

dictReader = csv.DictReader(dataFile2)
print(dictReader.fieldnames)
for row in dictReader:
    print(row)
