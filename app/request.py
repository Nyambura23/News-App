from email.mime import image
from app import app 
import urllib.request,json
from .models import news


News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting news base url

base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_article_data = url.read()
        get_news_response = json.loads(get_article_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for item in news_list:
        # id = item.get('id')
        author = item.get('author')
        description = item.get('description')
        time = item.get('time')
        url = item.get('url')
        image = item.get('image')
        title = item.get('title')

        if description:
            news_object = News(author,description,time,url,image,title)
            news_results.append(news_object)

    return news_results