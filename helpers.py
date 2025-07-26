"""
This module contains helper functions for game play.
"""

from card import COLORS, build_new_game_deck

import game
import random

def validate_npi(round):
    """
    Used to avoid index errors when looping through players

    Parameters
    ----------
    round : `Round` game object
        information concerning the current game round
    
    """
    while round.npi < 0:
        round.npi += len(round.players)
    round.npi %= len(round.players)

def skip_next_player(round):
    """
    Used to skip the next player in the game round

    Parameters
    ----------
    round : `Round` game object
        information concerning the current game round
    """
    round.npi += round.direction
    validate_npi(round)

def end_turn(round):
    """
    Used to finalize the end of a player's turn

    Checks to make sure the next player index is valid then sets the 
    active player as the next player in the player list using the npi.

    Parameters
    ----------
    round : `Round` game object
        information concerning the current game round
    """
    validate_npi(round)
    round.active_player = round.players[round.npi]
    if round.round_finished:
        return
    print(f"Passing turn to {round.active_player}.")
    round.pause()

def wild_get_new_color(round):
    """
    Used to determine the next color when a Wild card is played.

    If player is computer-controlled, a random color is chosen as the next
    color (previous color is allowed). If player is player-controlled, asks
    the user which color they want as the next color and validates the
    user input.

    Parameters
    ----------
    round : `Round` game object
        information concerning the current game round

    Returns
    -------
    new_color : str
        the new choice for active color
    """
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
    """
    Determines if the player wants to play another round of Uno

    Returns
    -------
    bool
        represents player's decision
    """
    play_again = input("Would you like to play again? [Y]es or [N]o? ")

    while play_again.lower() != "y" and play_again.lower() != "n":
        play_again = input("Please only enter either y or n: ")
    if play_again.lower() == "y":
        return True
    else:
        return False

def update_player_order(players):
    """
    Used to set the turn order for continuation rounds.

    If the player wants to keep playing this function will adjust the
    `players` list in place so that the previous first player is the 
    new dealer. Simulates rotating play order clockwise

    Parameters
    ----------
    players : list
        the previous list of players

    Returns
    -------
    players : list
        the reordered list of players
    """
    old_first = players.pop(0) #previous first player becomes the new dealer
    players.append(old_first)
    return players

def generate_next_round(players):
    """
    This function generates start conditions for the next round of play.

    Begins by updating the player order, resets all ```Player``` hands,
    creates a new game deck, deals player hands, and creates new 
    discard pile.

    Parameters
    ----------
    players : list
        the previous list of players

    Returns
    -------
    new_order : list
        the reorderd list of `Player` objects
    new_draw : list
        the new draw pile after dealing opening hands and first discard
    new_discard : list
        the new discard pile
    """
    new_order = update_player_order(players) #set new player order
    for player in players: #reset all player hands
        player.hand = []
    new_draw = build_new_game_deck()
    game.deal_hands(players, new_draw)
    new_discard = game.make_discard(new_draw)

    return new_order, new_draw, new_discard
