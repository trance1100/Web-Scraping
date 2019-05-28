from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://en.wikipedia.org/robots.txt")
bsObj = BeautifulSoup(url, features="lxml")
print(bsObj.text)