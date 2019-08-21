import requests
from bs4 import BeautifulSoup as bs


def news():
    url = "https://www.isro.gov.in"

    page = requests.get(url)
    soup = bs(page.content, 'html5lib')
    articles = []
    updates = soup.find('div', attrs = {'class':'updates'})

    for i,update in enumerate(updates.findAll('span',attrs={'class':'field-content'})):
        article_ = {}
        article_['id'] = i+1
        article_['date'] = update.strong.text
        article_['headline'] = update.text[15:]
        article_['link'] = url+update.a['href']
        articles.append(article_)

    return(articles)

def archives():
    url = "https://www.isro.gov.in/updates-archivals"

    page = requests.get(url)
    soup = bs(page.content, 'html5lib')
    articles = []
    updates = soup.find('table', attrs = {'class':'views-table'})

    for i,update in enumerate(updates.findAll('td',attrs={'class':'views-field-title-1'})):
        article_ = {}
        article_['headline'] = update.text[:-13]
        article_['link'] = url+update.a['href']
        articles.append(article_)

    return(articles)
