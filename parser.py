#The parser returns us a line with article headers based on our requests.

import urllib.request
from bs4 import BeautifulSoup

def getAllTitle(amount, rating='all'):
    output = ''
    for i in range(1, amount+1):
        try:
            if rating == 'all':
                html = urllib.request.urlopen('https://habr.com/ru/all/page'+ str(i) +'/').read()
            else:
                html = urllib.request.urlopen('https://habr.com/ru/all/'+ rating +'/page'+ str(i) +'/').read()
        except urllib.error.HTTPError:
            print('Error 404 Not Found')
            break
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('a', class_ = 'post__title_link')
        for i in title:
            i = i.get_text()
            output += ('- "'+i+'",\n')
    return output

def getTopTitile(amount, ade='daily'):
    output = ''
    for i in range(1, amount+1):
        try:
            html = urllib.request.urlopen('https://habrahabr.ru/top/'+ age +'/page'+ str(i) +'/').read()
        except urllib.error.HTTPError:
            print('Error 404 Not Found')
            break
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('a', class_ = 'post__title_link')
        for i in title:
            i = i.get_text()
            output += ('- "'+i+'",\n')
    return output