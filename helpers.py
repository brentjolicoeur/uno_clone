from card import COLORS
import random

def validate_npi(round):
    while round.npi < 0:
        round.npi += len(round.players)
    round.npi %= len(round.players)

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
    
def keep_playing():
    play_again = input("Would you like to play again? [Y]es or [N]o? ")

    while play_again.lower() != "y" and play_again.lower() != "n":
        play_again = input("Please only enter either y or n: ")
    if play_again.lower() == "y":
        return True
    else:
        return False
