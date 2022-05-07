
import urllib.request,json
from .models import news


News = news.News

# Getting api key
api_key = None['NEWS_API_KEY']

# Getting news base url

base_url = None["NEWS_API_BASE_URL"]

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    pass

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
        title = news_item.get('title')
        description = news_item.get('description')
        time = news_item.get('publishedAt')
        url = news_item.get('url')
        image = news_item.get('urlToImage')
        content = news_item.get('content')

        if url:
            news_object = News(author,title,description,time,url,image,content)
            news_results.append(news_object)

    return news_results

# def get_article_by_source(source_name):
#     get_source_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source_name,api_key)
#     print(get_source_article_url)
#     with urllib.request.urlopen(get_source_article_url) as url:
#         get_data = url.read()
#         get_response = json.loads(get_data)

#         results = None
#         if get_response['articles']:
#             results_list = get_response['articles']
#             results = process_results(results_list)
#     return results

# def process_results(articles_list):
#     articles_results = []
#     for article in articles_list:
#         author = article.get('author')
#         title = article.get('title')
#         description = article.get('description')
#         url = article.get('url')
#         urlToImage = article.get('urlToImage')
#         publishedAt = article.get('publisheAt')
#         content = article.get('content')
        
#         if urlToImage:
#             article_object = News(author,title,description,url,urlToImage,publishedAt,content)
#             articles_results.append(article_object)

#     return articles_results



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


def search_article(article_name):
    article_news_url = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'.format(article_name,api_key)
    with urllib.request.urlopen(article_news_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)


    return search_article_results

