from termcolor import colored

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
