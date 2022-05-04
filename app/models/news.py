class News:

    def __init__(self,author,description,time,url,urlToimage,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = urlToimage
        self.title = title


class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,author,description,time,url,urlToimage,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = urlToimage
        self.title = title

class Source:
    """
    source class to define source objects
    """
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        