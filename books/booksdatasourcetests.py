# this test suite was modified by Ruben Boero and Xiaoying Qu
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

    def test_all_books(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Never')
        self.assertTrue(books[2].title == 'Neverwhere')
        self.assertTrue(books[3].title == 'Omoo')

    def test_all_books_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('', 'year') # equivalent to books = tiny_data_source.books(sort_by='year')
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Omoo')
        self.assertTrue(books[2].title == 'Never')
        self.assertTrue(books[3].title == 'Neverwhere')

    def test_search_keyword(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('Never')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Never')
        self.assertTrue(books[1].title == 'Neverwhere')

    def test_search_keyword_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('e', 'year')
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Never')
        self.assertTrue(books[2].title == 'Neverwhere')

    def test_all_authors(self):
        # come up with a standard for what to do with mulitple authors, write a test to check our standard works
        # sort books with 2 authors by the author with the surname that comes first alphabetically
        # the good omens book

if __name__ == '__main__':
    unittest.main()

