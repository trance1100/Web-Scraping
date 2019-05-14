from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features="lxml")

for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)
    