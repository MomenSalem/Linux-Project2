# Momen Salem- 1200034
# Mohammad Dallash - 1200937
import os
import library


# function to print the Library books after loaded it from files
def print_books(lms):
    if not lms:
        print("There is no Books in Library")
        return 0  # the library is empty
    check_archive = check_number_copy = 0
    for book in lms:
        print("Title :", book.title)
        print("Publisher :", book.publisher)
        print("ISBN-10 :", book.isbn_10)
        print("ISBN-13 :", book.isbn_13)
        for op in book.options:
            if op is not None:
                if op[0].strip().lower() == "is archived":  # this condition and the bellow condition also is to check
                    # if is archived printed or no (just for printing purpose)
                    if book.is_archived == 0:
                        op[1] = "No"
                    else:
                        op[1] = "Yes"
                    check_archive = 1
                if op[0].strip().lower() == "number of copies":
                    op[1] = str(book.copies)
                    check_number_copy = 1
                print(op[0], ":", op[1])
        if check_number_copy == 0:
            print("Number of copies :", book.copies)
        if check_archive == 0:
            if book.is_archived == 0:
                print("Is Archived : No")
            else:
                print("Is Archived : Yes")
        print()  # to separate between books
    return 1  # return one indicate that there are books in library


def search_books(lms):
    result = []
    print("-------------------------------------------------------------------------------")
    titlesearch = input("Enter the title for book or 0 if you dont want to search for title")
    publishersearch = input("Enter the publisher for book or 0 if you dont want to search for publisher")
    isbn10search = input("Enter the isbn-10 number for book or 0 if you dont want to search for isbn-10 number")
    isbn13search = input("Enter the isbn-13 number for book or 0 if you dont want to search for isbn-13 number")
    optionsearch = input("Enter any option name to search for it or 0 if you dont want to search for option (as "
                         "optinon=value manner)")

    for book in lms:
        if titlesearch != '0' and titlesearch == book.title:
            result.append(book)
        if publishersearch != '0' and publishersearch == book.publisher:
            if book not in result:  # check if the book exist before to ignore the duplicate don't add it
                result.append(book)
        if isbn10search != '0' and isbn10search == book.isbn_10:
            if book not in result:
                result.append(book)
        if isbn13search != '0' and isbn13search == book.isbn_13:
            if book not in result:
                result.append(book)
    first_enter = 1
    if optionsearch != '0':  # this condition is to check if the user want to search for book using any option
        check_op = 1
        while check_op != '0':  # while loop to let user check for many options if he wants
            if first_enter == 1:
                for book in lms:
                    op = optionsearch.strip().split('=')
                    for j in book.options:
                        if j[0].strip().lower() == op[0].lower():
                            if j[1].strip().lower() == op[1].lower():
                                if book not in result:
                                    result.append(book)
                                    first_enter = 0
            else:
                if result:
                    for b in result:
                        op = optionsearch.strip().split('=')
                        for j in b.options:
                            if j[0].strip().lower() == op[0].lower():
                                if j[1].strip().lower() == op[1].lower():
                                    if b not in result:
                                        result.append(b)

            check_op = input("Enter any other option (as option=value manner) or 0 if you dont")
            # optionsearch = check_op
    print("===============================================")

    if result:
        print("Search Results:")
        for book in result:
            print("Title:", book.title)
            print("Publisher:", book.publisher)
            print("ISBN-10:", book.isbn_10)
            print("ISBN-13:", book.isbn_13)
            check_archive = check_number_copy = 0
            for op in book.options:
                if op is not None:
                    if op[0].strip().lower() == "is archived":  # this condition and the bellow condition also is to
                        # check if is archived printed or no (just for printing purpose)
                        if book.is_archived == 0:
                            op[1] = "No"
                        else:
                            op[1] = "Yes"
                        check_archive = 1
                    if op[0].strip().lower() == "number of copies":
                        op[1] = str(book.copies)
                        check_number_copy = 1
                    print(op[0], ":", op[1])
            if check_number_copy == 0:
                print("Number of copies :", book.copies)
            if check_archive == 0:
                if book.is_archived == 0:
                    print("Is Archived : No")
                else:
                    print("Is Archived : Yes")
            print()
        print("===============================================")
        choice = input("Do you want to save the search results to a file? (Y/N): ")
        if choice.upper() == 'Y':
            save_file = input("Enter the name of the file to save the search results: ")
            with open(save_file, 'w') as file:  # print the result to file
                for book in result:
                    file.write("Title : {}\n".format(book.title))
                    file.write("Publisher : {}\n".format(book.publisher))
                    file.write("ISBN-10 : {}\n".format(book.isbn_10))
                    file.write("ISBN-13 : {}\n".format(book.isbn_13))
                    file.write("Number of Copies : {}\n".format(book.copies))
                    file.write("Is Archived : {}\n".format(book.copies))
                    if book.options:
                        for op in book.options:
                            statment = op[0] + ':' + op[1] + '\n'
                            file.write(statment)
                    file.write("\n")
            print("Search results saved to file named (", save_file, ")")
        else:
            print("The saving to file operation is not confirmed")
        print("---------------------------------------")

    else:
        print("No books found matching the search query.")
        print("===============================================")


