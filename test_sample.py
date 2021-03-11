"""Comment."""

import requests
from app.API.maps import map_request


def test_get_location_coordinates_success(monkeypatch, ):
    class MockResponse:
        """Comment."""

        def __init__(self):
            self.status_code = 200

        def json(self):
            return {
                       "html_attributions": [],
                       "results": [
                           {
                               "geometry": {
                                   "location": {
                                       "lat": 48.8975156,
                                       "lng": 2.3833993
                                   },
                               },
                           },
                       ],
                   }

    def mock_get_coordinates(url):
        return MockResponse

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get_coordinates)

    request = map_request()
    assert request.longitude, request.latitude == (2.3833993, 48.8975156)
    # print(request.longitude)
    # print(request.latitude)
