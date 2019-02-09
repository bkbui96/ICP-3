from bs4 import BeautifulSoup
import urllib.request

soup = BeautifulSoup(urllib.request.urlopen('https://en.wikipedia.org/wiki/Deep_learning'), features="html.parser")

print(soup.title.string)

for link in soup.find_all('a'):
    print(link.get('href'))
