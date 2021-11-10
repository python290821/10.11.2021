'''
create a Book class. now, create an instance of your
favorite book with the following data fields:
title, author, genre, year_of_publish, no_of_pages
 (1) create the instance data using dictionary [for example:
      myBook.__dict__[‘year_of_publish’] = 1961]
 (2) create the instance data using dot
     [for example: myBook.title = ‘catch 22’]
 (3) create a method which creates a new books instance
     and data (see the create_Person method we did in lesson)
'''
class Book():
    pass

def create_book(title, author, year_of_publish, genre, no_of_pages):
    book = Book()
    book.title = title
    book.author = author
    book.year_of_publish = year_of_publish
    book.genre = genre
    book.number_of_pages = no_of_pages
    return book


# title, author, genre, year_of_publish, no_of_pages
myBook = Book()
myBook.__dict__['title'] = "Harry Potter and the Sorcerer's Stone"
myBook.__dict__['author'] = 'J.K.rowling'
myBook.__dict__['year_of_publish'] = 1999
myBook.__dict__['number_of_pages'] = 1003
myBook.__dict__['1genre'] = 'fantazy'

myBook_again = Book()
myBook_again.title = "Harry Potter and the Sorcerer's Stone"
myBook_again.author = 'J.K.rowling'
myBook_again.year_of_publish = 1999
myBook_again.genre = 'fantazy'
myBook_again.number_of_pages = 1003

my_book_fun = create_book('J.K.rowling', \
                          'Harry Potter and the Sorcerer\'s Stone'
                          , 1999, 'fantazy', 1003)
print(my_book_fun.__dict__)




