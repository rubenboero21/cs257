#!/usr/bin/env python3
# Interface implemented by Ruben and Xiaoying

# ******* git tag books-implementation ********

# SORTING:
# sorting based on key: 
# https://www.techiedelight.com/sort-list-of-objects-python/#:~:text=A%20simple%20solution%20is%20to,only%20arguments%3A%20key%20and%20reverse.

'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv

# should we define what the input/output type are for these functions like jeff does?

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
    s = csv_substring.split(' ') 
    # if there is an author with 1 last name
    if len(s) == 3:
        temp_yrstr = s[-1][1:-1]
        return temp_yrstr.split('-')[0]
    # if there is an author with 2 last names
    elif len(s) > 3: 
        temp_yrstr = s[-1][1:-1]
        return temp_yrstr.split('-')[0]
    # if there is no birth year given
    elif (len(temp_yrstr.split('-')) < 2):
        return None
    
def get_death_year(csv_substring):
    '''Returns the death year of an author given the substring of a csv file in which it appears.
       Returns None if there is no death year.'''
    s = csv_substring.split(' ') 
    temp_yrstr = s[-1][1:-1]
    year_substrings = temp_yrstr.split('-')

    # if the author has a death year
    if len(year_substrings[1]) > 0:
        return year_substrings[1]
    # if the author has no death year
    else:
        return None

def get_surname(csv_substring):
    '''Returns the surname of an author given the substring of a csv file in which it appears.'''
    # right now, we need to determine if there is more than 1 author, then pass in the parsed out single author into get_surname
    # Consider fixing this limitation
    s = csv_substring.split(' ') 
    if len(s) > 3:
        return s[1] + ' ' +s[2]
    else:
        return  s[1]

