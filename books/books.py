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
            else:
                data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
                authors = data_source.authors(arguments['search-term'])
                
                for i in authors:
                    print(i.books)
    else:
        data_source = booksdatasource.BooksDataSource('specifictinybooks.csv')
        authors = data_source.authors()
        for i in authors:
            print(i.books)

arguments = parse_command_line()
if 'search-attribute' not in arguments:
    print(usage_statement())
else:
    main(arguments)

