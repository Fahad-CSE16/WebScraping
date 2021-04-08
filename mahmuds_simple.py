from urllib.request import urlopen
from bs4 import BeautifulSoup
url_aj="http://www.aljazeera.com"
filepath="html/aj1.html"
html=urlopen(url_aj)
data=html.read()

soup=BeautifulSoup(data,'html.parser')

new_list=soup.find_all(['h1','h2','h3','h4','h5','h6','a','span'])
new_list+=soup.select('.card-gallery__title')
html_text='''<html><head><title>Simple Web scrapping</title></head><body>{NEWS_LISTS}</body></html>'''
new_links ='<ol>'
for tag in new_list:
    if tag.parent.get('href'):
        link=url_aj+tag.parent.get('href')
        title=tag.string
        new_links+= "<li><a href='{}' target='_blank' >{}</li>\n".format(link,title)
new_links+='</ol>'

html_text=html_text.format(NEWS_LISTS=new_links)

fobj=open('html/new_simple1.html','wb')
if data:
    fobj.write(html_text.encode())