def edit_books(lms):
    print("-------------------------------------------------------------------------------")
    print("choose from bellow list")
    print("1. edit book from file")
    print("2. edit book using its ISBNs")
    edit_choice = input()
    copy_library = []  # list to add the books obtained from file
    if edit_choice.isnumeric():
        if int(edit_choice) == 1:
            edit_file_name = input("Please Enter the file name")
            if os.path.exists(edit_file_name):
                with open(edit_file_name, 'r') as file:  # print the result to file (if it is not exist then create one)
                    lines = file.readlines()
                    option = []
                    for line in lines:
                        copy = 1
                        is_archived = 0
                        # first we must split each line as (:) delimiter and then save the important info of each book
                        book_info = line.strip().split(':', 1)
                        if book_info[0].replace(" ", "").lower() == 'title':
                            title = book_info[1].lstrip()
                        elif book_info[0].replace(" ", "").lower() == 'publisher':
                            publisher = book_info[1].lstrip()
                        elif book_info[0].replace(" ", "").lower() == 'isbn-10':
                            isbn_10 = book_info[1].lstrip()
                        elif book_info[0].replace(" ", "").lower() == 'isbn-13':
                            isbn_13 = book_info[1].lstrip()
                        elif book_info[0].strip().lower() == 'number of copies':
                            copy = book_info[1].lstrip()
                        elif book_info[0].strip().lower() == 'is archived':
                            if book_info[1].lstrip().lower() == 'no':
                                is_archived = 0
                            else:
                                is_archived = 1
                        elif book_info[0] == '':
                            copy_option = option.copy()  # copy the option list because we want to empty it for the next book
                            lib = library.Library(title, publisher, isbn_10, isbn_13, copy_option, int(copy),
                                                  int(is_archived), 0)
                            adding_check = lib.add_book(copy_library, title, publisher, isbn_10, isbn_13, copy_option,
                                                        int(copy),
                                                        int(is_archived))
                            if adding_check == 1:
                                copy_library.append(lib)  # add this new book to library
                                option.clear()
                                title = publisher = isbn_10 = isbn_13 = None  # empty all values to check if next book does
                                # not has this important information (if the book does not have this information don't add
                                # it to library)
                        else:  # adding this information as option info for this book
                            option.append(book_info)
                check_library = print_books(copy_library)
                if check_library == 1:
                    isbn10 = input("Please Enter the ISBN-10 for the book to edit it")
                    isbn13 = input("Please Enter the ISBN-13 for the book to edit it")
                    check_book = 0
                    for book in copy_library:
                        if book.isbn_10 == isbn10 and book.isbn_13 == isbn13:
                            check_book = 1  # the book is found so change the variable for printing the result
                            book_title = input("Enter the new book (title) or 0 if you dont not want to update it")
                            book_publisher = input(
                                "Enter the new book (publisher) or 0 if you dont not want to update it")
                            book_isbn10 = input(
                                "Enter the new (ISBN-10) for the book or 0 if you dont not want to update it")
                            book_isbn13 = input(
                                "Enter the new (ISBN-13) for the book or 0 if you dont not want to update it")
                            book_option = []
                            for op in book.options:
                                if op is not None:
                                    book_option.append(
                                        input("Enter the new option (" + op[0].strip() + ") for the book or 0 if you dont not "
                                                                                "want to update it"))
                            confirm = input("Do you want to confirm the updated result(Y/N)?")
                            if confirm.upper() == 'Y':
                                if book_title != '0':
                                    book.title = book_title
                                if book_publisher != '0':
                                    book.publisher = book_publisher
                                if book_isbn10 != '0':
                                    book.isbn_10 = book_isbn10
                                if book_isbn13 != '0':
                                    book.isbn_13 = book_isbn13
                                counter = 0
                                for edit_option in book_option:
                                    if edit_option is not None:
                                        if edit_option != '0':
                                            book.options[counter][1] = book_option[counter]
                                        counter += 1
                                write_result_to_file(copy_library, edit_file_name)
                                print("The result is changed properly and writen to file name (", edit_file_name, ")")
                            else:
                                print("The changing operation is not confirmed")
                    if check_book == 0:
                        print("There is no book with ISBN-10 = ", isbn10, " , ISBN-13 = ", isbn13, " in the library")
                    print("--------------------------------------------------")
                else:
                    print("There is No book in file called (", edit_file_name, ")")
                    print("--------------------------------------------------")
            else:
                print("The file does not exist!")
                print("---------------------------------------")


        elif int(edit_choice) == 2:
            if print_books(lms):
                isbn10 = input("Please Enter the ISBN-10 for the book to edit it")
                isbn13 = input("Please Enter the ISBN-13 for the book to edit it")
                check_book = 0
                for book in lms:
                    if book.isbn_10 == isbn10 and book.isbn_13 == isbn13:
                        check_book = 1  # the book is found so change the variable for printing the result
                        book_title = input("Enter the new book (title) or 0 if you dont not want to update it")
                        book_publisher = input("Enter the new book (publisher) or 0 if you dont not want to update it")
                        book_isbn10 = input("Enter the new (ISBN-10) for the book or 0 if you dont not want to update it")
                        book_isbn13 = input("Enter the new (ISBN-13) for the book or 0 if you dont not want to update it")
                        book_option = []
                        for op in book.options:
                            if op is not None:
                                if op[0].strip().lower() != "is archived" and op[0].strip().lower() != "number of copies" :
                                    book_option.append(
                                        input("Enter the new option (" + op[0].strip() + ")for the book or 0 if you dont not "
                                                                                "want to update it"))
                        confirm = input("Do you want to confirm the updated result(Y/N)?")
                        if confirm.upper() == 'Y':
                            if book_title != '0':
                                book.title = book_title
                            if book_publisher != '0':
                                book.publisher = book_publisher
                            if book_isbn10 != '0':
                                book.isbn_10 = book_isbn10
                            if book_isbn13 != '0':
                                book.isbn_13 = book_isbn13
                            counter = 0
                            for edit_option in book_option:
                                if edit_option is not None:
                                    if edit_option != '0':
                                        book.options[counter][1] = book_option[counter]
                                    counter += 1
                            print("The book is changed properly in the library")
                        else:
                            print("The changing operation is not confirmed")
                if check_book == 0:
                    print("There is no book with ISBN-10 = ", isbn10, " , ISBN-13 = ", isbn13, " in the library")
                print("-------------------------------------------------------------------------------")
        else:
            print("You Must choose 1 or 2 only")
            edit_books(lms)
    else:
        print("You Must Enter 1 or 2 only as a digit")
        edit_books(lms)


