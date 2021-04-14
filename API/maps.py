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
    def __init__(self, input):
        self.latitude = None
        self.longitude = None
        self.get_coordinates(input)

    def get_coordinates(self, input):
        search = "Lyon"
        # API = os.environ['API_KEY']
        API_KEY = "AIzaSyC0lfgQAaH7B2RCC6VOZbLr8REwvTo7i9g"
        url = str("https://maps.googleapis.com/maps/api/place/textsearch"
                  "/json?query={}&key={}").format(input, API_KEY)

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


# """ >> test """
#
# input = "Exemple de ville"
#
# instance = map_request(input)
#
# print("Latitude : ", instance.latitude)
# print("Longitude : ", instance.longitude)
#
#
# """ test << """
