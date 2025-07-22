from card import COLORS
import random

def validate_npi(round):
    while round.npi < 0:
        round.npi += len(round.players)
    round.npi %= len(round.players)

""" def set_next_player_index(index, num_players):
    while index < 0:
        index += num_players
    index %= num_players
    return index
 """
def skip_next_player(round):
    round.npi += round.direction
    validate_npi(round)

def end_turn(round):
    validate_npi(round)
    round.active_player = round.players[round.npi]
    if round.round_finished:
        return
    print(f"Passing turn to {round.active_player}.")
    round.pause()

def wild_get_new_color(round):
    player = round.active_player
    if player.cpu:
        new_color = random.choice(COLORS)
        print(f"{player} chooses {new_color}")
        return new_color
    else:
        valid_choice = False
        while not valid_choice:
            new_color = input("Please pick a new color (please type full color name): ")
            if new_color.lower() in COLORS:
                valid_choice = True
            else:
                print("Not a valid color choice.")
                new_color = input("Please pick a new color (please type full color name): ")
        print(f"{player} chooses {new_color}")
        return new_color