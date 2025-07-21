import game
#from card import Deck
#from player import Player

def main():
    players, draw_pile, discard_pile = game.start()

    print(f"The first to play will be {players[0]}")
    
    print(f"The top card of the Discard Pile is {discard_pile[-1]}.")
    print(f"There are {len(draw_pile)} cards left in the Draw Pile.")


if __name__ == "__main__":
    main()