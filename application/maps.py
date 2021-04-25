"""
Interact with Google Places API,
to get coordinates with given parsed input.
"""

import requests
from configuration.globals import API_KEY


class map_request:
    """
    This class will return latitude and longitude,
    for user research.
    """
    def __init__(self, input):
        self.latitude = None
        self.longitude = None
        self.get_coordinates(input)

    def get_coordinates(self, input):
        """Get latitude and longitude."""

        # Prepare url to make API call.
        url = str("https://maps.googleapis.com/maps/api/place/textsearch"
                  "/json?query={}&key={}").format(input, API_KEY)

        response = requests.get(url)

        # Code 200 means successful response.
        if response.status_code == 200:
            response_data = response.json()
            if len(response_data["results"]) > 0:
                self.latitude = \
                    response_data['results'][0]['geometry']['location']['lat']
                self.longitude = \
                    response_data['results'][0]['geometry']['location']['lng']
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
