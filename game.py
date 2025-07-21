from card import Card
from player import Player

import random

def start():
    intro()
    players = generate_players()
    draw_pile = build_new_game_deck()
    deal_hands(players, draw_pile)
    discard_pile = make_discard(draw_pile)

    return players, draw_pile, discard_pile

def intro():
    print("********************")
    print("Welcome to UNO!")
    print("********************")

def generate_players():
    NAMES = [
    "Emma",
    "Liam",
    "Olivia",
    "Noah",
    "Ava",
    "Ethan",
    "Sophia",
    "Mason",
    "Isabella",
    "William",
    "Mia",
    "James",
    "Charlotte",
    "Benjamin",
    "Amelia",
    "Lucas",
    "Harper",
    "Henry",
    "Evelyn",
    "Alexander"
]
    players = []

    player_name = input("What is your name? ")

    players.append(Player(player_name, cpu=False))

    num_opponents = get_num_opponents()

    opponents = random.sample(NAMES,num_opponents)
    print("********************")
    print("Today you will be playing against:")
    for opponent in opponents:
        print(opponent)

    for i in range(num_opponents):
        players.append(Player(f"{opponents[i]}"))
    
    return players

def get_num_opponents():
    valid_num = False
    while not valid_num:
        try:
            num_opponents = int(input("How many opponents would you like? (1-3) "))
            if 1 <= num_opponents <= 3:
                valid_num = True
            else:
                print("Please enter a number between 1 and 3. ")
        except:
            print("Please enter a valid digit.")
    return num_opponents

def build_new_game_deck():
    COLORS = ("red", "yellow", "green", "blue")
    STANDARD = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    SPECIAL = ("Skip", "Reverse", "Draw Two")
    WILDS = ("Wild", "Wild Draw Four")

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

    random.shuffle(deck)
    return deck

def deal_hands(players, deck):
    random.shuffle(players)
    print("********************")
    print(f"The Dealer will be {players[-1]}")
    print("********************")
    print("Dealing 7 cards to each player")
    for _ in range(7):
        for player in players:
            card = deck.pop()
            player.hand.append(card)
    print("********************")

def make_discard(deck):
    discard_pile = []
    start_card = deck.pop()
    if start_card.value == "Wild Draw Four":
        while True:
            print("Discard Pile cannot start with a Wild Draw Four. Reshuffling the Draw Pile and discarding a new card.")
            deck.append(start_card)
            random.shuffle(deck)
            start_card = deck.pop()
            if start_card.value != "Draw Four":
                break
    discard_pile.append(start_card)
    return discard_pile