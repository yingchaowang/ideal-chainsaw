from bs4 import BeautifulSoup
from collections import Counter
from operator import itemgetter as iget
import requests
import os

start_url = os.environ.get('URL', 'http://www.cs.ucla.edu')
html = requests.get(url)
soup = BeautifulSoup(html.text)
links = Counter()
links_visited = set()
links_to_visit = [start_url]

def get_links(url):
    mylinks = Counter()
    for a in soup.find_all('a'):
        href = a.get('href')
        if href != '#':
            if not href.startswith('http'):
                href = url + href
            mylinks[href] += 1
    return mylinks

while len(links_to_visit) > 0:
    next_link = links_to_visit.pop()
    if next_link in links_visited:
        continue

    links_visited.add(next_link)
    new_links = get_links(next_link)
    links += new_links
    for link in new_links:
        if link not in links_visited and link not in links_to_visit:
            links_to_visit.add(link)


for tup in links.most_common():
    print tup[1]," ", tup[0]
