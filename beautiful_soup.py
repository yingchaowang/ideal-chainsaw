from bs4 import BeautifulSoup
from collections import Counter
from operator import itemgetter as iget
import requests

html = requests.get('http://www.cs.ucla.edu')
soup = BeautifulSoup(html.text)
links = Counter()
for a in soup.find_all('a'):
    links[a.get('href')] += 1

for v in links.most_common():
    print v
