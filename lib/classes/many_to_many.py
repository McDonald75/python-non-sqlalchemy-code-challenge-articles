class Author:
    def __init__(self, name):
        self.name = name
        self.all_articles = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if(not isinstance(name, str) or len(name)==0):
            raise Exception("Name is invalid")
        if hasattr(self,'name'):
            raise Exception("Name is already defined")
        self._name = name
    def articles(self):
        return self.all_articles

class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        author.all_articles.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if(not isinstance(title, str) or not (5<=len(title)<=50)):
            raise Exception("title is invalid")
        if hasattr(self,'title'):
            raise Exception("title is already defined")
        self._title = title
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if(not isinstance(author, Author)):
            raise Exception("author is invalid")
        self._author = author
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if(not isinstance(magazine, Magazine) and not (5<=len(magazine)<=50)):
            raise Exception("magazine is invalid")
        self._magazine = magazine


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if(not isinstance(name, str) and not (2<=len(name)<=16)):
            raise Exception("Name is invalid")
        self._name = name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if(not isinstance(category, str) and len(category) == 0):
            raise Exception("Category is invalid")
        self._category = category
        
