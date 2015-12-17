#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while pages < max_pages:
		url = 'https://www.thenewboston.com/forum/recent_activity.php?page=' + str(page)