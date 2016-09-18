from bs4 import BeautifulSoup
from collections import Counter
from operator import itemgetter as iget
import requests
import os
import time

start_url = os.environ.get('URL', 'http://www.cs.ucla.edu')
links = Counter()
links_visited = set()
links_to_visit = [start_url]
max_pages = 5
visited_pages = 0

def get_links(url):
    mylinks = Counter()
    html = requests.get(url, verify=False)
    soup = BeautifulSoup(html.text)
    for a in soup.find_all('a'):
        href = a.get('href')
        if href != '#' and href is not None:
            if not href.startswith('http'):
                href = url + href
            mylinks[href] += 1
    return mylinks

while len(links_to_visit) > 0 and visited_pages <= max_pages:
    next_link = links_to_visit.pop(0)
    if next_link in links_visited or next_link is None:
        continue

    links_visited.add(next_link)
    new_links = get_links(next_link)
    links += new_links
    for link in new_links:
        if link not in links_visited and link not in links_to_visit:
            links_to_visit.append(link)
    visited_pages += 1
    # don't ruin the internet
    time.sleep(0.2)
    print "visited: ", next_link


for tup in links.most_common():
    print tup[1]," ", tup[0]
