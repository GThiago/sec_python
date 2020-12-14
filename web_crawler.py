import requests
import re
# expressões regularres

to_crawl = ['http://wikipedia.org']
crawled = set()

header = {'user-agent':"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

while True:
    url = to_crawl[0]
    try:
        req = requests.get(url, headers=header)
        html = req.text
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue

    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    #padrao = re.findall(r'href=\'?"?(https?://[\w:\.\'"@/_]+)', html)
    print('Crailing: ', url)

    to_crawl.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)
