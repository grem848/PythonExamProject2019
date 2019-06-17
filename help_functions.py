import requests
from bs4 import BeautifulSoup

# url = sys.argv[1:]

def url_to_transcript(url):
    '''Returns transcripts from millercenter.org'''
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="transcript-inner").find_all('p')]
    print('Downloading transcript from ' + url)
    return text

def combine_text(list_of_text):
    '''Takes a list of strings and combines them into one single string.'''
    combined_text = ' '.join(list_of_text)
    return combined_text