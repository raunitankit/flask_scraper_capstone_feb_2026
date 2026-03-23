# this module is used for scraping - core logic is here

# functions to scrape quotes and build Pandas DF.

import requests
import pandas as pd
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG)


def scrape_quotes(limit=5):  # default arg
    url = "https://quotes.toscrape.com/"

    response = requests.get(url)  # fetches webpage.
    if response.status_code != 200:  # 200 is for successful fetch
        logging.error("Failed to fetch the website and it returned code as : ", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    #<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
    quotes = [q.text for q in soup.find_all("span", class_="text")]
    #<small class="author" itemprop="author">Albert Einstein</small>
    author = [a.text for a in soup.find_all("small", class_="author")] #Enhancement by ***NANCY GARG***

    return quotes[:limit], author[:limit] #Enhancement by ***NANCY GARG***
 


# books function added by ***NANCY GARG***

def scrape_books(limit=5):
    url = "https://books.toscrape.com/"

    response = requests.get(url)
    if response.status_code != 200:
        logging.error("Failed to fetch the website and it returned code as : ", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    books = [t.h3.a["title"] for t in soup.find_all("article", class_="product_pod")]

    return books[:limit]


# Pandas Dataframe - very handy for tabular form of representation
def quotes_to_df(quotes,author):    #Enhancement by ***NANCY GARG***
    df = pd.DataFrame({"Quotes": quotes, "Author": author} ) 
    df.index=df.index + 1 
    return df


# books function added by ***NANCY GARG***

def books_to_df(books):
    df = pd.DataFrame(books, columns=["Books"])
    df.index=df.index + 1 

    '''
        Quote
    0   <actual quote>“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
    1   “It is our choices, Harry, that show what we truly are, far more than our abilities.”
    '''

    return df