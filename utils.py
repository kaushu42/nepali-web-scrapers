import urllib as u
from bs4 import BeautifulSoup
import re
import requests

def _headers():
    return {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }

def _request(url):
    req = u.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    return req

def get_page_soup(url):
#     req = _request(url)
#     page = u.request.urlopen(req)
#     soup = BeautifulSoup(page, 'lxml')
#     return soup
    response = requests.get(url, headers=_headers())
    content = response.content.decode()
    return BeautifulSoup(content, 'lxml')

_p1 = re.compile(r'[^\u0900-\u097f\s]')
_p2 = re.compile(r"[०-९]")
_p3 = re.compile(r"[\n]+")

stopwords = set(open('stop-words.list').read().split('\n')[:-1])

def clean(text, keep_numbers=False, newline=False):
    sub = _p1.sub('', text)
    if keep_numbers:
        sub = _p2.sub("", sub)
    if newline:
        sub = _p3.sub('\n', sub)
    return sub

