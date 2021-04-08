import requests, webbrowser
from bs4 import BeautifulSoup

# user_input= input("ENter something to search on goole")
print("googling............")
html= requests.get("https://www.google.com/search?q="+'fahad')
soup=BeautifulSoup(html.content, 'html.parser')
search_results=soup.find_all('a')
for link in search_results[15:20]:
    actual_link=link.get('href')
    # print(actual_link)
    webbrowser.open('https://google.com/'+actual_link)
