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

def get_query_results_and_url(query, num_of_inputs, search_text):
    pokemon_list = []
    url = []

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # the execute line is differente depending on which category is being searched
        if num_of_inputs == 0:
            cursor.execute(query,)
        elif num_of_inputs == 1:
            cursor.execute(query, (search_text,))
        elif num_of_inputs == 2:
            cursor.execute(query, (search_text, search_text,))
        elif num_of_inputs == 3:
            cursor.execute(query, (search_text, search_text, search_text,))

        for row in cursor:
            row = list(row)
            for i in range(len(row)):
                row[i] = str(row[i])
                # give a value of NA to any entry that has no value
                if row[i] == '':
                    row[i] = 'NA'
                # replace any spaces with an underscore (otherwise causes a problem with the url
                # in jinja -- stops after a space)
                if ' ' in row[i]:
                    split = row[i].split(' ')
                    new_row = ''
                    for j in range(len(split)):
                        new_row += split[j]
                        if (j + 1) < len(split):
                            new_row += '_'
                    row[i] = new_row

            pokemon_list.append({'dex_num':row[0], 'name':row[1], 'ability1':row[2], 'ability2':row[3],\
                'ability3':row[4], 'type1':row[5], 'type2':row[6], 'generation':row[7], 'height':row[8], \
                'weight':row[9], 'normal_resist':row[10], 'fire_resist':row[11], 'water_resist':row[12], \
                'electric_resist':row[13], 'grass_resist':row[14], 'ice_resist':row[15], 'fighting_resist':row[16], \
                'poison_resist':row[17], 'ground_resist':row[18], 'flying_resist':row[19], 'psychic_resist':row[20],\
                'bug_resist':row[21], 'rock_resist':row[22], 'ghost_resist':row[23], 'dragon_resist':row[24], \
                'dark_resist':row[25], 'steel_resist':row[26], 'fairy_resist':row[27], 'fairy_resist':row[27], \
                'hp':row[28], 'atk':row[29], 'def':row[30], 'spatk':row[31], 'spdef':row[31], 'spd':row[32]})

            url.append(
                row[0] + '/' + row[1] + '/' + row[2] + '/' + row[3] + '/' + row[4] + '/' + row[5] + '/' \
                + row[6] + '/' + row[7] + '/' + row[8] + '/' + row[9] + '/' + row[10] + '/' + row[11] + '/' \
                + row[12] + '/' + row[13] + '/' + row[14] + '/' + row[15] + '/' + row[16] + '/' + row[17] + '/' \
                + row[18] + '/' + row[19] + '/' + row[20] + '/' + row[21] + '/' + row[22] + '/' + row[23] + '/' \
                + row[24] + '/' + row[25] + '/' + row[26] + '/' + row[27] + '/' + row[28] + '/' + row[29] + '/' \
                + row[30] + '/' + row[31] + '/' + row[32] + '/' + row[33]
            )
                
        cursor.close()
        connection.close()

        return pokemon_list, url

    except Exception as e:
        print(e, file=sys.stderr)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/api/help')
def help():
    with open('help.txt', 'r') as file:
        content = file.read()
    
    return flask.Response(content, mimetype='text/plain')
    
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

# if we add the '\' character to break up the line, flask doesn't work
@app.route('/<id>/<name>/<ab1>/<ab2>/<ab3>/<type1>/<type2>/<generation>/<height>/<weight>/<normal_resist>/<fire_resist>/<water_resist>/<electric_resist>/<grass_resist>/<ice_resist>/<fighting_resist>/<poison_resist>/<ground_resist>/<flying_resist>/<psychic_resist>/<bug_resist>/<rock_resist>/<ghost_resist>/<dragon_resist>/<dark_resist>/<steel_resist>/<fairy_resist>/<hp>/<atk>/<defense>/<spatk>/<spdef>/<spd>')
def pokedex(id,name,ab1,ab2,ab3,type1,type2,generation,height,weight,normal_resist,fire_resist, \
water_resist,electric_resist,grass_resist,ice_resist,fighting_resist,poison_resist,ground_resist,flying_resist, \
psychic_resist,bug_resist,rock_resist,ghost_resist,dragon_resist,dark_resist,steel_resist,fairy_resist, hp, atk, \
defense, spatk, spdef, spd):

    # add the rest of the variables into the render template function
    return flask.render_template('pokedex.html', id=id,name=name,ability1=ab1,ability2=ab2,ability3=ab3,type1=type1,\
    type2=type2,generation=generation,height=height,weight=weight,normal_resist=normal_resist,fire_resist=fire_resist, \
    water_resist=water_resist,electric_resist=electric_resist,grass_resist=grass_resist,ice_resist=ice_resist,\
    fighting_resist=fighting_resist,poison_resist=poison_resist,ground_resist=ground_resist,flying_resist=flying_resist, \
    psychic_resist=psychic_resist,bug_resist=bug_resist,rock_resist=rock_resist,ghost_resist=ghost_resist,\
    dragon_resist=dragon_resist,dark_resist=dark_resist,steel_resist=steel_resist,fairy_resist=fairy_resist, \
    hp=hp, atk=atk, defense=defense, spatk=spatk, spdef=spdef, spd=spd)

