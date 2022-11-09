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
def get_pokemon_for_generation(gen_name):
# def get_books_for_author(gen_name):
    # This query must be update to work with whatever our database is
    query = '''SELECT  pokemon.dex_num, pokemon.name, ab1.name, ab2.name, ab3.name, typ1.name, typ2.name
            FROM pokemon, abilities ab1, abilities ab2, abilities ab3, types typ1, types typ2, generations, linking_table
            WHERE 1 = 1
            AND pokemon.id = linking_table.pokemon_id
            AND ab1.id = linking_table.ability1_id
            AND ab2.id = linking_table.ability2_id
            AND ab3.id = linking_table.ability3_id
            AND typ1.id = linking_table.type1_id
            AND typ2.id = linking_table.type2_id
            AND generations.id = linking_table.generation_id
            AND generations.name = %s
            ORDER BY pokemon.dex_num ASC;
            '''
    pokemon_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (gen_name,))
        for row in cursor:
            # pokemon = row[0]

            # pokemon_list.append(pokemon)
            pokemon_list.append({'dex_num':row[0], 'name':row[1], 'ability1':row[2], 'ability2':row[3],\
                'ability3':row[4], 'type1':row[5], 'type2':row[6]})
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(pokemon_list)

