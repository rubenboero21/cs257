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
    
    # if we search for Terry Pratchett and the result is that 2 books are printed, 
    # then we know that search works with multiple authors
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
    
    def test_title_search_multiple_authors(self):
        datasource = BooksDataSource('books1.csv')
        books = datasource.books('omen')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0].authors[0].surname == 'Gaiman')
        self.assertTrue(books[0].authors[1].surname == 'Pratchett')

    # test that year search works with no search term and break a tie
    def test_all_books_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('', 'year') # equivalent to books = tiny_data_source.books(sort_by='year')
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Omoo')
        self.assertTrue(books[2].title == 'Never')
        self.assertTrue(books[3].title == 'Neverwhere')

    # test that default search works with a search term
    def test_search_keyword(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('Never', 'title')
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

    # test that author search works with no search term
    def test_all_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        self.assertTrue(len(authors) == 4)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(authors[2] == Author('Melville', 'Herman'))
        self.assertTrue(authors[3] == Author('Xiaoying', 'Ruben'))
    
    # test that author search works when 2 authors have the same last name
    def test_same_surname(self):
        gaiman_data_source = BooksDataSource('justgaiman.csv')
        authors = gaiman_data_source.authors('Gaiman')
        self.assertTrue(len(authors) == 2)
        self.assertTrue(authors[0] == Author('Gaiman', 'Anne'))
        self.assertTrue(authors[1] == Author('Gaiman', 'Neil'))

    # test that authors with more than two names can be searched for
    def test_multiple_surnames(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        authors = specific_data_source.authors('Márquez')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('García Márquez', 'Gabriel'))

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

    # test that year search works when only the start year is input
    def test_only_start_year(self):
        gaiman_data_source = BooksDataSource('justgaiman.csv')
        books = gaiman_data_source.books_between_years(start_year=1940)
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0].title == 'Neverwhere')

    # test that year search works when 0 years are input
    def test_no_year_input(self):
        gaiman_data_source = BooksDataSource('justgaiman.csv')
        books = gaiman_data_source.books_between_years()
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Fake Book')
        self.assertTrue(books[1].title == 'Neverwhere')
    
    # test tie breaking when searching by year
    def test_year_tie_break(self):
        specific_data_source = BooksDataSource('specifictinybooks.csv')
        books = specific_data_source.books_between_years(start_year=1990)
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Good Omens')
        self.assertTrue(books[1].title == 'Neverwhere')
        self.assertTrue(books[2].title == 'Thief of Time')

    # test that case doesn't matter when searching titles and sorting by title
    def test_title_search_case(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('EVER', 'title')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Never')
        self.assertTrue(books[1].title == 'Neverwhere')
    
    # test that case doesn't matter when searching for titles and sorting by year
    def test_year_search_case(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books('eVeR', 'year')
        self.assertTrue(len(books) == 2)
        self.assertTrue(books[0].title == 'Never')
        self.assertTrue(books[1].title == 'Neverwhere')
        
    # test that case doesn't matter when searching authors
    def test_author_case(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors('mELVILLE')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Melville', 'Herman'))

if __name__ == '__main__':
    unittest.main()

