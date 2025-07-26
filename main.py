from card import build_new_game_deck
import game, helpers


def main():
    players, draw_pile, discard_pile = game.start() #initialize game, create players, draw pile, deal hands, first discard

    round = game.Round(players, draw_pile, discard_pile)

    continue_playing = True

    while continue_playing:
        while not round.round_finished:
            round.player_turn()
        round.score_round()
        continue_playing = helpers.keep_playing()

        if continue_playing:
            for player in players:
                player.hand = []
            new_deck = build_new_game_deck()
            game.deal_hands(players, new_deck)
            new_discard = game.make_discard(new_deck)

            round = game.Round(players, new_deck, new_discard)



    print("Thanks for playing!!")

    

if __name__ == "__main__":
    main()