# Web-Crawler
## This is the Python software for identify the most common words used in web site, using web crawler

### Libraries and Modules are used for the operation.
1. requests : Will send HTTP/1.1request and many more
2. beautifulsoup4 : Pulling data out of HTML and XML
3. operator : Export a set of efficient Function
4. Collection : Implement High Performance Data Type

###Following code is used to extract the html format of the webpage from the specific web address.
source_code = requests.get(url).text

###Following Code is used to parse the given html web page.
soup = BeautifulSoup(source_code, 'html.parser') 

### From below code we can output all the text from the given URL. There will be 2 for loops running seperatly.
    for each_text in html_parser.find_all('div', {'class':'entry-content'}):
        content=each_text.text
        words=content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
###

###
