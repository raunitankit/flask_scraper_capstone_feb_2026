# rule of thumb is test every function and class/object that you have written inside your python module(s)
from scraper import scrape_quotes,quotes_to_df,scrape_books,books_to_df
from scraper import scrape_quotes,quotes_to_df,scrape_books,books_to_df


def test_scrape_quotes():
    quotes,author = scrape_quotes(limit=3)
    assert len(quotes) == 3 # getting back 3 entries in my list or not. 
    assert len(author) == 3

def test_scrape_books():
    books = scrape_books(limit=3)
    assert len(books) == 3 # getting back 3 entries in my list or not. 



def test_quotes_to_df():
    df = quotes_to_df(["ThinkPython", "AI"],["Nancy Garg", "Mickey Mouse"]) # treat this as quotes and we are passing only 2 elements "ThinkPython" and "AI"
    assert df.shape[0] ==  2
    assert "Quotes" in df.columns
    assert "Author" in df.columns
    # enhancement woudl be add a third column name as "Author" and assert that as well.

def test_books_to_df():
    df = books_to_df(["Book1", "Book2", "Book3"]) # modified for books
    assert df.shape[0] ==  3
    assert "Books" in df.columns

#pytest -v - this is how you run it.
