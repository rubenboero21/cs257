# this program was written by Ruben Boero and Xiaoying Qu
# modeled from Jeff Ondich's sysargv-sample.py example

# REMEMBER TO TAG THIS FILE: git tag books-implementation

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

    # if there is a command entered and something else (everything possible entererd)
    if (len(sys.argv) > 2):
        if (sys.argv[1] == 'author'):

            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                arguments['help'] = sys.argv[2]

            else:
                arguments['search-term'] = sys.argv[2]
    return arguments

def main(arguments):
    if (len(sys.argv) > 2):
        if arguments['search-attribute'] == 'author':
            if sys.argv[2] == '-h' or sys.argv[2] == '--help':
                if arguments['help'] == '-h' or arguments['help'] == '--help':
                    help_statement = 'python3 books.py author [-h] string \n'
                    help_statement += "\nGiven a search string S, prints a list of authors whose names contain S (case-insensitive). For each such author, prints a list of the author's books. Authors are sorted alphabetically by surname. If there is a tie, it will be broken by first/given name. If no search string is provided, all authors will be printed."
                print(help_statement)

            elif 'search-term' in arguments:
                data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
                authors = data_source.authors(arguments['search-term'])
                
                for i in authors:
                    print(i. surname, i.given_name, ": ", i.books)

    # this case handles if the author command is used with no parameters
    elif (len(sys.argv) > 1 and arguments['search-attribute'] == 'author'):
            data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
            authors = data_source.authors()

            for i in authors:
                print(i. surname, i.given_name, ": ", i.books)

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
        
    # this case is reached if the command entered is invalid
    else:
        invalid_command = arguments['search-attribute']
        print(f"{invalid_command} is not a valid command. Type -h or --help for more information on valid commands.")

arguments = parse_command_line()
if 'search-attribute' not in arguments:
    print(usage_statement())
else:
    main(arguments)

