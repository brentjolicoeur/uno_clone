

def set_next_player_index(index, num_players):
    while index < 0:
        index += num_players
    index %= num_players
    return index

def skip_next_player(round):
    round.npi += round.direction
    round.npi = set_next_player_index(round.npi, len(round.players))

def end_turn(round):
    round.npi %= len(round.players)
    round.active_player = round.players[round.npi]
    print(f"Passing turn to {round.active_player}.")