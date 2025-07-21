import game
from card import Card
from player import Player

def main():
    players, draw_pile, discard_pile = game.start() #initialize game, create players, draw pile, deal hands, first discard

    first_round = game.Round(players, draw_pile, discard_pile)
    
    
    print(f"There are {len(draw_pile)} cards left in the Draw Pile.")

    

if __name__ == "__main__":
    main()