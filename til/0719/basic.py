import requests
import pprint

key = '91284a83b7411eebfefdc29320bc5cfa'
targetDt = '20190713' #yyyymmdd
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json
?key={key}&targetDt={targetDt}'

pprint.pprint(api_url)
response = requests.get(api_url).json()
pprint.pprint(response)
