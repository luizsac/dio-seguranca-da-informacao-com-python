import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    word_list = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")

    # o texto na página dada está contido nas tags <div> pertencentes à classe "entry-content"
    for each_text in soup.find_all("div", {"class": "entry-content"}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            word_list.append(each_word)
        
        clean_word_list(word_list)

def clean_word_list(word_list):
    clean_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_-+={[}]|\;:'<>?/,. "

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        
        if len(word) > 0:
            clean_list.append(word)
    
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(f"{key} : {value}")
    
    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == "__main__":
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=shm")