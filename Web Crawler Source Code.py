import requests
from bs4 import BeautifulSoup
import operator
import collections

def webcrawl(url):
    wordlist=[]
    response=requests.get(url)
    source_code=response.text
#    print(response)
#    print(source_code)
    html_parser=BeautifulSoup(source_code,'html.parser')
#    print(html_parser)

    for each_text in html_parser.find_all('dev',{'class':'entry-content'}):
        content=each_text.text
        words=content.lower().split()

webcrawl('http://www.github.com')
