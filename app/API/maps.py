"""
Interact with Google Places API, to get coordinates.
"""

import os
import requests
import json


class map_request:
    """
    Comment.
    """

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.get_coordinates()

    def get_coordinates(self):
        search = "Lyon"
        API = os.environ['API_KEY']
        url = str("https://maps.googleapis.com/maps/api/place/textsearch"
                  "/json?query={}&key={}").format(search, API)

        response = requests.get(url)

        if response.status_code == 200:
            response_data = response.json()
            if len(response_data["results"]) > 0:
                self.latitude = response_data['results'][0]['geometry']['location']['lat']
                self.longitude = response_data['results'][0]['geometry']['location']['lng']
            else:
                return "Lenght response data = 0"
        else:
            return response.status_code, ''


# """ test """
#
# json_result = map_request()
#
# print("Latitude : ", json_result.latitude)
# print("Longitude : ", json_result.longitude)
#
#
# """ test """
