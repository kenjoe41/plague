

import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'plugin_research/0.0.1'}
page = requests.get("http://plugins.svn.wordpress.org/", headers=headers)
# print(page.content)

soup = BeautifulSoup(page.text, 'html.parser')

pList = soup.find('ul')
if pList:
	num_plugins = len(pList.find_all('li'))
	print(num_plugins)
else:
	print("We didn't find anything Boss, prolly something went wrong.")