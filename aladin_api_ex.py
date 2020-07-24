import sys
from urllib import parse, request
from bs4 import BeautifulSoup

def toString(utf8String):
	return str(utf8String).decode('utf-8', 'ignore').encode('cp949', 'ignore')

#print(sys.argv)
#query = sys.argv[0];print(query)
query = '잎 속의 검은 잎'
data = parse.urlencode({
	'ttbkey' : 'ttbtororok9111807001', 
	'QueryType' : 'Title', 
	'MaxResults':'10', 
	'start':'1', 
	'SearchTarget':'Book', 
	'output':'xml', 
	'Query':query,
	'inputencoding':'euc-kr',
	'Version':'20070901'
})
print('data:', data)
url = 'http://www.aladdin.co.kr/ttb/api/ItemSearch.aspx'
#url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=[TTBKey]&Query=aladdin&QueryType=Title&MaxResults=10&start=1&SearchTarget=Book&output=xml&Version=20131101'

con = request.urlopen(url +'?' + data) # HTTPResponse object
print('url: ', url+ '?' + data)
objectXml = con.read()
con.close()

soup = BeautifulSoup(objectXml, features="xml")
soupString = str(soup); print(soupString)

if soupString.find('<error xml') > -1:
	for s in soup('errormessage'):
		print('## Error!! ##')
		print("Error Message: ", toString(s.contents[0]))
else:
	for s in soup('item'):
		print(toString(s.title.contents[0]), '-' , toString(s.link.contents[0]))


