import requests
from bs4 import BeautifulSoup

def url_to_transcript(url):
    '''Returns transcript data from millercenter.org'''

    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="transcript-inner").find_all('p')]
    print(url)
    return text