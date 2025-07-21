from termcolor import colored
import random

COLORS = ("red", "yellow", "green", "blue")
STANDARD = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
SPECIAL = ("Skip", "Reverse", "Draw Two")
WILDS = ("Wild", "Wild Draw Four")

class Card:
    def __init__(self, color, value, special=False):
        self.color = color
        self.value = value
        self.special = special

    def __repr__(self):
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
                    colors_index += 1
                    colors_index %= 4
            return string

def build_new_game_deck():
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