#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests

def get_hyper(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a'):
        hyper = link.get('href')
        if hyper[0] == '/':
            hyper = url + hyper
        elif hyper[0] == '#':
            continue
        print(hyper)

def get_content(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.get_text())

if __name__ == '__main__':
    get_hyper('https://pyhello.world')
    get_content('https://pyhello.world')
