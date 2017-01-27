from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://mikebozee.com').read()
soup = BeautifulSoup(r)
print(type(soup))

print(soup.prettify()) [0:1000]