import urllib.request,json
from .models import News

# News = news.News
# Getting api key
api_key = None
# Getting news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    # pass

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
        # print (news_results)


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
        url = news_item.get('url')
        time = news_item.get('publishedAt')
        image = news_item.get('urlToImage')
        content = news_item.get('content')
      
        
    if url:
        news_object = News(author,title,description,url,time,image,content)
        news_results.append(news_object)
        # print(news_results)

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

# def get_sources():
#     get_sources_url = 'https://newsapi.org/v2/sources?&apiKey={}'.format(api_key)
#     with urllib.request.urlopen(get_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         if get_sources_response['sources']:
#             sources_results_list = get_sources_response['sources']
#             sources_results = process_results_sources(sources_results_list)

#     return sources_results

# def process_results_sources(sources_list):
#     sources_results = []

#     for source in sources_list:
#         id = source.get('id')
#         name = source.get('name')
#         url = source.get('url')

#         source_obj = Source(id,name,url)
#         sources_results.append(source_obj)
#     return sources_results

def get_category(categ_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = base_url.format(categ_name,api_key)
    # print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_results = process_results(get_category_list)

    return get_category_results


def search_article(article_name):
    article_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article_name,api_key)
    with urllib.request.urlopen(article_news_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)

    return search_article_results

