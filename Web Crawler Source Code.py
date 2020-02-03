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
#        print(content)

        for each_word in words:
            wordlist.append(each_word)
#        print(wordlist)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list=[]

    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
        for i in range(0,len(symbols)):
            word=word.replace(symbols[i],'')
        if len(word)>0:
            clean_list.append(word)
#    print(clean_list)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count={}
    for word in clean_list:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
#    print(word_count)

    c=Counter(word_count)
#    print(c)
    top=c.most_common(10)
    print(top)

# Driver code
if __name__ == '__main__':
    webcrawl('https://www.geeksforgeeks.org/programming-language-choose/')
