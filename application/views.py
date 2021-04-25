"""This file manages routes and views."""

from application import app
from flask import request
from flask import render_template
from flask_cors import cross_origin
from application.parser import Input_parser
from application.maps import map_request
from application.wiki import wiki_request


@app.route("/")  # view function with route URL
@cross_origin(origin="*")
def hello_world():
    return render_template("index.html")


@app.route('/process', methods=['get', 'post'])
@cross_origin(origin="*")
def index():
    if request.method == 'POST':
        input = request.form['input']
        if len(input) != 0:
            parser = Input_parser(input)
            # " parser.parsed_input " is the parsed input to use for map
            map_coordinates = map_request(parser.parsed_input)
            latitude = str(map_coordinates.latitude)
            longitude = str(map_coordinates.longitude)
            map_coords = {
                "latitude": latitude,
                "longitude": longitude
            }
            instance_wiki = wiki_request(latitude, longitude)
            instance_wiki_description = \
                instance_wiki.get_wiki_info(latitude, longitude)
            response = {
                "wiki_info": instance_wiki_description,
                "map": map_coords
            }
            return response
        else:
            return {
                "error": "Vous n'avez pas saisie de texte "
            }
    else:
        return {"error": "request method is not 'POST' "}


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
