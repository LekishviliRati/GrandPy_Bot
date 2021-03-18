"""
Test of Input_parser class.
"""

from app.parser import Input_parser

input_1 = "Peux-tu, m'indiquer l'adresse d'openlassrooms ? "
input_2 = " Est-ce que tu connais l'addresse de la mairie de Paris ? "


def test_input_1(input):
    """Test of Input_parser class."""
    parsed = Input_parser(input)
    assert parsed.parsed_input == "adresse openlassrooms"
#     # To see what the function prints
#     # print(parsed.parsed_input)


test_input_1(input_1)


def test_input_2(input):
    """Test of Input_parser class."""
    parsed = Input_parser(input)
    assert parsed.parsed_input == "addresse mairie paris"
    # To see what the function prints
    # print(parsed.parsed_input)


test_input_2(input_2)
