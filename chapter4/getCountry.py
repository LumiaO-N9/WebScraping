import json
from urllib.request import urlopen


def getCountry(ipAddress):
    with open('/home/lumia/Desktop/AccessKey.txt', 'r', encoding='utf-8') as f:
        AccessName, MyAccess_key = f.read().split(':')
        response = urlopen('http://api.ipstack.com/' + ipAddress +
                           '?access_key=' +
                           MyAccess_key).read().decode('utf-8')
        responseJson = json.loads(response)
        return responseJson.get("country_code")
    return None


print(getCountry("50.78.253.58"))
