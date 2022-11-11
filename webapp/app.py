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

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

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
