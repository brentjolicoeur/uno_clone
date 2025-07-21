from card import Card

class Player:
    def __init__(self, name, cpu=True):
        self.name = name
        self.hand = []
        self.cpu = cpu

    def __repr__(self):
        return self.name
    
    def get_valid_plays(self, current_discard):
        valid_plays = []

        if current_discard.color == "Wild": #should only ever happen if the first discard of the game is a Wild
            #all cards in hand are valid
            return self.hand

        for card in self.hand:
            # all matching colors are valid
            if card.color == current_discard.color:
                valid_plays.append(card)
            # check if Wild Draw Four is a valid play
            elif card.value == "Wild Draw Four":
                if self.valid_draw_four(current_discard.color):
                    valid_plays.append(card)
            # add any value-matching, non-color-matching cards to valid_plays
            elif card.value == current_discard.value or card.value == "Wild":
                valid_plays.append(card)

        return valid_plays

    def valid_draw_four(self, color):
        valid = True
        for card in self.hand:
            if card.color == color:
                valid = False
        return valid