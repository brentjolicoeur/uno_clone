from termcolor import colored
import random

COLORS = ("red", "yellow", "green", "blue")
STANDARD = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
SPECIAL = ("Skip", "Reverse", "Draw Two")
WILDS = ("Wild", "Wild Draw Four")

class Card:
    """
    A class used to represent an individual Card

    ...

    Attributes
    ----------
    color : str
        the color of the card
    value : int or str
        represents the printed value or effect of the card
    special : bool, default False
        whether or not the card has a special ability when played (default False)
    points : int, default 0
        the amount of points the card is worth -- gets set by the `_set_points()` method

    Methods
    ------
    _set_points()
        Assigns a point value to the card for scoring
    """

    def __init__(self, color, value, special=False):
        """
        Initializes an instance of the Card class.

        Parameters
        ----------
        color : str
            the color of the card
        value : int or str
            represents the printed value or effect of the card
        special : bool, default False
            whether or not the card has a special ability when played (default False)
        
        """
        self.color = color
        self.value = value
        self.special = special
        self.points = 0
        self._set_points()

    def __repr__(self):
        """Prints a representation of the Card object to the terminal using colord text.

        Uses the colored() method of the termcolor module to print the card representation
        using colored text. If the card is a Wild card, it will print the letters in sequential colors.

        Returns
        -------
        str
            Colored representation of the Card using it's `color` and `value`
        """
        COLORS = ("red", "yellow", "green", "blue")

        if self.color == "red":
            return colored(f"{self.color} {self.value}", "red")
        if self.color == "yellow":
            return colored(f"{self.color} {self.value}", "yellow")
        if self.color == "green":
            return colored(f"{self.color} {self.value}", "green")
        if self.color == "blue":
            return colored(f"{self.color} {self.value}", "blue")
        if self.color == "Wild":
            string = ""
            colors_index = 0
            for char in self.value:
                if char == " ":
                    string += char
                else:
                    string += colored(char, COLORS[colors_index])
                    colors_index = (colors_index + 1) % 4

            return string

    def _set_points(self):
        """Sets the point values for each card.

        Numbered cards are worth their face value.  Colored specials are worth 20 points.
        Wild cards are worth 50 points.
        """
        if not self.special:
            self.points = self.value
        elif self.color == "Wild":
            self.points = 50
        else:
            self.points = 20

def build_new_game_deck():
    """
    Builds a new deck of Uno cards to draw from

    Returns
    -------
    list
        a list of `Card` objects representing a full Uno Deck
    """
    deck = []

    for color in COLORS:
        for value in STANDARD:
            for _ in range(2):
                deck.append(Card(color, value))
        for value in SPECIAL:
            for _ in range(2):
                deck.append(Card(color, value, special=True))

    for value in WILDS:
        for _ in range(4):
            deck.append(Card("Wild", value, special=True))

    for _ in range(7):
        random.shuffle(deck)

    return deck