@app.route('/search_results/<category>/<search_text>')
# def display_search_results():
def display_search_results(category, search_text):

    if search_text == 'default':
        query = '''SELECT  pokemon.dex_num, pokemon.name, ab1.name, ab2.name, ab3.name, typ1.name, typ2.name, generations.name, linking_table.height, linking_table.weight, linking_table.normal_resist, linking_table.fire_resist, linking_table.water_resist, linking_table.electric_resist, linking_table.grass_resist, linking_table.ice_resist, linking_table.fighting_resist, linking_table.poison_resist, linking_table.ground_resist, linking_table.flying_resist, linking_table.psychic_resist, linking_table.bug_resist, linking_table.rock_resist, linking_table.ghost_resist, linking_table.dragon_resist, linking_table.dark_resist, linking_table.steel_resist, linking_table.fairy_resist, pokemon.hp, pokemon.atk, pokemon.def, pokemon.spatk, pokemon.spdef, pokemon.spd
                FROM pokemon, abilities ab1, abilities ab2, abilities ab3, types typ1, types typ2, generations, linking_table
                WHERE 1 = 1
                AND pokemon.id = linking_table.pokemon_id
                AND ab1.id = linking_table.ability1_id
                AND ab2.id = linking_table.ability2_id
                AND ab3.id = linking_table.ability3_id
                AND typ1.id = linking_table.type1_id
                AND typ2.id = linking_table.type2_id
                AND generations.id = linking_table.generation_id
                ORDER BY pokemon.dex_num ASC;'''

    elif category == 'pokemon':
        query = '''SELECT  pokemon.dex_num, pokemon.name, ab1.name, ab2.name, ab3.name, typ1.name, typ2.name, generations.name, linking_table.height, linking_table.weight, linking_table.normal_resist, linking_table.fire_resist, linking_table.water_resist, linking_table.electric_resist, linking_table.grass_resist, linking_table.ice_resist, linking_table.fighting_resist, linking_table.poison_resist, linking_table.ground_resist, linking_table.flying_resist, linking_table.psychic_resist, linking_table.bug_resist, linking_table.rock_resist, linking_table.ghost_resist, linking_table.dragon_resist, linking_table.dark_resist, linking_table.steel_resist, linking_table.fairy_resist, pokemon.hp, pokemon.atk, pokemon.def, pokemon.spatk, pokemon.spdef, pokemon.spd
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

    elif category == 'pokedex_number':
        query = '''SELECT  pokemon.dex_num, pokemon.name, ab1.name, ab2.name, ab3.name, typ1.name, typ2.name, generations.name, linking_table.height, linking_table.weight, linking_table.normal_resist, linking_table.fire_resist, linking_table.water_resist, linking_table.electric_resist, linking_table.grass_resist, linking_table.ice_resist, linking_table.fighting_resist, linking_table.poison_resist, linking_table.ground_resist, linking_table.flying_resist, linking_table.psychic_resist, linking_table.bug_resist, linking_table.rock_resist, linking_table.ghost_resist, linking_table.dragon_resist, linking_table.dark_resist, linking_table.steel_resist, linking_table.fairy_resist, pokemon.hp, pokemon.atk, pokemon.def, pokemon.spatk, pokemon.spdef, pokemon.spd
                FROM pokemon, abilities ab1, abilities ab2, abilities ab3, types typ1, types typ2, generations, linking_table
                WHERE 1 = 1
                AND pokemon.id = linking_table.pokemon_id
                AND ab1.id = linking_table.ability1_id
                AND ab2.id = linking_table.ability2_id
                AND ab3.id = linking_table.ability3_id
                AND typ1.id = linking_table.type1_id
                AND typ2.id = linking_table.type2_id
                AND generations.id = linking_table.generation_id
                AND pokemon.dex_num = %s
                ORDER BY pokemon.dex_num ASC;'''

    elif category == 'ability':
        query = '''SELECT  pokemon.dex_num, pokemon.name, ab1.name, ab2.name, ab3.name, typ1.name, typ2.name, generations.name, linking_table.height, linking_table.weight, linking_table.normal_resist, linking_table.fire_resist, linking_table.water_resist, linking_table.electric_resist, linking_table.grass_resist, linking_table.ice_resist, linking_table.fighting_resist, linking_table.poison_resist, linking_table.ground_resist, linking_table.flying_resist, linking_table.psychic_resist, linking_table.bug_resist, linking_table.rock_resist, linking_table.ghost_resist, linking_table.dragon_resist, linking_table.dark_resist, linking_table.steel_resist, linking_table.fairy_resist, pokemon.hp, pokemon.atk, pokemon.def, pokemon.spatk, pokemon.spdef, pokemon.spd
                FROM pokemon, abilities ab1, abilities ab2, abilities ab3, types typ1, types typ2, generations, linking_table
                WHERE 1 = 1
                AND pokemon.id = linking_table.pokemon_id
                AND ab1.id = linking_table.ability1_id
                AND ab2.id = linking_table.ability2_id
                AND ab3.id = linking_table.ability3_id
                AND typ1.id = linking_table.type1_id
                AND typ2.id = linking_table.type2_id
                AND generations.id = linking_table.generation_id
                AND (ab1.name ILIKE CONCAT ('%%',%s,'%%')
                OR ab2.name ILIKE CONCAT ('%%',%s,'%%') 
                OR ab3.name ILIKE CONCAT ('%%',%s,'%%'))
                ORDER BY pokemon.dex_num ASC;'''

    elif category == 'type':
        query = '''SELECT  pokemon.dex_num, pokemon.name, ab1.name, ab2.name, ab3.name, typ1.name, typ2.name, generations.name, linking_table.height, linking_table.weight, linking_table.normal_resist, linking_table.fire_resist, linking_table.water_resist, linking_table.electric_resist, linking_table.grass_resist, linking_table.ice_resist, linking_table.fighting_resist, linking_table.poison_resist, linking_table.ground_resist, linking_table.flying_resist, linking_table.psychic_resist, linking_table.bug_resist, linking_table.rock_resist, linking_table.ghost_resist, linking_table.dragon_resist, linking_table.dark_resist, linking_table.steel_resist, linking_table.fairy_resist, pokemon.hp, pokemon.atk, pokemon.def, pokemon.spatk, pokemon.spdef, pokemon.spd
                FROM pokemon, abilities ab1, abilities ab2, abilities ab3, types typ1, types typ2, generations, linking_table
                WHERE 1 = 1
                AND pokemon.id = linking_table.pokemon_id
                AND ab1.id = linking_table.ability1_id
                AND ab2.id = linking_table.ability2_id
                AND ab3.id = linking_table.ability3_id
                AND typ1.id = linking_table.type1_id
                AND typ2.id = linking_table.type2_id
                AND generations.id = linking_table.generation_id
                AND (typ1.name ILIKE CONCAT ('%%',%s,'%%') OR typ2.name ILIKE CONCAT ('%%',%s,'%%'))
                ORDER BY pokemon.dex_num ASC;'''

    pokemon_list = []
    url = []

    # if there is no search text, return all pokemon
    if search_text == 'default':
        result = get_query_results_and_url(query, 0, '')
        pokemon_list = result[0]
        url = result[1]

        return flask.render_template('search_results.html', search_results=pokemon_list, url=url)

    elif category == 'pokemon' or category == 'pokedex_number':
        result = get_query_results_and_url(query, 1, search_text)
        pokemon_list = result[0]
        url = result[1]

        # return the list of dictionaries to the html, then parse it inside HTML
        return flask.render_template('search_results.html', search_results=pokemon_list, url=url)
    
    elif category == 'ability':
        result = get_query_results_and_url(query, 3, search_text)
        pokemon_list = result[0]
        url = result[1]

        # return the list of dictionaries to the html, then parse it inside HTML
        return flask.render_template('search_results.html', search_results=pokemon_list, url=url)
    
    elif category == 'type':
        result = get_query_results_and_url(query, 2, search_text)
        pokemon_list = result[0]
        url = result[1]

        # return the list of dictionaries to the html, then parse it inside HTML
        return flask.render_template('search_results.html', search_results=pokemon_list, url=url)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A Pokémon search engine/database')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
