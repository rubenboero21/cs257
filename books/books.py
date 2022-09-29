# this program was written by Ruben Boero and Xiaoying Qu
# modelled from Jeff Ondich's sysargv-sample.py example

# REMEMBER TO TAG THIS FILE: git tag books-implementation

from ast import arg
import booksdatasource
import sys

def usage_statement():
    statement = f'Usage: {sys.argv[0]} . This is a program that will search through a CSV file to find and sort information. It can search for titles, authors, and dates of publication. \n'
    statement += '\n    Use the -h or --help command to see more details.'
    return statement

def parse_command_line():
    arguments = {}
    # if there is more than just books.py entered
    if len(sys.argv) > 1:
        # should we rename 'search-attribute' to be 'command'?
        arguments['search-attribute'] = sys.argv[1]

    # if there is a command entered and something else 
    if (len(sys.argv) > 2):
        # author search
        if (sys.argv[1] == 'author'):
            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                arguments['help'] = sys.argv[2]
            # could use a case that catches if the user inputs an invalid flag
            else:
                arguments['search-term'] = sys.argv[2]
    
        # title search
        elif (sys.argv[1] == 'title'):
            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                arguments['help'] = sys.argv[2]
            
            elif sys.argv[2] == '-t' or sys.argv[2] == '--title':
                arguments['sort'] = sys.argv[2]

                # if a search term is entered
                if (len(sys.argv) > 3):
                    arguments['search-term'] = sys.argv[3]

            elif sys.argv[2] == '-y' or sys.argv[2] == '--year':
                arguments['sort'] = sys.argv[2]

                # if a search term is entered
                if (len(sys.argv) > 3):
                    arguments['search-term'] = sys.argv[3]

            # if the user inputs a flag that is invalid, stop running the code
            else:  
                print(f"Flag {sys.argv[2]} is not a valid flag for the title search. Type 'title -h' or 'title --help' for more information.")
                # this might be a bad way to do things
                quit()
        
        # year search
        elif (sys.argv[1] == 'year'):
            # need to be able to stop bad inpts from coming in

            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                arguments['help'] = sys.argv[2]
            
            elif len(sys.argv) == 4:
                # there is no start year
                if sys.argv[2] == '_':
                    arguments['end-year'] = sys.argv[3]
                # if there is no end year
                elif sys.argv[3] == '_':
                    arguments['start-year'] = sys.argv[2]
                # if both years are input
                elif sys.argv[2] != '_' and sys.argv[3] != '_':
                    arguments['start-year'] = sys.argv[2]
                    arguments['end-year'] = sys.argv[3]

    print (len(sys.argv))
    return arguments

