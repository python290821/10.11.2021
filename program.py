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