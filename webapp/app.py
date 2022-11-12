'''
    app.py
    Jeff Ondich, 25 April 2016
    Updated 8 November 2021

    A small Flask application that provides a barelywebsite with an accompanying
    API (which is also tiny) to support that website.

    Modified by Ruben Boero and Serafin Patino
'''
import flask
import argparse
import api
import sys
import config
import psycopg2
import json

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)

@app.route('/')
def home():
    return flask.render_template('index.html')
    
@app.route('/generations') 
def generations():
    return flask.render_template('generations.html')

@app.route('/legendaries') 
def legendaries():
    return flask.render_template('legendaries.html')

@app.route('/egg_groups') 
def egg_groups():
    return flask.render_template('egg_groups.html')

@app.route('/types') 
def types():
    return flask.render_template('types.html')

@app.route('/pokedex')
def pokedex():
    return flask.render_template('pokedex.html')

@app.route('/search_results/<category>/<search_text>')
# def display_search_results():
def display_search_results(category, search_text):

    if search_text == 'default':
        if category == 'pokemon':
            query = ''''''
        elif category == 'pokedex_number':
            query = ''''''
        elif category == 'ability':
            query = ''''''
        elif category == 'type':
            query = ''''''
    else: # if there is search text
        if category == 'pokemon':
            query = '''SELECT pokemon.dex_num, pokemon.name, ab1.name, ab2.name, ab3.name, typ1.name, typ2.name, generations.name
                    FROM pokemon, abilities ab1, abilities ab2, abilities ab3, types typ1, types typ2, generations, linking_table
                    WHERE 1 = 1
                    AND pokemon.id = linking_table.pokemon_id
                    AND ab1.id = linking_table.ability1_id
                    AND ab2.id = linking_table.ability2_id
                    AND ab3.id = linking_table.ability3_id
                    AND typ1.id = linking_table.type1_id
                    AND typ2.id = linking_table.type2_id
                    AND generations.id = linking_table.generation_id
                    AND pokemon.name ILIKE CONCAT ('%%',%s,'%%')
                    ORDER BY pokemon.dex_num ASC;'''
            pokemon_list = []
            try:
                connection = get_connection()
                cursor = connection.cursor()
                #what's the purpose of tuple in jeff's example
                cursor.execute(query, (search_text,))
                for row in cursor:
                    pokemon_list.append({'dex_num':row[0], 'name':row[1], 'ability1':row[2], 'ability2':row[3],\
                        'ability3':row[4], 'type1':row[5], 'type2':row[6], 'generation' : row[7]})
                cursor.close()
                connection.close()
            except Exception as e:
                print(e, file=sys.stderr)

            # return the list of dictionaries to the html, then parse it inside HTML
            return flask.render_template('search_results.html', search_results=pokemon_list)


        elif category == 'pokedex_number':
            query = ''''''
        elif category == 'ability':
            query = ''''''
        elif category == 'type':
            query = ''''''

# send in the info needed for the pokemon specific page in the url. construct the URL in the JS after
# the JSON dump. then this route can parse out each piece of information
# @app.route('/pokemon/<ID-dex_num-name-etc.>')
# def pokemon_detail(useful variables):
#     return flask.render_template(same useful variables)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A Pokémon search engine/database')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
