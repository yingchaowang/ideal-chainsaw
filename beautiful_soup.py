from bs4 import BeautifulSoup
from collections import Counter
from operator import itemgetter as iget
import requests
import os

url = os.environ.get('URL', 'http://www.cs.ucla.edu')
html = requests.get(url)
soup = BeautifulSoup(html.text)
links = Counter()
for a in soup.find_all('a'):
    href = a.get('href')
    if href != '#':
        if not href.startswith('http'):
            href = url + href
        links[href] += 1

for v in links.most_common():
    print v
