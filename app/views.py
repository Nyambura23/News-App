
from flask import render_template 
from  app import app
from .request import get_news ,get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

        # Getting general news
    general_news = get_news('general')
    # print(general_news)
    
    return render_template('index.html', general = general_news)