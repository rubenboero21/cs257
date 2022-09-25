#!/usr/bin/env python3
# Interface Implemented by Ruben and Xiaoying

# ******* git tag books-implementation ********
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv



def get_title(self, csv_line):
    title =""



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
    # sorting based on key: 
    # https://www.techiedelight.com/sort-list-of-objects-python/#:~:text=A%20simple%20solution%20is%20to,only%20arguments%3A%20key%20and%20reverse.

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



                #following is the code we wrote:
        for line in books_csv_file_name:
            
            # import csv

            # f = open('file.csv')

            # the_data = list(csv.reader(f, delimiter r'\t'))[1:]
            # https://stackoverflow.com/questions/45120726/how-to-read-csv-file-lines-and-split-elements-in-line-into-list-of-lists
            
            data = line.strip().split(",")
            title = get_title(data[0])
            pub_year = get_pub_year(data[1])
            author = get_author(data[2])
            birth_year = get_brith_year

        '''
        
        # how will we handle authors that have multiple books on the list? we dont want to create multiple author
        # objects for those cases. should we search through the whole list to look for other books that they have authored?
        # the look through the whole list thing seems unnecesarily inneficient 
        # also, we need to pass in a list of books for the author class, so basically, how will we create that list of books? 
        # 1. find an author 2. add the book to their list of books 3. look through the rest of the csv to see if the author appears again?

        # when parsing the author category, we could use a contains search to look for the 'and' in the author index
        # then would need to parse things on either side of the and (and is the delimiter)

        # for the multiple last names thing, does counting spaces work? ie 2 spaces is 1 last name, 3 spaces is 2 last names?
        # 2 spaces bc there is a space between the name and birth/death year
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
    f = open('books1.csv')

    reader = csv.reader(f,delimiter= ',')
    #the_data = list(csv.reader(f[1:])
    for row in reader:
        print(row)
   


    

