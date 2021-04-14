"""."""

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from API.parser import Input_parser
from API.maps import map_request
from API.wiki import wiki_request


app = Flask(__name__)


@app.route('/process', methods=['get', 'post'])
@cross_origin(origin="*")
def index():
    if request.method == 'POST':
        input = request.form['input']
        if len(input) != 0:
            parser = Input_parser(input)
            # " parser.parsed_input " is the parsed input to use for map API
            map_coordinates = map_request(parser.parsed_input)
            # str(map_coordinates.latitude) | str(map_coordinates.longitude)
            # to display parsed input's coordinates send by google API
            # return "Latitude : " + str(map_coordinates.latitude) + "  Longitude: " +str(map_coordinates.longitude)
            latitude = str(map_coordinates.latitude)
            longitude = str(map_coordinates.longitude)

            instance_wiki = wiki_request(latitude, longitude)
            instance_wiki_description = instance_wiki.get_wiki_info(latitude, longitude)
            return instance_wiki_description
        else:
            return {
                "error": "Vous n'avez pas saisie de texte "
            }
    else:
        return render_template('index.html')

# def input():
#     if request.method == 'POST':
#         input = request.form['input']
#         return input


@app.route('/exemple', methods=['get', 'post'])
@cross_origin(origin="*")
def exemple():
    if request.method == 'POST':
        input = request.form['input']
        if len(input) != 0:
            parser = Input_parser(input)
            # " parser.parsed_input " is the parsed input to use for map API
            map_coordinates = map_request(parser.parsed_input)
            # str(map_coordinates.latitude) | str(map_coordinates.longitude)
            # to display parsed input's coordinates send by google API
            # return "Latitude : " + str(map_coordinates.latitude) + "  Longitude: " +str(map_coordinates.longitude)
            latitude = map_coordinates.latitude
            longitude = map_coordinates.longitude
            return latitude
        else:
            return {
                "error": "Vous n'avez pas saisie de texte "
            }
    else:
        return render_template('index.html')