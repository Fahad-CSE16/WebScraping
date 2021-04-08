import requests
from bs4 import BeautifulSoup

url="https://codewithharry.com/"
c=requests.get(url)
htmlc=c.content
# print(htmlc)

soup= BeautifulSoup(htmlc,'html.parser')
# print(soup)
# print(soup.prettify)
title=soup.title
# print(title)
# print(type(title))

pera=soup.find('p') #first pera
peraText=soup.find('p').get_text() #first pera er text
# print(pera)
# print(pera['class'])
# print(pera.next_sibling.next_sibling)
# print(pera.next_sibling)
# print(pera.previous_sibling.previous_sibling)
# print(pera.previous_sibling)
# print(pera.contents)
# print(pera.strings)
# print(pera.stripped_strings)
# print(pera.clildren)
# print(pera.parent)
# for prnt in pera.parents:
#     print(prnt)

peras=soup.find_all('p') #all pera

anchors=soup.find_all('a')
# for link in anchors:
#     print(link.get('href'))
all_links=set()
for link in anchors:
    if link.get('href') != '#':
        all_links.add(url+link.get('href'))
# print(all_links)
