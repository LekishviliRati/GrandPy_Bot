"""
Test of Input_parser class.
"""
import json

from app.API.maps import map_request


class test_map_request:

    text = "Paris"

    def test_return_type(self, monkeypatch):

        data = {"results": [{
                        "formatted_address": "7 Cité Paradis, 75010 Paris,"
                                             "France",
                        "geometry": {
                          "location": {
                              "lat": 48.8748465,
                              "lng": 2.3504873
                                            }
                                    }
                        }]}

        class mockrequestget:
            def __init__(self, url, headers=None):
                self.status_code = 200
                self.text = json.dumps(data)

        monkeypatch.setattr('app.API.Gmaps.gmaps_request.requests.get',
                            mockrequestget)
        r = map_request.request(self.text)
        assert isinstance(r, dict)

    def test_type_return_value_when_error(self, monkeypatch):
        class MockRequestsGet:
            def __init__(self, url, headers=None):
                self.status_code = 404

        monkeypatch.setattr('app.API.Gmaps.gmaps_request.requests.get',
                            MockRequestsGet)

        r = map_request.request(self.text)
        assert isinstance(r, str)

    def test_bad_status_code(self, monkeypatch):
        class MockRequestsGet:
            def __init__(self, url, headers=None):
                self.status_code = 500

        monkeypatch.setattr('app.API.Gmaps.gmaps_request.requests.get',
                            MockRequestsGet)

        response = map_request.request(self.text)
        assert response == "Problème pour contacter l'API Google Places"