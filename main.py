import game
from card import Card
from player import Player

def main():
    players, draw_pile, discard_pile = game.start() #initialize game, create players, draw pile, deal hands, first discard

    active_discard = discard_pile[-1]
    active_color = active_discard.color
    active_direction = 1  # will either be 1 or -1 to determine who next player is as we cycle through indices
    next_player_index = 0

    print(f"The top card of the Discard Pile is {active_discard}.")

    # Handle special cards as the first discard
    if active_discard.special:
        match active_discard.value:
            case "Skip":
                print(f"Uh Oh! {players[next_player_index]} loses their first turn!")
                next_player_index += 1
            case "Reverse":
                print("Looks like we are changing directions!")
                active_direction *= -1
            case "Draw Two":
                print(f"Oh No! {players[next_player_index]} must draw 2 cards and loses their first turn.")
                game.draw_card(players[next_player_index], draw_pile, 2)
                next_player_index += 1
            case _:
                print(f"Looks like {players[next_player_index]} will get to pick the first color!")

    print(f"The first to play will be {players[next_player_index]}")
    
    
    print(f"There are {len(draw_pile)} cards left in the Draw Pile.")

    

if __name__ == "__main__":
    main()