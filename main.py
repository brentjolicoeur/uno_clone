import game
from card import Card
from player import Player

def main():
    players, draw_pile, discard_pile = game.start()

    active_discard = discard_pile[-1]
    active_color = active_discard.color
    active_direction = 1
    next_player_index = 0

    print(f"The top card of the Discard Pile is {active_discard}.")

    print(f"The first to play will be {players[next_player_index]}")
    
    
    print(f"There are {len(draw_pile)} cards left in the Draw Pile.")

    for player in players:
        if not player.cpu:
            print(f"Your hand is: {player.hand}")
            valid_plays = player.get_valid_plays(active_color, active_discard)
            print(f"{player.name}'s valid plays are {valid_plays}.")
        else:
            print(f"{player.name}'s hand is {player.hand}")
            valid_plays = player.get_valid_plays(active_color, active_discard)
            print(f"{player.name}'s valid plays are {valid_plays}.")


if __name__ == "__main__":
    main()