def archive_book(lms):
    isbn10 = input("Please Enter the ISBN-10 for the book to archive it")
    isbn13 = input("Please Enter the ISBN-13 for the book to archive it")
    check_book = 0
    confirm = 'N'
    for book in lms:
        if book.isbn_10 == isbn10 and book.isbn_13 == isbn13:
            check_book = 1  # the book is found so change the variable for printing the result
            if book.copies > 1:
                print("There are ", book.copies, " copy for the book")
                num_copy = input("Enter number of copy to archive it")
                while int(num_copy) > book.copies or 0 >= int(num_copy):
                    num_copy = input("There is no copy for this book and you must enter a positive digit only!\nEnter "
                                     "number of copy")
                confirm = input("The book is found do you want to archive it (Y/N)?")
                if confirm.upper() == 'Y':
                    book.is_archived = 1
                    book.copies = int(book.copies) - int(num_copy)
            elif book.copies == 1:
                confirm = input("The book is found do you want to archive it (Y/N)?")
                if confirm.upper() == 'Y':
                    book.is_archived = 1
                    book.copies -= 1  # the book is archive so change the number of copy for it
            else:
                print("The book is already in archive and there is no copy available")
                break
            if confirm.upper() == 'Y':
                book.is_archived = 1  # now the book is in archive
                print("Book with ISBN-10 = ", isbn10, "& ISBN-13 = ", isbn13, " archived properly")
            else:
                print("Archiving book operation not confirmed")
    if check_book == 0:
        print("There is no book with ISBN-10 = ", isbn10, " , ISBN-13 = ", isbn13, " in the library")
    print("---------------------------------------")


