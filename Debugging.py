import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def webcrawl(url):
    wordlist=[]
    response=requests.get(url)
    source_code=response.text
#    print(response)
#    print(source_code)
    html_parser=BeautifulSoup(source_code,'html.parser')
#    print(html_parser)

    for each_text in html_parser.find_all('div', {'class':'entry-content'}):
        content=each_text.text
        words=content.lower().split()
        print(content)

# Driver code
if __name__ == '__main__':
    webcrawl('https://www.geeksforgeeks.org/python-program-crawl-web-page-get-frequent-words/')