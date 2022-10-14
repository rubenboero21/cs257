# This program was written by Ruben Boero
# Code was adapted from Jeff's example in psycopg2-sample.py file

import config
import sys
import psycopg2

# check that there is a subcommand, if not quit and print error message
if len(sys.argv) < 2:
    sys.exit("Not enough arguments were input. Please type 'python3 olympics.py --help' for more information.")
else:
    subcommand = sys.argv[1]

# this function was taken directly from Jeff's code
def get_connection():
    ''' Returns a database connection object with which you can create cursors,
        issue SQL queries, etc. This function is extremely aggressive about
        failed connections--it just prints an error message and kills the whole
        program. Sometimes that's the right choice, but it depends on your
        error-handling needs. '''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def get_athletes_from_noc(search_noc):
    ''' Returns a list of all athletes sorted by a given NOC abbreviation.'''
    athletes = []
    try:
        query = '''SELECT DISTINCT athletes.name
                FROM athletes, nocs, athletes_nocs_olympic_games_events_sports_medals
                WHERE athletes.id = athletes_nocs_olympic_games_events_sports_medals.athlete_id
                AND nocs.id = athletes_nocs_olympic_games_events_sports_medals.noc_id
                AND nocs.abbreviation = %s
                ORDER BY name ASC;'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_noc,))
        for row in cursor:
            name = row[0]
            athletes.append(name)

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_noc_medal_count():
    '''Returns a list of the medal count of each NOC sorted by descending medal count'''
    noc_medal_count = []
    try:
        query = '''SELECT nocs.abbreviation, COUNT(medals.class)
                FROM nocs, medals, athletes_nocs_olympic_games_events_sports_medals
                WHERE medals.id = athletes_nocs_olympic_games_events_sports_medals.medal_id
                AND nocs.id = athletes_nocs_olympic_games_events_sports_medals.noc_id
                AND medals.class = 'Gold'
                GROUP BY nocs.abbreviation
                ORDER BY COUNT(medals.class) DESC, nocs.abbreviation;'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            abbreviation = row[0]
            count = row[1]
            noc_medal_count.append(f"{abbreviation}: {count}")

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return noc_medal_count

def get_most_gold_medal_athletes():
    '''Returns a list of the top 81 athletes with the most gold medals ordered by descending medal count, 
       then name alphabetically'''
    athletes = []
    try:
        query = '''SELECT athletes.name, nocs.abbreviation, COUNT(medals.class)
                FROM athletes, nocs, medals, athletes_nocs_olympic_games_events_sports_medals
                WHERE athletes.id = athletes_nocs_olympic_games_events_sports_medals.athlete_id
                AND medals.id = athletes_nocs_olympic_games_events_sports_medals.medal_id
                AND nocs.id = athletes_nocs_olympic_games_events_sports_medals.noc_id
                AND medals.class = 'Gold'
                GROUP BY athletes.name, nocs.abbreviation
                ORDER BY COUNT(medals.class) DESC, athletes.name
                LIMIT 81;''' # top 81 bc that's the cut off for ties for 4 gold medals
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            name = row[0]
            noc = row[1]
            medal_count = row[2]
            athletes.append(f"{name} ({noc}): {medal_count}")

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

# handle the athlete by noc query
if subcommand == 'athletes':
    if len(sys.argv) > 2:
        noc_abbreviation = sys.argv[2]
        # handle case insensitivity
        noc_abbreviation = noc_abbreviation.upper()

        # handle the case where an invalid NOC abbreviation is input
        if len(noc_abbreviation) != 3 or noc_abbreviation.isdigit():
            sys.exit("Please provide a valid NOC 3 digit abbreviation.\nType 'python3 olympics.py --help' for more information.")
        
        athletes = get_athletes_from_noc(noc_abbreviation)

        for athlete in athletes:
            print(athlete)
    else:
        print("Please provide a valid NOC 3 digit abbreviation.\nType 'python3 olympics.py --help' for more information.")

# handles the query that lists how many gold medals each NOC has won
elif subcommand == 'noc_medals':
    # handle the case where more arguments are input than necessary
    if len(sys.argv) > 2:
        sys.exit("No arguments are required for this subcommand.\nType 'python3 olympics.py --help' for more information.")

    noc_medals_count = get_noc_medal_count()
    
    for noc_count in noc_medals_count:
        print(noc_count)

# handle the athletes with the most gold medals query
elif subcommand == 'top_athletes':

    # handle the case where more arguments are input than necessary
    if len(sys.argv) > 2:
        sys.exit("No arguments are required for this subcommand.\nType 'python3 olympics.py --help' for more information.")

    athletes = get_most_gold_medal_athletes()

    for athlete in athletes:
        print(athlete)

# handle the usage statement printing
elif subcommand == '-h' or subcommand == '--help':
    # the follwing 2 lines were taken directly from Alex Falk and Carl Zhang's books.py file
    # https://github.com/aafalk/cs257/blob/main/books/books.py
    with open('usage.txt', 'r') as file:
        print(file.read())

# handle if an invalid subcommand is entered
else:
    print(f"'{subcommand}' is not a recognized subcommand. Please type 'python3 olympics.py --help' for a list of valid subcommands.")
