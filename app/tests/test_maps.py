"""Test of maps.py class."""

import requests
from app.API.maps import map_request


def test_get_location_coordinates_success(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """

    class MockResponse(object):
        def __init__(self):
            self.status_code = 200

        def json(self):
            """
            Return short response, just enough to get job done.
            Short version of response gathered with Postman
            from a request made with Google places documentation.
            """
            return {"html_attributions": [],
                    "results": [
                        {
                            "geometry": {
                                "location": {
                                    "lat": "Monkey_lat",
                                    "lng": "Monkey_lng"
                                },
                            },
                        },
                    ],
                    }

    def mock_get_coordinates(url):
        return MockResponse()

    # Apply the monkeypatch for requests.get to mock_get_coordinates
    monkeypatch.setattr(requests, "get", mock_get_coordinates)
    instance_of_map_request = map_request()
    assert (instance_of_map_request.latitude, instance_of_map_request.longitude) == ("Monkey_lat", "Monkey_lng")


def test_get_response_failure(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to failed
    THEN check the HTTP response
    """
    class MockResponse(object):
        def __init__(self):
            self.status_code = 404

        def json(self):
            return {'error': 'bad'}

    def mock_get_coordinates(url):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get_coordinates)
    r = map_request()
    assert (r.longitude, r.latitude) == (None, None)
