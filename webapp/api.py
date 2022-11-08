'''
    api.py
    Jeff Ondich, 25 April 2016
    Updated 8 November 2021

    Tiny Flask API to support the tiny books web application.

    Modified by Ruben Boero and Serafin Patino
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)

@api.route('/generations') 
def get_generations():
    ''' Returns a list of all the pokemon in a given generation. 
        By default the list is in ascending order by idx number.  
            http://.../generations
        Returns an empty list if there's any database failure.
    '''
    query = '''SELECT name FROM generations
               ORDER BY id ASC;'''
    generations_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        #what's the purpose of tuple in jeff's example
        cursor.execute(query, tuple())
        for row in cursor:
            generation = row[0]
            generations_list.append(generation)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(generations_list)

@api.route('/generation/<gen_name>')
def get_books_for_author(gen_name):
    # This query must be update to work with whatever our database is
    query = '''SELECT pokemon.name
               FROM pokemon, generations, linking_table
               WHERE pokemon.id = linking_table.pokemon_id
               AND generations.id = linking_table.generation_id
               AND generations.name = %s;
            '''
    pokemon_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (gen_name,))
        for row in cursor:
            pokemon = row[0]
            pokemon_list.append(pokemon)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(pokemon_list)

