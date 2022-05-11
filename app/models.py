class News:
    '''
    News class to define news Objects
    '''
    news_list = []
    def __init__(self,author,title,description,url,time,image,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.time = time
        self.image = image
        self.content = content


class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,author,title,description,url,time,image,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.time = time
        self.image = image
        self.content = content
        

# class Source:
#     sources_list = []
#     def __init__(self,id,name,url):
#         self.id = id
#         self.name = name
#         self.url = url
#     pass

   


