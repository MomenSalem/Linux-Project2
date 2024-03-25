# Momen Salem- 1200034
# Mohammad Dallash - 1200937

class Book:
    def __init__(self, title, publisher, isbn10, isbn13, options):
        self.title = title
        self.publisher = publisher
        self.isbn_10 = isbn10  # may isbn be list isbn[2]
        self.isbn_13 = isbn13
        self.options = options