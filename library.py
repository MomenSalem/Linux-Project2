# Momen Salem- 1200034
# Mohammad Dallash - 1200937
import book


class Library(book.Book):
    def __init__(self, title, publisher, isbn10, isbn13, options, copies, is_archived, is_read):
        super().__init__(title, publisher, isbn10, isbn13, options)
        self.copies = copies
        self.is_archived = is_archived  # check if the book is archived or not
        self.is_read = is_read  # variable used in report section to check if the book is read before (no duplicate)

    def add_book(self, lms, title, publisher, isbn10, isbn13, options, copies, is_archive):
        if title is None or publisher is None or isbn10 is None or isbn13 is None:
            return 0
        for lib in lms:
            if lib.isbn_10 == isbn10:
                choice = input(
                    "Book with isbn_10 = (" + lib.isbn_10 + ") already exists in the library. press (r) to replace "
                                                            "its properties")
                if choice.lower() == 'r':
                    lib.title = title
                    lib.publisher = publisher
                    lib.isbn10 = isbn10
                    lib.isbn13 = isbn13
                    lib.options = options
                    lib.copies = copies
                    lib.is_archived = is_archive  # for first time the book is not archived
                    lib.is_read = 0
                else:
                    lib.copies += 1
                return 0

        return 1  # return 1 which mean add this book it is new to library (no other one has the same isbn)
