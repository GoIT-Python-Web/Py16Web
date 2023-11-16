import requests
from bs4 import BeautifulSoup
import json


def get_page_content(url):
    response = requests.get(url)
    content = BeautifulSoup(response.content, 'html.parser')
    return content


def get_quotes(content):
    quotes = content.find_all('div', class_='quote')
    return [quote.find('span', class_='text').get_text() for quote in quotes]


def get_authors(content):
    authors = content.find_all('div', class_='quote')
    return [author.find('small', class_='author').get_text() for author in authors]


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


base_url = 'http://quotes.toscrape.com'
page_content = get_page_content(base_url)

quotes = []
authors = []

while True:
    quotes.extend(get_quotes(page_content))
    authors.extend(get_authors(page_content))

    next_page_link = page_content.find('li', class_='next')
    if next_page_link is None:
        break

    next_page_url = base_url + next_page_link.find('a')['href']
    page_content = get_page_content(next_page_url)

save_to_json(quotes, 'quotes.json')
save_to_json(authors, 'authors.json')
