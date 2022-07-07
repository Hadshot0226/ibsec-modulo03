# author: Tarcio Rodrigo
# requirements:
# pip install beautifulsoup4
# pip install html5lib
# pip install requests

import requests
url = "https://ignitelab-delta.vercel.app/"
r = requests.get(url)
#print(r.content)

from bs4 import BeautifulSoup
import csv
soup = BeautifulSoup(r.content, 'html5lib')
print("*****HTML:******")
print(soup.prettify())