def print_archived_book(lms):
    print("---------------------------------------")
    print("Books in Archive :")
    is_empty = 1
    check_print_archive = check_print_number_of_copy = 0
    for book in lms:
        if book.is_archived == 1:
            is_empty = 0  # there is archived books in lms so return 0 (the list not empty)
            print("Title :", book.title)
            print("Publisher :", book.publisher)
            print("ISBN-10 :", book.isbn_10)
            print("ISBN-13 :", book.isbn_13)
            for op in book.options:
                if op is not None:
                    if op[0].strip().lower() == "is archived":  # this condition and the bellow condition also is to
                        # check if is archived printed or no (just for printing purpose)
                        if book.is_archived == 0:
                            op[1] = "No"
                        else:
                            op[1] = "Yes"
                        check_print_archive = 1
                    if op[0].strip().lower() == "number of copies":
                        op[1] = str(book.copies)
                        check_print_number_of_copy = 1
                    print(op[0], ":", op[1])
            if check_print_number_of_copy == 0:
                print("Number of copies :", book.copies)
            if check_print_archive == 0:
                if book.is_archived == 0:
                    print("Is Archived : No")
                else:
                    print("Is Archived : Yes")
            print("--------")
    return is_empty


def delete_book(lms):
    check_empty = print_archived_book(lms)
    if check_empty == 0:
        isbn10 = input("Enter the ISBN-10 for the book to delete it")
        isbn13 = input("Enter the ISBN-13 for the book to delete it")
        is_deleted = 0  # variable to check if the book is deleted to print the proper statement
        for book in lms:
            if book.is_archived == 1 and book.isbn_10 == isbn10 and book.isbn_13 == isbn13:
                confirm = input("The book is found do you want to delete it (Y/N)?")
                if confirm.upper() == 'Y':
                    if book.copies > 0:# check if there is copy (that means not all copies in archive so delete
                        # archive copies only)
                        book.is_archived = 0
                    else:
                        lms.remove(book)
                    print("Book with ISBN-10 = ", isbn10, "& ISBN-13 = ", isbn13, " deleted properly")
                    is_deleted = 1
                else:
                    print("Deleting book operation not confirmed")
        if is_deleted == 0:
            print("There is no book with ISBN-10 = ", isbn10, " , ISBN-13 = ", isbn13, " in archive")
    else:
        print("There is no book in archive")
    print("---------------------------------------")


