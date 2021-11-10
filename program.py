class Book():
    # constructor
    def __init__(self, title, author, year_of_publish, genre, no_of_pages):
        # self = Book()
        self.title = title
        self.author = author
        self.year_of_publish = year_of_publish
        self.genre = genre
        self.number_of_pages = no_of_pages
        # return self

cooking_book = Book('cooking in 1 hour', 'rut', 2020, 'food', 155)
racing_car = Book('formula 1', 'john', 2022, 'fast', 300)

print(cooking_book.__dict__)