def main(arguments):
    print(arguments)

    # the and is needed bc if an author command has 3 args then it must have a search, not the case for 
    # title and year search. Handles cases when search term is provided
    # if (len(sys.argv) > 2) and 'search-term' in arguments:
    if (len(sys.argv) > 2) and 'search-term' in arguments:
        if arguments['search-attribute'] == 'author':
            # handles the case when a search term is passed into the author command
            # if 'search-term' in arguments:
            search_term = arguments['search-term']
            data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
            authors = data_source.authors(search_term)
            
            if len(authors) > 0:
                for i in authors:
                    print(i. surname, i.given_name, ": ", i.books)
            else:
                print(f"No authors were found containing {search_term}. If you meant to input a flag, type 'author -h' or 'author --help' to valid flags")

        elif arguments['search-attribute'] == 'title':
            # handles the case when sorting by title and a search term is provided
            if sys.argv[2] == '-t' or sys.argv[2] == '--title':
                # CHECK THAT THIS WORKS ONCE THE TITLE SORT IS WORKING, IT DOES WEIRD THINGS RN
                print('There is currently not functionality for this sort method')
                # if 'search-term' in arguments:
                search_term = arguments['search-term']
                data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
                books = data_source.books(search_term, 'title')

                if (len(books) > 0):
                    for i in books:
                        authors = []

                        for j in i.authors:
                            authors.append(j.given_name + " " + j.surname)

                        print(i.title, "by", authors)
                else:
                    print(f"No books were found containing {search_term}")  

            # handles the case when the sorting by year and a search term is provided
            elif sys.argv[2] == '-y' or sys.argv[2] == '--year':
                #print('2')
                # if 'search-term' in arguments:
                search_term = arguments['search-term']
                data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
                books = data_source.books(search_term, 'year')

                if (len(books) > 0):
                    for i in books:
                        authors = []

                        for j in i.authors:
                            authors.append(j.given_name + " " + j.surname)

                        print(i.title, "by", authors)
                else:
                    print(f"No books were found containing {search_term}")

        # elif arguments['search-attribute'] == 'year':
        #     print("year")

    # search by year
    # if there is only a start year
    elif (len(sys.argv) > 2) and 'start-year' in arguments and 'end-year' not in arguments:
        print('just start year')

        start_year= int(arguments['start-year'])
        data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
        books = data_source.books_between_years(start_year=start_year)

        if (len(books) > 0):
            for i in books:
                authors = []

                for j in i.authors:
                    authors.append(j.given_name + " " + j.surname)

                print(i.title, "by", authors)
        else:
            print(f"No books were found after or during the year {start_year}")

    # if there is only an end year
    elif (len(sys.argv) > 2) and 'start-year' not in arguments and 'end-year'  in arguments:
        print('just end year')

        end_year= int(arguments['end-year'])
        data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
        books = data_source.books_between_years(end_year=end_year)

        if (len(books) > 0):
            for i in books:
                authors = []

                for j in i.authors:
                    authors.append(j.given_name + " " + j.surname)

                print(i.title, "by", authors)
        else:
            print(f"No books were found before or during the year {end_year}")

    # if both years are inlcluded
    elif (len(sys.argv) > 2) and 'start-year'  in arguments and 'end-year'  in arguments:
        print("both years")

        start_year= int(arguments['start-year'])
        end_year= int(arguments['end-year'])
        data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
        books = data_source.books_between_years(start_year, end_year)

        if (len(books) > 0):
            for i in books:
                authors = []

                for j in i.authors:
                    authors.append(j.given_name + " " + j.surname)

                print(i.title, "by", authors)
        else:
            print(f"No books were found between or during the years {start_year} and {end_year}")
    
    # case to print books when no years are input
    elif (len(sys.argv) == 2 and arguments['search-attribute'] == 'year'):
        print('no years')
        data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
        books = data_source.books_between_years()

        if (len(books) > 0):
            for i in books:
                authors = []

                for j in i.authors:
                    authors.append(j.given_name + " " + j.surname)

                print(i.title, "by", authors)
        else:
            print("No books were found in the CSV file")
    # end year stuff

    # case to print help statements 
    elif (len(sys.argv) > 2):
        if arguments['search-attribute'] == 'author':        
            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                help_statement = 'python3 books.py author [-h] string \n'
                help_statement += "\nGiven a search string S, prints a list of authors whose names contain S (case-insensitive). For each such author, prints a list of the author's books. Authors are sorted alphabetically by surname. If there is a tie, it will be broken by first/given name. If no search string is provided, all authors will be printed."
                print(help_statement)     

        elif arguments['search-attribute'] == 'title':
            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                help_statement = 'python3 books.py title [-h|-t|-y] string \n'
                help_statement += "\nGiven a search string S, prints a list of books whose titles contain S (case-insensitive). Books are sorted by title or publication year as specified. If no sort method is specified, books will default to be sorted by title. If no search string is provided, all books will be printed."
                print(help_statement)

        elif arguments['search-attribute'] == 'year':
            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                help_statement = 'python3 books.py year [-h|_ yearB|yearA _|yearA yearB] \n'
                help_statement += "\nGiven a range of years A to B, prints a list of books published between years A and B, inclusive. Books are printed in order of publication year. Ties are broken by which title comes first alphabetically. If year A is not provided, then any book published before or during year B is printed. If year B is not provided, then any book published after or during year A are printed. If neither year A or B are provided, all books are printed.Note that to specify that no year is input, use the '_' character."
                print(help_statement)

    # this case handles if the author command is used with no parameters
    elif (len(sys.argv) > 1 and arguments['search-attribute'] == 'author'):
            data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
            authors = data_source.authors()

            for i in authors:
                print(i. surname, i.given_name, ": ", i.books)

    # case for when title search a sort method is specified but has no search term
    elif (len(sys.argv) > 2 and arguments['search-attribute'] == 'title'):
        if arguments['sort'] == '-y' or arguments['sort'] == '--year':
            data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
            books = data_source.books(sort_by= 'year')

            if len(books) > 0:
                for i in books:
                    authors = []

                    for j in i.authors:
                        authors.append(j.given_name + " " + j.surname)

                    print(i.title, "by", authors)
            else:
                print("No books were found in the CSV file")
        
        elif arguments['sort'] == '-t' or arguments['sort'] == '--title':
            data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
            books = data_source.books(sort_by= 'title')

            if len(books) > 0:
                for i in books:
                    authors = []

                    for j in i.authors:
                        authors.append(j.given_name + " " + j.surname)

                    print(i.title, "by", authors)
            else:
                print("No books were found in the CSV file")

    # print the default help statement - there has to be a better way to do this
    elif (len(sys.argv) > 1 and (arguments['search-attribute'] == '-h' or arguments['search-attribute'] == '--help')):
        '''   this gives weird spacing
        f = open('usage.txt')
        for line in f:
            print(line)
        f.close()'''
        
        print('''
Synopsis
	python3 books.py title [-h|-t|-y] string
	python3 books.py author [-h] string
	python3 books.py year [-h|yearA and yearB|yearA|yearB]

Description

	This is a program that will search through a CSV file to find and sort 
	information. It can search for titles, authors, and dates of publication.

	title
		Given a search string S, prints a list of books whose titles contain S 
		(case-insensitive). Books are sorted by title or publication year as 
		specified. If no sort method is specified, books will default to be sorted 
		by title. If no search string is provided, all books will be printed.
	
	author
		Given a search string S, prints a list of authors whose names contain S 
		(case-insensitive). For each such author, prints a list of the author's 
		books. Authors are sorted alphabetically by surname. If there is a tie, 
		it will be broken by first/given name. If no search string is provided, 
		all authors will be printed.

	year
		Given a range of years A to B, prints a list of books published between 
		years A and B, inclusive. Books are printed in order of publication year. 
		Ties are broken by which title comes first alphabetically. If year A is 
		not provided, then any book published before or during year B is printed. 
		If year B is not provided, then any book published after or during year A 
		are printed. If neither year A or B are provided, all books are printed.

General Flags

	-h, --help
		Prints the information about the specified command.
	
Title search specific flags

	-t, --title
		The list of books matching search string will be printed in order of book 
		title.
	
	-y, --year
		The list of books matching search string will be printed in order of 
		publication year.	
	''')
    elif ('sort' in arguments and (arguments['sort'] != '-t' or '-h' or '-y' )):
        print('invalid')
        
    # this case is reached if the search command entered is invalid
    else:
        invalid_command = arguments['search-attribute']
        print(f"{invalid_command} is not a valid command. Type -h or --help for more information on valid commands.")

arguments = parse_command_line()
if 'search-attribute' not in arguments:
    print(usage_statement())
else:
    main(arguments)