def get_given_name(csv_substring):
    '''Returns the given name of an author given the substring of a csv file in which it appears.'''
    # books with mulitple authors are already checked for before this function is called
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

    def __lt__(self, other):
        # THIS DOESNT WORK, currently only works when sorting by title

        if (self.title == other.title):
            return self.publication_year < other.publication_year
        else:
            return self.title < other.title

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
        
        # https://stackoverflow.com/questions/45120726/how-to-read-csv-file-lines-and-split-elements-in-line-into-list-of-lists
        # https://docs.python.org/3/library/csv.html
        file = open(books_csv_file_name)
        reader = csv.reader(file, delimiter= ',')
        
        # self. makes these an instance variable, and therefore accessible outside of the contructor method
        self.authors_list = [] # list of author objects
        self.books_list = [] # list of book objects

        for line in reader:
            # the get title and pub_year functions do basically nothing, does it make sense to 
            # leave them as functions to make it easier to read + be consistent, or should we
            # not have them as functions? Also, does it make sense to need to pass in the
            # substring in which they appear?
            title = get_title(line[0])
            pub_year = get_pub_year(line[1])

            # a list to store all the authors who have written a given book (used in Book obj construction)
            written_by = []

            # if there are 2 authors
            if 'and' in line[2]:
                author_str = line[2].split(' and ')
                author1 = author_str[0]
                author2 = author_str[1]

                surname1 = get_surname(author1)
                given_name1 = get_given_name(author1)
                birth_year1 = get_birth_year(author1)
                death_year1 = get_death_year(author1)

                surname2 = get_surname(author2)
                given_name2 = get_given_name(author2)
                birth_year2 = get_birth_year(author2)
                death_year2 = get_death_year(author2)

                # we don't need any temp authors, just search by the surname and given name that we already have
                temp_author1 = Author(surname1, given_name1, birth_year1, death_year1, [])
                temp_author2 = Author(surname2, given_name2, birth_year2, death_year2, [])
                
                # create 2 booleans to store if an author obj is already stored in the list
                temp_author1_seen = False
                temp_author2_seen = False

                # check if the author is stored in the list
                for author in self.authors_list:
                    if author == temp_author1:
                        temp_author1_seen = True

                        # updating the already existing author's list of written books
                        author.books.append(title)
                        written_by.append(temp_author1)

                    if author == temp_author2:
                        temp_author2_seen = True

                        # updating the already existing author's list of written book                            
                        author.books.append(title)
                        written_by.append(temp_author2)
                    
                    if (temp_author1_seen and temp_author2_seen):
                        break

                # add an author to the list if they are not already in the list
                if not (temp_author1_seen):
                    # edit the author object's books_written list to include the current book before appending
                    temp_author1.books.append(title)
                    self.authors_list.append(temp_author1)
                    written_by.append(temp_author1)

                if not (temp_author2_seen):
                    temp_author2.books.append(title)
                    self.authors_list.append(temp_author2)
                    written_by.append(temp_author2)
                    
            # if there is just 1 author
            else:
                surname = get_surname(line[2])
                given_name = get_given_name(line[2])
                birth_year = get_birth_year(line[2])
                death_year = get_death_year(line[2])

                # we don't need a temp author, just search by the surname and given name that we already have
                temp_author = Author(surname, given_name, birth_year, death_year, [])
                
                temp_author_seen = False

                for author in self.authors_list:
                    # if author does not already exist, add it to the list
                    if author == temp_author:
                        temp_author_seen = True
                        # updating the already existing author's list of written books
                        author.books.append(title)
                        written_by.append(temp_author)
                        break # break out of the for loop bc the author has been found

                # add an author to the list if they are not already in the list
                if not (temp_author_seen):
                    # edit the author object's books_written list to include the current book before appending
                    temp_author.books.append(title)
                    self.authors_list.append(temp_author)
                    written_by.append(temp_author)

            # create the Book object
            self.books_list.append(Book(title, pub_year, written_by))
            
        file.close() # couldnt figure out how to open the file using 'with' so just close the file here

        # these for loops are to test that the authors_list is being created correctly

        # print("List of Author objects:")
        # for authors in self.authors_list:
        #     print(authors.surname + ", " + authors.given_name)
        #     print(authors.birth_year)
        #     if not authors.death_year:
        #         print('--')
        #     else:
        #         print(authors.death_year)
        #     print(authors.books)
        #     print("========")

        # print()

        # print("List of Book objects:")
        # for books in self.books_list:
        #     print(books.title)
        #     print(books.publication_year)
        #     for i in books.authors:
        #         print(i.given_name)
        #     print("========")

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        # to handle case insensitivity, try usng casefold() or lower()

        complete_list = self.authors_list
        search_list = []

        if (search_text == None):
            complete_list.sort()
            return complete_list

        else:
            search_text = search_text.lower()
            for author in complete_list:
                lower_surname = author.surname.lower()
                lower_given_name = author.given_name.lower()
                if (search_text in lower_surname or search_text in lower_given_name):
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

        # this will need to be changed, just for testing
        if (search_text == None):
            # __lt__ for books doesnt work
            complete_list.sort()
            return complete_list

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
        return []


if __name__ == '__main__':
    #name = 'books1.csv'
    # name = '1book2authors.csv'

    #file = open("books1.csv")
    # file = open(name)

    #file = open('1book2authors.csv')

    # reader = csv.reader(file, delimiter= ',')

    # for line in reader:
    #     print(line[2])
    #     print(get_title(line[0]))
    #     print(get_pub_year(line[1]))

    # test = BooksDataSource('specifictinybooks.csv')

    # special_ch = 'GAbRiEl GaRCíA MÁrQUez'
    # print(special_ch.casefold())
    # print(special_ch.lower())

    # Anne = Author('Gaiman', 'Anne')
    # Neil = Author('Gaiman', 'Neil')
    # Terry = Author ('Pratchett', 'Terry')

    # if (Terry < Neil):
    #     print("less than")
    # else:
    #     print('greater than')

    data_source = BooksDataSource('tinybooks.csv')
    # data_source = BooksDataSource('specifictinybooks.csv')

    # authors = data_source.authors()
    # authors = data_source.authors("mELVILLE")
    # print(len(authors))
    # for i in authors:
    #     print(i.given_name, i.surname)

    books = data_source.books()
    print(len(books))
    for i in books:
        print(i.title)

