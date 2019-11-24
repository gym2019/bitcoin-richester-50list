import requests
import requests_cache
import lxml.html

requests_cache.install_cache('comment_cache')

from lxml.cssselect import CSSSelector

URL_50 = 'https://bitinfocharts.com/top-100-richest-bitcoin-addresses-{page_num}.html'


def get_href(html):
    tree = lxml.html.fromstring(html)
    sel = CSSSelector('.table tbody tr td a')
    return [i.get('href') for i in sel(tree)]


def get_text(html):
    tree = lxml.html.fromstring(html)
    sel = CSSSelector('.table tbody tr td a')
    return [i.text_content() for i in sel(tree)]


session = requests.Session()

# TO DO: make an iterable for loop for each page
page_num = 1

response = session.get(URL_50.format(page_num=page_num))
html = response.text
hrefs = get_href(html)
addresses = get_text(html)

print(addresses)