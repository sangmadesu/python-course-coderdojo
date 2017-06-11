import requests as req 
from bs4 import BeautifulSoup as soup

url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=180'
response = req.get(url)
result = soup(response.content, 'lxml')

row = result.find_all('tr', 'table_highlight')
data = row[0]

# print data

# perulangan suatu array/list
i = 0
waktu_berbuka = ''
for d in data:
	if i == 5:
		waktu_berbuka = d.text 
	i = i + 1

print 'waktu berbuka =', waktu_berbuka