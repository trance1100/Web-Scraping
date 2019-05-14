import urllib3
from bs4 import BeautifulSoup

url = "http://www.imdb.com/search/title?release_date=" + "2019"
ourUrl = urllib3.PoolManager().request('GET', url).data 
soup = BeautifulSoup(ourUrl, features="lxml")

i = 1
movieList = soup.find_all('div', attrs={'class': 'lister-item mode-advanced'})
soup.find
for div_item in movieList:
    div = div_item.find('div', attr={'class': 'lister-item mode-advanced'})
    print(str(i) + ".")
    header = div.find_all('h3',attrs={'class':'lister-item-header'})

    print('Movie: ' + str((header[0].find_all_next('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

    i += 1