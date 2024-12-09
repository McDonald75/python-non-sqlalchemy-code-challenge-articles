class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        if hasattr(self, "_name"):
            raise Exception("Cannot modify name after instantiation")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    _instances = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string of 2 to 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._instances.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string of 2 to 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls._instances:
            return None
        return max(cls._instances, key=lambda mag: len(mag._articles), default=None)

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise ValueError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters inclusive")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        self._magazine = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("title is immutable")

class Article:
    all =[]
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string of 5 to 50 characters")
        if hasattr(self, "_title"):
            raise Exception("Cannot modify title after instantiation")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)
        self.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine")
        self._magazine = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self):
        raise Exception('cant set title')
# Article.all = []
# author = Author("Carry Bradshaw")
# magazine_1 = Magazine("Vogue", "Fashion")
# magazine_2 = Magazine("AD", "Architecture & Design")
# article_1 = Article(author, magazine_1, "How to wear a tutu with style")
# article_2 = Article(author, magazine_2, "Dating life in NYC")
# print(len(Article.all))

author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine = Magazine("Vogue", "Fashion")
article_1 = Article(author_1, magazine, "How to wear a tutu with style")
article_2 = Article(author_1, magazine, "Dating life in NYC")
article_3 = Article(author_2, magazine, "How to be single and happy")

print(author_2.articles())