
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
    for news_item in news_list:
        author = news_item.get('author')
        description = news_item.get('description')
        time = news_item.get('publishedAt')
        url = news_item.get('url')
        image = news_item.get('urlToImage')
        title = news_item.get('title')

        if url:
            news_object = News(author,description,time,url,image,title)
            news_results.append(news_object)

    return news_results




def get_category(categ_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = base_url.format(categ_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_results(get_cartegory_list)

    return get_cartegory_results


def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&from=2022-04-30&language=en&sortBy=publishedAt&apiKey={}'.format(news_name,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_results(search_news_list)


    return search_news_results

