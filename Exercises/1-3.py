from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.data.gov/")
bsObj = BeautifulSoup(url, features="lxml")
dataset = bsObj.find("div", {"class": "getstarted"}).find("a")
print("In https://www.data.gov/ there are currently:")
print(dataset.text)