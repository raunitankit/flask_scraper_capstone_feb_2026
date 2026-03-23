# Flask Dashboard setup

from flask import Flask,render_template
from scraper import scrape_quotes, quotes_to_df,scrape_books, books_to_df

app = Flask(__name__) # tells FLASK to create the app - object - so it knows where to find the templates, static files,etc.

""" @app.route("/")
def hello():
    return "Hello, World!" """

@app.route("/")
def dashboard():
    quotes,author = scrape_quotes(limit=10)   #Enhancement by ***NANCY GARG***
    df =quotes_to_df(quotes,author)
    #return "Hello World!"
    return render_template("dashboard.html",tables=[df.to_html (classes='data')],titles=df.columns.values, page_title="Quotes Dashboard", page_type="quotes")
    # converts the Dataframe DF into an html table
    # jinja2 -> flask template engine. it is what we use to work with python code inside the html
    # enhacenemnts - add more decorators like /about and put your description


#Enhancement by ***NANCY GARG***
@app.route("/books")
def dashboard_books():
    books = scrape_books(limit=10) 
    df =books_to_df(books)
    #return "Hello World!"
    return render_template("dashboard.html",tables=[df.to_html (classes='data')],titles=df.columns.values, page_title="Books Dashboard", page_type="books")

    # converts the Dataframe DF into an html table

#Enhancement by ***NANCY GARG***
@app.route("/about")
def about():
    about_text = """I am Nancy Garg, a passionate Python learner. I love exploring new coding challenges and spending time enhancing my skills. My goal is to build projects that are both practical and fun, while continuously learning and growing as a developer. Added below enhancements to "Original Feb 2026 Capestone" project:""" 
    enhancements = [
        "Added Books function",
        "Added Author column for the quotes",
        "Added new pages for Books and About Me functions",
        "Changed Index to run from 1–10 instead of 0–9",
        "Hosted this project on Render",
        "Added a splash of color",
        "Added Hyperlinks to navigate to different pages"
    ]
    return render_template(
        "dashboard.html",
        page_title="About Me",
        page_type="about",
        page_content=about_text,
        enhancements=enhancements,
        tables=None  # no tables for About page
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5500, debug=False) # use 5000 as port in your deployment unless you have anything running on that port.
    #0.0.0.0 --> instead of localhost we are giving comp localnetwork

    
