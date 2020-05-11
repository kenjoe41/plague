

import requests
from bs4 import BeautifulSoup
import re

headers = {'user-agent': 'plugin_research/0.1'}
page = requests.get("http://plugins.svn.wordpress.org/", headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')
revision = soup.h2
if revision:
	regex = r"(Revision\s[0-9]+)"
	rHeader = re.search(regex, revision.string)
	print(rHeader[0])

pList = soup.find('ul')
if pList:
	num_plugins = len(pList.find_all('li'))
	print(num_plugins)
else:
	print("We didn't find anything Boss, prolly something went wrong.")