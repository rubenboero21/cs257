# This program was written by Ruben Boero and Xiaoying Qu

# The program was adapted from code by Alex Falk and Carl Zhang's books.py file 
# https://github.com/aafalk/cs257/blob/main/books/books.py

# This code was revised by Alex Falk, Carl Zhang, Aldo Polanco, and Yiming Xia

import sys
import booksdatasource

def print_books(books_list):
    '''Prints a list of book objects'''
    if len(books_list) > 0:
        for i in books_list:
            authors = []

            for j in i.authors:
                authors.append(j.surname + ", " + j.given_name)

            print(f"{i.title} by {authors}: ({i.publication_year})")
    else:
        print('No books were found in the CSV file within the given search parameters.') 

def print_authors(authors_list):
    '''Prints a list of author objects'''
    if len(authors_list) > 0:
        for i in authors_list:
            if i.death_year != None:
                print(f"{i.surname}, {i.given_name} ({i.birth_year}-{i.death_year}): {i.books}")
            else:
                print(f"{i.surname}, {i.given_name} ({i.birth_year}-): {i.books}")

    else:
        print('No authors were found in the CSV file with that search string.') 

if len(sys.argv) < 2:
    sys.exit("Not enough arguments were input. Please use the 'help' subcommand for more information.")
else:
    subcommand = sys.argv[1]

if subcommand == 'title':
    data_source = booksdatasource.BooksDataSource('books1.csv')

    # default title search with no search string
    if len(sys.argv) == 2:
        books = data_source.books(sort_by= 'title')

        print_books(books)

    elif len(sys.argv) == 3:
        # print the help statement for the title subcommand
        if sys.argv[2] == '-h' or sys.argv[2] == '--help':
            print('python3 books.py title [-h|-t|-y] [string]\n')
            print("For additional information about the program use the 'help' subcommand.")

        # print the list of all books sorted by year
        elif sys.argv[2] == '-y' or sys.argv[2] == '--year':
            books = data_source.books(sort_by= 'year')

            print_books(books)
        
        # print the list of all books sorted explicitly by title
        elif sys.argv[2] == '-t' or sys.argv[2] == '--title':
            books = data_source.books(sort_by= 'title')

            print_books(books)
        
        # print the list of all books containing the search string sorted in the default manner
        else:
            search_str = sys.argv[2]
            books = data_source.books(search_str, 'title')

            print_books(books)

    elif len(sys.argv) == 4:
        # print the list of books containing the search string sorted by year
        if sys.argv[2] == '-y' or sys.argv[2] == '--year':
            search_str = sys.argv[3]
            books = data_source.books(search_str, 'year')

            print_books(books)

        # print the list of books containing the search string sorted explicitly by title
        elif sys.argv[2] == '-t' or sys.argv[2] == '--title':
            search_str = sys.argv[3]
            books = data_source.books(search_str, 'title')

            print_books(books)

elif subcommand == 'author':
    data_source = booksdatasource.BooksDataSource('books1.csv')

    if len(sys.argv) == 2:     
        # print a list of all author objects
        authors = data_source.authors()

        print_authors(authors)
    
    elif len(sys.argv) == 3:
        # print the help statement for author subcommand
        if sys.argv[2] == '-h' or sys.argv[2] == '--help':
            print('python3 books.py author [-h] [string]\n')
            print("For additional information about the program use the 'help' subcommand.")
        
        # print the list of authors that contain a search string
        else:
            search_str = sys.argv[2]
            authors = data_source.authors(search_str)

            print_authors(authors)

elif subcommand == 'year':
    data_source = booksdatasource.BooksDataSource('books1.csv')

    # print the help statement
    if len(sys.argv) == 3 and (sys.argv[2] == '-h' or sys.argv[2] == '--help'):
        print('python3 books.py year [-h] _ _|_ yearB|yearA _|yearA yearB\n')
        print("For additional information about the program use the 'help' subcommand.")

    # check that the correct number of arguments were passed in
    elif len(sys.argv) != 4:
        sys.exit("Either the wrong number of arguments were input or an invalid flag was entered. Please use the 'help' subcommand for more information.")
    
    # check that the arguments are of the valid type
    elif (sys.argv[2].isdigit() or sys.argv[2] == '_') and (sys.argv[3].isdigit() or sys.argv[3] == '_'):
        # print all books
        if sys.argv[2] == '_' and sys.argv[3] == '_':
            books = data_source.books_between_years()

            print_books(books)

        # print books after a given start year
        elif sys.argv[2] != '_' and sys.argv[3] == '_':
            start_year = int(sys.argv[2])
            books = data_source.books_between_years(start_year)

            print_books(books)

        # print before a given end year
        elif sys.argv[2] == '_' and sys.argv[3] != '_':
            end_year = int(sys.argv[3])
            books = data_source.books_between_years(end_year= end_year)

            print_books(books)

        # print books between 2 given years
        elif sys.argv[2] != '_' and sys.argv[3] != '_':
            start_year = int(sys.argv[2])
            end_year = int(sys.argv[3])
            books = data_source.books_between_years(start_year, end_year)

            print_books(books)
    else:
        sys.exit("An invalid argument was provided to the year subcommand. Only the '_' character or an integer is valid input.\n \nType 'python3 books.py year -h' for more information about the year subcommand.")

# print usage.txt
elif subcommand == 'help':
    # the follwing 2 lines were taken directly from Alex Falk and Carl Zhang's books.py file
    # https://github.com/aafalk/cs257/blob/main/books/books.py
    with open('usage.txt', 'r') as file:
        print(file.read())

# if this line is reached, an invalid subcommand was entered
else:
    print(f"Subcommand '{subcommand}' not recognized. Use the 'help' subcommand for more information.")
