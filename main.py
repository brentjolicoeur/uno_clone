import game
#from card import Card
#from player import Player

def main():
    players, draw_pile, discard_pile = game.start() #initialize game, create players, draw pile, deal hands, first discard

    first_round = game.Round(players, draw_pile, discard_pile)

    while not first_round.round_finished:
        first_round.player_turn()
    
    first_round.score_round()
    print("Thanks for playing!!")

    

if __name__ == "__main__":
    main()