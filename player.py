from card import Card

class Player:
    def __init__(self, name, cpu=True):
        self.name = name
        self.hand = []
        self.cpu = cpu

    def __repr__(self):
        return self.name
    
    def get_valid_plays(self, active_color, current_discard):
        valid_plays = []
        color_matches = []  # will be used to check if Wild Draw Four is legal

        if active_color == "Wild": #should *eventually* only ever happen if the first discard of the game is a Wild
            #all cards in hand are valid
            return self.hand

        for card in self.hand:
            # all matching colors are legal
            if card.color == active_color:
                color_matches.append(card) # will use this set to extend valid_plays after checking for Draw Four
            # add any value-matching, non-color-matching cards to valid_plays
            if card.value == current_discard.value and card not in color_matches:
                valid_plays.append(card)
        valid_plays.extend(color_matches)
        #check if hand contains a Draw Four Wild and add to valid plays if it meets the criteria (no matching colors)
        for card in self.hand:
            if card.color == "Wild":
                if card.value == "Wild Draw Four":
                    if len(color_matches) == 0:
                        #legal to play
                        valid_plays.append(card)
                    # Otherwise not legal to play--do nothing
                else: # will only trigger if it's a regular wild
                    valid_plays.append(card)

        return valid_plays
