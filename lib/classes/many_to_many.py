from collections import Counter
class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        if not author in magazine.authors:
            magazine.authors.append(author)
        magazine.all_articles.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if(not isinstance(title, str)) or not (len(title)>4 and len(title)<51):
            raise Exception("Article title invalide")
        if(hasattr(self, 'title')):
            raise Exception("Article title already set")
        self._title = title
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if(not isinstance(author, Author)):
            raise Exception("Invalide author")
        self._author = author
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if(not isinstance(magazine, Magazine)):
            raise Exception("Invalide magazine")
        self._magazine = magazine
    

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.authors = []
        self.all_articles = []
        Magazine.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if(not isinstance(name, str)) or not (len(name)>1 and len(name)<17 ):
            raise Exception("Magazine name invalide")
        self._name = name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if(not isinstance(category, str)) or (len(category)<1):
            raise Exception("category name invalide")
        self._category = category
    def articles(self):
        return self.all_articles
    def contributors(self):
        return self.authors
    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        if(len(titles)>0):
            return titles
    @classmethod
    def top_publisher(self):
        if(len(Magazine.all) == 0):
            return None
        count = 0
        magazine = None;
        for mag in Magazine.all:
            if len(mag.all_articles) > count:
                count = len(mag.all_articles)
                magazine = mag
        return magazine




class Author:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if(not isinstance(name, str)) or (len(name)<1):
            raise Exception("Author name must be string and greater than 0")
        self._name = name
    def articles(self):
        return [article for article in Article.all if article.author == self]
    def magazines(self):
        return [magazine for magazine in Magazine.all if self in magazine.authors]
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    def topic_areas(self):
        magazines = self.magazines()
        areas = list({magazine.category for magazine in magazines})
        if(len(areas) == 0):
            return None
        return areas

