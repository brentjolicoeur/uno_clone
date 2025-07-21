from termcolor import colored

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
