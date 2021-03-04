"""
Parse user input, to look for an adress.
"""
from unidecode import unidecode

from configuration.globals import STOPWORDS, PUNCTUATION


class Input_parser:
    """Represents the parser."""

    def __init__(self, user_input):
        self.user_input = user_input
        self.delete_accents()
        self.make_lower_case()
        self.delete_punctuation()
        self.split_words()
        self.save_key_words()
        self.parsed_input = self.user_input

    def delete_accents(self):
        """Removes accents from user_input."""
        self.user_input = unidecode(self.user_input)

    def make_lower_case(self):
        """Makes user_input in lower case."""
        self.user_input = self.user_input.lower()

    def delete_punctuation(self):
        """Removes punctuation from user input."""
        for char in self.user_input:
            if char in PUNCTUATION:
                self.user_input = self.user_input.replace(char, " ")

    def split_words(self):
        """Split user_input into a list of words."""
        self.user_input = self.user_input.split()

    def save_key_words(self):
        """Save only key words using stopwords."""
        key_words = \
            [word for word in self.user_input if word not in STOPWORDS]
        self.user_input = ' '.join(key_words)
