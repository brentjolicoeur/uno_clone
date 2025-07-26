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
            next_players, next_draw, next_discard = helpers.generate_next_round(players)
            round = game.Round(next_players, next_draw, next_discard)
   
    print("The final scores are:")
    for player in players:
        print(f"{player.name}: {player.score} points")
    print("Thanks for playing!!")

    

if __name__ == "__main__":
    main()