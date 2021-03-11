"""
Interact with Google Places API, to get coordinates.
"""

import os
import requests
import json


class map_request:
    """
    Use request to interact with Google Places API.
    """

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.get_coordinates()

    try:
        def get_coordinates(self):
            search = "Openclassrooms"
            API = "AIzaSyC0lfgQAaH7B2RCC6VOZbLr8REwvTo7i9g"
            # os.environ['API_KEY']
            url = str("https://maps.googleapis.com/maps/api/place/textsearch"
                      "/json?query={}&key={}").format(search, API)

            response = requests.get(url)

            assert response.status_code == 200

            j_result = response.json()

            if len(j_result["results"]) > 0:
                self.latitude = j_result['results'][0]['geometry']['location']['lat']
                self.longitude = j_result['results'][0]['geometry']['location']['lng']
    except ValueError:
        print("Cannot  reach API of Google Places")


""" test """

# json_result = map_request()
#
# print("Latitude : ", json_result.latitude)
# print("Longitude : ", json_result.longitude)

""" test """
