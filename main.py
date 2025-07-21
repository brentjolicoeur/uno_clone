import game
#from card import Card
#from player import Player

def main():
    players, draw_pile, discard_pile = game.start() #initialize game, create players, draw pile, deal hands, first discard

    first_round = game.Round(players, draw_pile, discard_pile)

    while not first_round.round_finished:
        break
    
    for player in first_round.players:
        print(f"{player.name}'s hand is {player.hand}")
        print(f"{player.name}'s valid plays are {player.get_valid_plays(first_round.active_discard)}")
    
    print(f"There are {len(draw_pile)} cards left in the Draw Pile.")

    

if __name__ == "__main__":
    main()