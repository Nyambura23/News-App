
# from pickle import APPEND
from flask import render_template,request,redirect,url_for
from  app import app
from .request import  get_news, get_category, search_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
        # Getting general news
    general_news = get_news('technology')
    # print(general_news)
    
    search_article= request.args.get('news_query')

    if search_article:
     return redirect(url_for('search',news_name=search_article))
    else:

     return render_template('index.html', general = general_news )

# @app.route('/source/<source_name>')
# def source(source_name):
#     article_display = get_article_by_source(source_name)
#     title = source_name.upper()

#     return render_template('source.html', article_display=article_display,title=title )
    
@app.route('/categories/<categ_name>')
def category(categ_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(categ_name)
    title = f'{categ_name}'
    cate = categ_name

    return render_template('categories.html',title = title,category = category, cate= categ_name)


@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news= search_article(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',movies = searched_news)
