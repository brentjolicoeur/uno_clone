from termcolor import colored
import random

COLORS = ("red", "yellow", "green", "blue")
STANDARD = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two")
SPECIAL = ("Wild", "Draw Four")

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        if self.color == "red":
            return colored(f"{self.color} {self.value}", "red")
        if self.color == "yellow":
            return colored(f"{self.color} {self.value}", "yellow")
        if self.color == "green":
            return colored(f"{self.color} {self.value}", "green")
        if self.color == "blue":
            return colored(f"{self.color} {self.value}", "blue")
        if self.color == "Wild":
            return f"{self.value}"
    
class Deck:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def __repr__(self):
        return f"The {self.name} has {len(self.cards)} cards in it."

    def build_new_game_deck(self):
        for color in COLORS:
            for value in STANDARD:
                for _ in range(2):
                    self.cards.append(Card(color, value))

        for value in SPECIAL:
            for _ in range(4):
                self.cards.append(Card("Wild", value))

        random.shuffle(self.cards)
    

game_deck = Deck("Draw Deck")
game_deck.build_new_game_deck()

print(game_deck)
print(game_deck.cards)
    