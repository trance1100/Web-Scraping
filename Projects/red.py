from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="lxml")
nameList = bsObj.find_all("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

allText = bsObj.find_all(id="text")
print(allText[0].get_text())