
# from pickle import APPEND
from flask import render_template 
from  app import app
from .request import get_news, get_category

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
        # Getting general news
    general_news = get_news('technology')
    # print(general_news)
    
    return render_template('index.html', general = general_news )

# @app.route('/article/<id>')
# def article(id):

#     '''
#     View article page function that returns the various article details page and its data
#     '''
#     # title= 'Articles'
#     articles = get_article(id)
#     return render_template('article.html',articles= articles,id=id )
    
@app.route('/categories/<categ_name>')
def category(categ_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(categ_name)
    title = f'{categ_name}'
    cate = categ_name

    return render_template('categories.html',title = title,category = category, cate= categ_name)

