from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    # abstractmethod
    def display(self): 
        pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
    
    def display(self):
        print('{0}: {1}'.format('Title', self.title))
        print('{0}: {1}'.format('Author', self.author))
        print('{0}: {1}'.format('Price', self.price))
title=input()