# This program was written by Ruben Boero
# Code was adapted from Jeff's example in psycopg2-sample.py file

from itertools import count
import config
import sys
import psycopg2

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

def get_count_of_sports():
    sport_count = []
    try:
        query = '''SELECT sport, Count(sports.sport)
                FROM sports, athletes_nocs_olympic_games_events_sports_medals
                WHERE sports.id = athletes_nocs_olympic_games_events_sports_medals.sport_id
                GROUP BY sports.sport
                ORDER BY COUNT(sports.sport) DESC;'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            sport= row[0]
            count = row[1]
            sport_count.append(f"{sport}: {count}")

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return sport_count

def main():
    # athletes = get_athletes_from_noc('SGP')
    # for athlete in athletes:
    #     print(athlete)

    # medals_count = get_noc_medal_count()
    # for i in medals_count:
    #     print(i)

    sport_count = get_count_of_sports()
    for i in sport_count:
        print(i)

if __name__ == '__main__':
    main()
