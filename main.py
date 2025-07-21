import game
#from card import Deck
from player import Player

def main():
    players, draw_pile, discard_pile = game.start()

    print(f"The first to play will be {players[0]}")
    
    print(f"The top card of the Discard Pile is {discard_pile[-1]}.")
    print(f"There are {len(draw_pile)} cards left in the Draw Pile.")

    for player in players:
        if not player.cpu:
            print(f"Your hand is: {player.hand}")
        else:
            print(f"{player.name}'s hand is {player.hand}")


if __name__ == "__main__":
    main()