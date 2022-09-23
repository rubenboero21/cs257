# this test suite was modified by Ruben Boero and Xiaoying Qu

# REMEMBER TO TAG THIS FILE: git tag books-tests
'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    # test that default sort works with no search term
    def test_all_books(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Never')
        self.assertTrue(books[2].title == 'Neverwhere')
        self.assertTrue(books[3].title == 'Omoo')

    # test that year search works with no search term
    def test_all_books_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('', 'year') # equivalent to books = tiny_data_source.books(sort_by='year')
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Omoo')
        self.assertTrue(books[2].title == 'Never')
        self.assertTrue(books[3].title == 'Neverwhere')

    # test that default search works with a search term (case-insensitive)
    # if this fails and we cant figure out why, try it with the search term capitalized correctly
    def test_search_keyword(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('never')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Never')
        self.assertTrue(books[1].title == 'Neverwhere')

    # test that year search works with a search term
    def test_search_keyword_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('e', 'year')
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Never')
        self.assertTrue(books[2].title == 'Neverwhere')
    
    # come up with a standard for what to do with mulitple authors, write a test to check our standard works
    #   sort books with 2 authors by the author with the surname that comes first alphabetically
    # the good omens book, for example

    # come up with a standard to sort authors with multiple last names (like Márquez)
    #   i think we should take both last names and store it as 1 string

    # test that author search works with no search term
    def test_all_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.books()
        self.assertTrue(len(authors) == 4)
        self.assertTrue(authors[0] == Author('Jane', 'Austen'))
        self.assertTrue(authors[1] == Author('Neil', 'Gaiman'))
        self.assertTrue(authors[2] == Author('Herman', 'Melville'))
        self.assertTrue(authors[3] == Author('Ruben', 'Xiaoying'))
    
    # test that author search works when 2 authors have the same last name
    def test_same_surname(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        authors = specific_data_source.authors('Gaiman')
        self.assertTrue(len(authors) == 2)
        self.assertTrue(authors[0] == Author('Anne', 'Gaiman'))
        self.assertTrue(authors[1] == Author('Neil', 'Gaiman'))

    # test that author search works when a book has multiple authors (also case-insensitivity)
    # if this fails and we cant figure out why, try it with the search term capitalized correctly
    def test_two_authors(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        authors = specific_data_source.authors('gaiman')
        self.assertTrue(len(authors) == 2)
        self.assertTrue(authors[0] == Author('Anne', 'Gaiman'))
        self.assertTrue(authors[1] == Author('Neil', 'Gaiman'))

    #THIS TEST ASSUMES THAT WE ONLY TAKE IN BOTH OF Márquez' NAMES AS HIS LAST NAME
    # test that authors with more than two names can be searched for
    def test_special_character_name(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        authors = specific_data_source.authors('Márquez')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Gabriel', 'García Márquez'))

    # test that year search works when 2 years are input
    def test_two_years_input(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        books = specific_data_source.books_between_years(1939, 1967)
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Fake Book')
        self.assertTrue(books[1].title == 'One Hundred Years of Solitude')

    # test that year search works when only the end year is input
    def test_only_end_year(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        books = specific_data_source.books_between_years(end_year=1990)
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Fake Book')
        self.assertTrue(books[1].title == 'One Hundred Years of Solitude')
        self.assertTrue(books[2].title == 'Good Omens')

    # test that year search works when only the start year is input (also breaks a tie)
    def test_only_end_year(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        books = specific_data_source.books_between_years(start_year=1990)
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Good Omens')
        self.assertTrue(books[1].title == 'Neverwhere')
        self.assertTrue(books[2].title == 'Thief of Time')

    # test that year search works when 0 years are input
    def test_no_year_input(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        books = specific_data_source.books_between_years()
        self.assertTrue(len(books) == 5)
        self.assertTrue(books[0].title == 'Fake Book')
        self.assertTrue(books[1].title == 'One Hundred Years of Solitude')
        self.assertTrue(books[2].title == 'Good Omens')
        self.assertTrue(books[3].title == 'Neverwhere')
        self.assertTrue(books[4].title == 'Thief of Time')

    # check that case insensitivity works

if __name__ == '__main__':
    unittest.main()

