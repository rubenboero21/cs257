#!/usr/bin/env python3
# Interface Implemented by Ruben and Xiaoying

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

# this function could be useless
def make_lowercase(csv_line):
    '''Takes in a line from a csv file and makes all of its substrings lower case to adhere
       to case-insensitivity'''
    i = 0
    while i < len(csv_line):
        csv_line[i] = csv_line[i].lower()
        i += 2 # jump the middle substring bc its a date, so cant be lowercase

def get_title(csv_substring):
    '''Returns the title of a book given the subtring of a csv file in which it appears.'''
    title = csv_substring
    return title

def get_pub_year(csv_substring):
    '''Returns the publication year of a book given the subtring of a csv file in which it appears.'''
    pub_year = csv_substring
    return pub_year

# this function could be useless
def get_authors(csv_substring):
    '''Returns the list of author(s) for a book given the subtring of a csv file in which it appears.'''
    authors = []
    return authors

def get_birth_year(csv_substring):
    '''Returns the birth year of an author given the subtring of a csv file in which it appears.'''
    # will need to work with books with more than 1 author
    birth_year = None
    return birth_year

def get_death_year(csv_substring):
    '''Returns the death year of an author given the subtring of a csv file in which it appears.
       Returns None if there is no death year.'''
    # will need to work with books with more than 1 author
    death_year = None
    return death_year

def get_surname(csv_substring):
    '''Returns the surname of an author given the subtring of a csv file in which it appears.'''
    # books with mulitple authors are already checked for before this function is called
    s = csv_substring.split(' ') 
    if len(s) > 3:
        #return str(s[1]) + str(s[2])
        return s[1] + ' ' +s[2]
    else:
        return  s[1]

def get_given_name(csv_substring):
    '''Returns the given name of an author given the subtring of a csv file in which it appears.'''
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
            # CANNOT make the input to the objects lowercase, it will make all of the outputs
            # later on incorrect. will need to figure out case-insensitivity later
            # make_lowercase(line) # is it bad to have a function that transforms the csv line?

            # the get title and pub_year functions do basically nothing, does it make sense to 
            # leave them as functions to make it easier to read + be consistent, or should we
            # not have them as functions? Also, does it make sense to need to pass in the
            # substring in which they appear?
            title = get_title(line[0])
            pub_year = get_pub_year(line[1])
            #authors = get_authors(line[2])

            # we dont want to create a new author object every time that there is a new line bc
            # some authors are in the csv in multiple places
            
            # if there are 2 authors
            if 'and' in line[2]:
                author_str = line[2].split(' and ')
                author1 = author_str[0]
                author2 = author_str[1]

                surname1 = get_surname(author1)
                given_name1 = get_given_name(author1)
                # birth_yea1r = get_birth_year(author1)

                surname2 = get_surname(author2)
                given_name2 = get_given_name(author2)
                # birth_year2 = get_birth_year(author2)


                # create objects
                temp_author1 = Author(surname1, given_name1)
                temp_author2 = Author(surname2, given_name2)
                
                # if the list of authors is empty, then add the first 2 Author objects
                if len(self.authors_list) == 0:
                    self.authors_list.append(temp_author1)
                    self.authors_list.append(temp_author2)
                # if the list of authors is not empty
                else:
                    # create 2 booleans to store if an author obj is already stored in the list
                    temp_author1_seen = False
                    temp_author2_seen = False

                    # check if the author is stored in the list
                    for author in self.authors_list:
                        if author == temp_author1:
                            temp_author1_seen = True
                        if author == temp_author2:
                            temp_author2_seen = True

                    # add an author to the list if they are not already in the list
                    if not (temp_author1_seen):
                        self.authors_list.append(temp_author1)
                    if not (temp_author2_seen):
                        self.authors_list.append(temp_author2)

            # if there is just 1 author
            else:
                surname = get_surname(line[2])
                given_name = get_given_name(line[2])
                # birth_year = get_birth_year(line[2])
                # death_year = get_death_year(line[2])

                # this will need to be updated when the rest of the helper functions work
                temp_author = Author(surname, given_name)
                
                # if the list of authors is empty, then add the first Author object
                if len(self.authors_list) == 0:
                    self.authors_list.append(temp_author)
                else:
                    temp_author_seen = False

                    for author in self.authors_list:
                        # if author does not already exist, add it to the list
                        if author == temp_author:
                            temp_author_seen = True
                            break # break out of the for loop bc the author has been found
                   
                    if not (temp_author_seen):
                        self.authors_list.append(temp_author)

            books_written = [] # if the author has not been encountered before, create a list of their 1 book so far (inside for loop so it resets for all new authors)
            books_written.append(title)            

            # ****this is INCORRECT, the last instance variable is a list containing all Author
            # objects. this means a book object contains a list of all author objects who wrote them,
            # so book objects need to be created after author objects - see notes for ideas on how to do this efficiently
            #self.books_list.append(Book(title, pub_year, authors))
            
        file.close() # couldnt figure out how to open the file using 'with' so just close the file here

        # this for loop is to test that the authors_list is being created correctly
        print("list of Author objects:")
        for authors in self.authors_list:
            print(authors.surname + ", " + authors.given_name)

        # how will we handle authors that have multiple books on the list? we dont want to create multiple author
        # objects for those cases. should we search through the whole list to look for other books that they have authored?
        # the look through the whole list thing seems unnecesarily inneficient 
        # also, we need to pass in a list of books for the author class, so basically, how will we create that list of books? 
        # 1. find an author 2. add the book to their list of books 3. look through the rest of the csv to see if the author appears again?

        # when parsing the author category, we could use a contains search to look for the 'and' in the author index
        # then would need to parse things on either side of the and (and is the delimiter)

        # for the multiple last names thing, get a parser, delemit at each space, and stop parsing when 
        # you hit the '('. then entry 1 is first name, and everything else is last  name
        pass

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        return []

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
        return []

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

    test = BooksDataSource('specifictinybooks.csv')
    
    