def print_publisher_book(lms, publisher):
    num_books = 0
    check_num = 0
    counter = 0  # counter for printing books title
    books_publisher = []
    for book in lms:
        if book.publisher.lower() == publisher.lower() and book.is_read == 0:
            check_num = 1
            num_books += 1
            book.is_read = 1
            books_publisher.append(book)

    if check_num == 1:
        print("--------------------------------------------------")
        print("Number of books by publisher ", publisher, " = ", num_books)
        for book in books_publisher:
            counter += 1
            print(counter, "- Book Title : ", book.title, " | ISBN-10 = ", book.isbn_10, " , ISBN-13 = ", book.isbn_13)


def print_year_book(lms, year):
    num_books = 0
    check_num = 0
    counter = 0  # counter for printing books title
    books_in_year = []
    for book in lms:
        if book.options:
            for op in book.options:
                if op[0].strip().lower() == 'year' and int(op[1]) == int(year) and book.is_read == 0:
                    check_num = 1
                    num_books += 1
                    book.is_read = 1
                    books_in_year.append(book)
    if check_num == 1:
        print("--------------------------------------------------")
        print("Number of books published in year ", year, " = ", num_books)
        for book in books_in_year:
            counter += 1
            print(counter, "- Book Title : ", book.title, " | ISBN-10 = ", book.isbn_10, " , ISBN-13 = ", book.isbn_13)


def generate_reports(lms):
    num_books = 0  # this variable is for the whole number of books in library
    num_different_books = len(lms)  # the number of different books in library (without copies)
    num_archived = 0
    for book in lms:
        num_books += book.copies
        if book.is_archived == 1:
            num_archived += 1
    print("############################################################")
    print("Number of books in library = ", num_books)
    print("Number of different books in library = ", num_different_books)
    print("Number of books in archive = ", num_archived)
    num_year = 0  # number of books newer than year initialized to zero
    year = input("Enter year to find the number of books published newer than this year")
    for book in lms:
        if book.options:
            for op in book.options:
                if op[0].strip().lower() == 'year' and int(op[1]) > int(year):
                    num_year += 1
    print("Number of books newer than year ", year, " = ", num_year)
    for book in lms:
        print_publisher_book(LMS, book.publisher)
    print("--------------------------------------------------")

    for book in lms:
        book.is_read = 0  # empty this choice so if user enter again then the result is obtained
    for book in lms:
        if book.options:
            for op in book.options:
                if op[0].strip().lower() == 'year':
                    print_year_book(LMS, int(op[1]))
    print("--------------------------------------------------")
    for book in lms:
        book.is_read = 0  # empty this choice so if user enter again then the result is obtained


def write_result_to_file(lms, file_name):
    with open(file_name, 'w') as file:  # print the result to file (if it is not exist then create one)
        for book in lms:
            file.write("Title : {}\n".format(book.title))
            file.write("Publisher : {}\n".format(book.publisher))
            file.write("ISBN-10 : {}\n".format(book.isbn_10))
            file.write("ISBN-13 : {}\n".format(book.isbn_13))
            file.write("Number of Copies : {}\n".format(book.copies))
            check_archive = 'No'
            if book.is_archived == 1:
                check_archive = 'Yes'
            file.write("Is Archived : {}\n".format(check_archive))
            if book.options:
                for op in book.options:
                    statment = op[0] + ' : ' + op[1] + '\n'
                    file.write(statment)
            file.write("\n")


