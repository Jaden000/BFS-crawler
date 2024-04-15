from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlsplit
from html.parser import HTMLParser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import sys
import os

def Filtering_url(seed_url, url_arr, visited_list):
    result = []
    
    origin_host_url = "{0.scheme}://{0.netloc}/".format(urlsplit(seed_url)) 

    tmp = set(url_arr) #removing duplicated url 
    url_arr = list(tmp)
    
    for url in url_arr:
		url = url.rstrip('/') 
        if url in  visited_list:  #duplicated url 
            continue
        elif url in queue:   #duplicated url 
        	continue
        elif not url: #meaningless url 
            continue
        elif url == "javascript:;" or url[0] =='#': #meaningless url
            continue
        elif "{0.scheme}://{0.netloc}/".format(urlsplit(url)) !=  origin_host_url: #irrelevant url
                continue
        else: 
            result.append(url)

    return result

def BFS_crawler(url):
    visited_list.append(url)

    if len(visited_list) > 100: # end when number of visited url is 50
        return
    
    with urllib.request.urlopen(url) as res:
        soup = BeautifulSoup(res.read(), 'html.parser') 

    a_tags = soup.find_all("a", href = True)
    urls = [] 
    for i in a_tags:
        urls.append(i['href'])

    filtered_urls = Filtering_url(seed_url, urls, visited_list) #url filtering (1. duplicated url; 2. meaningless url; 3. has different origin host as seed url's origin host)
    level_starting_loc.append( level_starting_loc[-1] + len(filtered_urls))

    queue.extend(filtered_urls)
	
    if not queue: # there is no element in queue
        return

    BFS_crawler(queue.pop(0))
        




if len(sys.argv) == 1: #if there is no argv[1], give a default seed url 
	seed_url = "https://news.naver.com"
else: 
	seed_url = sys.argv[1].rstrip('/')

level_starting_loc = [0, 1] #starting location of the level
queue = [seed_url]
visited_list = []
BFS_crawler(queue.pop(0))

k = 0
for i, url in enumerate(visited_list):
	if len(level_starting_loc) >= k: 
		if i == level_starting_loc[k]:
			print("--------------------------------"+str(k)+" level------------------------------------")
			k += 1
	print(url)

