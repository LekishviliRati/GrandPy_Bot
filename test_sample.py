# """Test of wiki.py """
#
# import requests
# from app.API.wiki import wiki_request
# from configuration import wiki_test_lng, wiki_test_lat
#
#
# def test_of_get_description_from_wiki_info_success(monkeypatch):
#     """
#     GIVEN a monkeypatched version of requests.get()
#     WHEN the HTTP response is set to successful
#     THEN check the HTTP response
#     """
#
#     class MockResponse(object):
#         def __init__(self):
#             self.status_code = 200
#
#         def json(self):
#             """
#             Return short response, just enough to get job done.
#             """
#             # Short version of response gathered with Postman
#             # from a request made with sandbox of wikimedia
#             return {
#                 "query": {
#                     "pages": {
#                         "239441": {
#                             "pageid": 239441,
#                             "title": "Monkey Title",
#                             "extract": "Monkey description",
#                             "fullurl": "Monkey URL",
#                         },
#                     },
#                 },
#             }
#
#     def mock_get_wiki_info(latitude, longitude):
#         return MockResponse()
#
#     expected_response = {
#         "title": "Monkey Title",
#         "description": "Monkey description",
#         "url": "Monkey URL"
#     }
#
#     # Apply the monkeypatch for requests.get to mock_get_coordinates
#     monkeypatch.setattr(requests, 'get', mock_get_wiki_info)
#     instance_of_wiki_request = wiki_request()
#     test_request = instance_of_wiki_request.get_wiki_info(wiki_test_lat, wiki_test_lng)
#     assert test_request == expected_response
#
#
#
# """Test of maps.py class."""
#
# import requests
# from app.API.maps import map_request
#
#
# def test_get_location_coordinates_success(monkeypatch):
#     """
#     GIVEN a monkeypatched version of requests.get()
#     WHEN the HTTP response is set to successful
#     THEN check the HTTP response
#     """
#
#     class MockResponse(object):
#         def __init__(self):
#             self.status_code = 200
#
#         def json(self):
#             # Return short response, just enough to get job done.
#             return {"html_attributions": [],
#                     "results": [
#                         {
#                             "geometry": {
#                                 "location": {
#                                     "lat": 48.8975156,
#                                     "lng": 2.3833993
#                                 },
#                             },
#                         },
#                     ],
#                     }
#
#     def mock_get_coordinates(url):
#         return MockResponse()
#
#     # Apply the monkeypatch for requests.get to mock_get_coordinates
#     monkeypatch.setattr(requests, "get", mock_get_coordinates)
#     instance_of_map_request = map_request()
#     assert (instance_of_map_request.latitude, instance_of_map_request.longitude) == (48.8975156, 2.3833993)
#
#
# def test_get_response_failure(monkeypatch):
#     """
#     GIVEN a monkeypatched version of requests.get()
#     WHEN the HTTP response is set to failed
#     THEN check the HTTP response
#     """
#     class MockResponse(object):
#         def __init__(self):
#             self.status_code = 404
#
#         def json(self):
#             return {'error': 'bad'}
#
#     def mock_get_coordinates(url):
#         return MockResponse()
#
#     monkeypatch.setattr(requests, 'get', mock_get_coordinates)
#     r = map_request()
#     assert (r.longitude, r.latitude) == (None, None)