# Create the library management system list which is empty at first
LMS = []
basic_file = 'lms.txt'  # the basic file that when program start must load it
if os.path.exists(basic_file):  # check if file exists
    with open(basic_file, 'r') as file:  # this line is for open and close the file automatically (using with)
        lines = file.readlines()
        option = []
        copy = 1
        is_archived = 0
        for line in lines:
            # first we must split each line as (:) delimiter and then save the important info of each book
            book_info = line.strip().split(':', 1)
            if book_info[0].replace(" ", "").lower() == 'title':
                title = book_info[1].lstrip()
            elif book_info[0].replace(" ", "").lower() == 'publisher':
                publisher = book_info[1].lstrip()
            elif book_info[0].replace(" ", "").lower() == 'isbn-10':
                isbn_10 = book_info[1].lstrip()
            elif book_info[0].replace(" ", "").lower() == 'isbn-13':
                isbn_13 = book_info[1].lstrip()
            elif book_info[0].strip().lower() == 'number of copies':
                copy = book_info[1].lstrip()
            elif book_info[0].strip().lower() == 'is archived':
                if book_info[1].lstrip().lower() == 'no':
                    is_archived = 0
                else:
                    is_archived = 1
            elif book_info[0] == '':
                copy_option = option.copy()  # copy the option list because we want to empty it for the next book
                lib = library.Library(title, publisher, isbn_10, isbn_13, copy_option, int(copy), int(is_archived), 0)
                adding_check = lib.add_book(LMS, title, publisher, isbn_10, isbn_13, copy_option, int(copy),
                                            is_archived)
                if adding_check == 1:
                    LMS.append(lib)  # add this new book to library
                option.clear()
                title = publisher = isbn_10 = isbn_13 = None  # empty all values to check if next book does
                # not has this important information (if the book does not have this information don't add
                # it to library)

            else:  # adding this information as option info for this book
                option.append(book_info)
    print("-------------------------------------------------------------------------------")
    print("The books information that were loaded from basic file called (lms.txt):")
    print_books(LMS)
    print("-------------------------------------------------------------------------------")
else:
    print("The basic file (lms.txt) is empty so there is no book stored previously in library management system")

while True:
    print("Library Management System")
    print("1. Add new books to the library collection")
    print("2. Search for books within the library collection")
    print("3. Edit the information of existing books")
    print("4. Archive books")
    print("5. Remove books from the LMS")
    print("6. Generate reports about the books available in the LMS")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        print("-------------------------------------------------------------------------------")
        file_name = input("provide the name of the file contains books information: ")
        # Read the file and extract book information
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:  # this line is for open and close the file automatically
                lines = file.readlines()
                option = []
                title = publisher = isbn_10 = isbn_13 = None  # define the needed variables which will be used bellow
                for line in lines:
                    copy = 1  # always initialized the first number of copy for book to one
                    # first we must split each line as (:) delimiter and then save the important info of each book
                    book_info = line.strip().split(':', 1)
                    if book_info[0].replace(" ", "").lower() == 'title':
                        title = book_info[1].lstrip()
                    elif book_info[0].replace(" ", "").lower() == 'publisher':
                        publisher = book_info[1].lstrip()
                    elif book_info[0].replace(" ", "").lower() == 'isbn-10':
                        isbn_10 = book_info[1].lstrip()
                    elif book_info[0].replace(" ", "").lower() == 'isbn-13':
                        isbn_13 = book_info[1].lstrip()
                    elif book_info[0] == '':
                        copy_option = option.copy()
                        lib = library.Library(title, publisher, isbn_10, isbn_13, copy_option, copy, 0, 0)
                        adding_check = lib.add_book(LMS, title, publisher, isbn_10, isbn_13, copy_option, copy, 0)
                        if adding_check == 1:
                            LMS.append(lib)  # add this new book to library
                        option.clear()
                        title = publisher = isbn_10 = isbn_13 = None  # empty all values to check if next book does
                        # not has this important information

                    else:  # adding this information as option info for this book
                        option.append(book_info)
            print("---------------------------------------")
            print("The books information that were loaded :")
            print_books(LMS)
            print("---------------------------------------")
        else:
            print("The file does not exist!")
            print("---------------------------------------")

    elif choice == '2':
        search_books(LMS)

    elif choice == '3':
        edit_books(LMS)

    elif choice == '4':
        archive_book(LMS)

    elif choice == '5':
        delete_book(LMS)

    elif choice == '6':
        generate_reports(LMS)

    elif choice == '7':
        print("-------------------------------------------------------------------------------")
        write_result_to_file(LMS, basic_file)
        print("The result is written properly in text called (lms.txt)")
        print("Wellcome to Our Library Management System")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
