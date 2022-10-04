#!/usr/bin/env python3

# Interface implemented by Ruben and Xiaoying with the help of an example provided by Alex Falk and 
# Carl Zhang's booksdatasoure.py file: 
# https://github.com/aafalk/cs257/blob/main/books/booksdatasource.py

'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv

def get_title(csv_substring):
    '''Returns the title of a book given the substring of a csv file in which it appears.'''
    title = csv_substring
    return title

def get_pub_year(csv_substring):
    '''Returns the publication year of a book given the substring of a csv file in which it appears.'''
    pub_year = csv_substring
    return pub_year

def get_birth_year(csv_substring):
    '''Returns the birth year of an author given the substring of a csv file in which it appears.'''
    author_info = csv_substring.split(' ') 
    # if there is an author with 1 last name
    if len(author_info) == 3:
        temp_yrstr = author_info[-1][1:-1]
        return temp_yrstr.split('-')[0]
    # if there is an author with 2 last names
    elif len(author_info) > 3: 
        temp_yrstr = author_info[-1][1:-1]
        return temp_yrstr.split('-')[0]
    # if there is no birth year given
    elif (len(temp_yrstr.split('-')) < 2):
        return None
    
def get_death_year(csv_substring):
    '''Returns the death year of an author given the substring of a csv file in which it appears.
       Returns None if there is no death year.'''
    author_info = csv_substring.split(' ') 
    temp_yrstr = author_info[-1][1:-1]
    year_substrings = temp_yrstr.split('-')

    # if the author has a death year
    if len(year_substrings[1]) > 0:
        return year_substrings[1]
    # if the author has no death year
    else:
        return None

def get_surname(csv_substring):
    '''Returns the surname of an author given the substring of a csv file in which it appears.'''
    s = csv_substring.split(' ') 
    if len(s) > 3:
        return s[1] + ' ' +s[2]
    else:
        return  s[1]

def get_given_name(csv_substring):
    '''Returns the given name of an author given the substring of a csv file in which it appears.'''
    s = csv_substring.split(' ')
    return s[0]

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None, books=[]):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year
        self.books = books

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

    # For sorting authors, you could add a "def __lt__(self, other)" method
    # to go along with __eq__ to enable you to use the built-in "sorted" function
    # to sort a list of Author objects.

    def __lt__(self, other):
        if self.surname == other.surname:
            return self.given_name < other.given_name
        else:
            return self.surname < other.surname

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

    # For sorting books, you could add a "def __lt__(self, other)" method
    # to go along with __eq__ to enable you to use the built-in "sorted" function
    # to sort a list of Book objects.
    #   - I used sorted() instead
        
class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
            '''
        # the following sources were used to get the file reader working
        # https://stackoverflow.com/questions/45120726/how-to-read-csv-file-lines-and-split-elements-in-line-into-list-of-lists
        # https://docs.python.org/3/library/csv.html
        file = open(books_csv_file_name)
        reader = csv.reader(file, delimiter= ',')
        
        self.authors_list = [] # list of author objects
        self.books_list = [] # list of book objects

        for line in reader:
            title = get_title(line[0])
            pub_year = get_pub_year(line[1])

            # a list to store all the authors who have written a given book (used in Book obj construction)
            written_by = []

            # the following line and strategy was adapted from Alex Falk and Carl Zhang's 
            # booksdatasource.py file 
            # https://github.com/aafalk/cs257/blob/main/books/booksdatasource.py
            author_fields = line[2].split(' and ')
            
            for author in author_fields:

                surname = get_surname(line[2])
                given_name = get_given_name(line[2])
                birth_year = get_birth_year(line[2])
                death_year = get_death_year(line[2])

                # we don't need a temp author, just search by the surname and given name that we already have
                temp_author = Author(surname, given_name, birth_year, death_year, [])
                
                # only add the author object to authors_list if that author is not already 
                # in the list
                temp_author_seen = False

                for author in self.authors_list:
                    # if author does not already exist, add it to the list
                    if author == temp_author:
                        temp_author_seen = True
                        # update the already existing author's list of written books
                        author.books.append(title)
                        # also update the corresponding book object's list of authors
                        written_by.append(temp_author)
                        break # break out of the for loop bc the author has been found

                # add an author to the list if they are not already in the list
                if not (temp_author_seen):
                    temp_author.books.append(title)
                    self.authors_list.append(temp_author)
                    written_by.append(temp_author)

            # create the Book object
            self.books_list.append(Book(title, pub_year, written_by))
            
        file.close()

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''

        complete_list = self.authors_list
        search_list = []

        # if no search text, sort and return all authors
        if (search_text == None):
            complete_list.sort()
            return complete_list

        # else, search for the authors to add, then sort and return the list of authors
        else:
            # making everything lower case for case-insensitivity
            search_text = search_text.lower()
            for author in complete_list:
                lower_surname = author.surname.lower()
                lower_given_name = author.given_name.lower()
                lower_full_name = lower_given_name + " " + lower_surname
                if (search_text in lower_full_name):
                    search_list.append(author)
            search_list.sort()
            return search_list

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        complete_list = self.books_list
        search_list = []

        # if there is no search term, sort and return out all books
        if (search_text == None and sort_by == 'title'):
            sorted_list = sorted(complete_list, key = lambda b: (b.title, b.publication_year))
            return sorted_list

        # else if it's specified, sort all books by year
        elif (search_text == None and sort_by == 'year'):
            sorted_list = sorted(complete_list, key = lambda b: (b.publication_year, b.title))
            return sorted_list

        # else if there is a search string, find all book titles that contain the string, sort them by 
        # title and return them
        elif (search_text != None and sort_by == 'title'):
            # making everything lower case for case-insensitivity
            search_text = search_text.lower()
            for book in complete_list:
                lower_title = book.title.lower()
                if (search_text in lower_title):
                    search_list.append(book)
            sorted_list = sorted(search_list, key = lambda b: (b.title, b.publication_year))
            return sorted_list

        # else if there is a search string, find all book titles that contain the string, sort them by 
        # year and return them
        elif (search_text != None and sort_by == 'year'):
            # making everything lower case for case-insensitivity
            search_text = search_text.lower()
            for book in complete_list:
                lower_title = book.title.lower()
                if (search_text in lower_title):
                    search_list.append(book)
            sorted_list = sorted(search_list, key = lambda b: (b.publication_year, b.title))
            return sorted_list

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        complete_list = self.books_list
        search_list = []

        # if no start or end year is provided, sort all books by year, and return them
        if (start_year == None and end_year == None):
            sorted_list = sorted(complete_list, key = lambda b: (b.publication_year, b.title))
            return sorted_list

        # if just an end year is provided, sort books by year, then return all books that were 
        # published before or during the end year
        elif (start_year == None and end_year != None):
            for book in complete_list:
                if (int(book.publication_year) <= end_year):
                    search_list.append(book)
            sorted_list = sorted(search_list, key = lambda b: (b.publication_year, b.title))
            return sorted_list

        # if just an start year is provided, sort books by year, then return all books that were 
        # published after or during the start year
        elif (start_year != None and end_year == None):
            for book in complete_list:
                if (int(book.publication_year) >= start_year):
                    search_list.append(book)
            sorted_list = sorted(search_list, key = lambda b: (b.publication_year, b.title))
            return sorted_list
        
        # if both years are provided, sort books by year, then return all books that were published
        # in between or during those years
        else:
            for book in complete_list:
                if (int(book.publication_year) <= end_year and int(book.publication_year) >= start_year):
                    search_list.append(book)
            sorted_list = sorted(search_list, key = lambda b: (b.publication_year, b.title))
            return sorted_list

