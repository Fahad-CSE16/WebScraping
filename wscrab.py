from urllib.request import urlopen
from bs4 import BeautifulSoup

url_aj="http://www.aljazeera.com"
filepath="html/aj.html"

class NewsScrapper:
    __url =''
    __data=''
    __wlog=None
    __soup=None

    def __init__(self, url, wlog):
        self.__url=url
        self.__wlog=wlog
    
    def retrieve_webpage(self):
        try:
            html=urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)

        else:
            self.__data=html.read()
            if len(self.__data)> 0:
                print('retrieved successfully')
    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath,'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)       
            self.__wlog.report(str(e))
    def read_webpage_from_html(self,filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__data=fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
    def change_url(self,url):
        self.__url=url
    def print_data(self):
        print(self.__data)
    def convert_data_to_bs4(self):
        self.__soup=BeautifulSoup(self.__data,'html.parser')
    def parse_soup_to_simple_html(self):
        new_list=self.__soup.find_all(['h1','h2','h3','h4','h5','h6','a','span'])
        new_list+=self.__soup.select('.card-gallery__title')
        # print(new_list)
        html_text='''<html><head><title>Simple Web scrapping</title></head><body>{NEWS_LINKS}</body></html>'''
        new_links ='<ol>'
        for tag in new_list:
            if tag.parent.get('href'):
                link=self.__url+tag.parent.get('href')
                title=tag.string
                new_links+= "<li><a href='{}' target='_blank' >{}</li>\n".format(link,title)
        new_links+='</ol>'
        html_text=html_text.format(NEWS_LINKS=new_links)
        self.write_webpage_as_html(filepath='html/new_simple.html',data=html_text.encode())