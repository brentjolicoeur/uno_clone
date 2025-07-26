class Player:
    """
    A class used to represent an individual Player

    ...

    Attributes
    ----------
    name : str
        the name of the player
    hand : list of Card objects
        represents the hand of cards the player holds
    cpu : bool, default True
        whether or not the player is computer-controlled or player-controlled
    score : int, default 0
        the number of points the player has scored

    Methods
    -------
    get_valid_plays(color, current_discard)
        determines which cards in a players hand are valid to play
    valid_draw_four(color)
        determines if a Wild Draw Four in hand is valid to play
    """
    def __init__(self, name, cpu=True):
        self.name = name
        self.hand = []
        self.cpu = cpu
        self.score = 0

    def __repr__(self):
        """
        Prints a representation of the Player object

        Returns
        -------
        str
            Represents the Player object using its `name` attribute
        """
        return self.name
    
    def get_valid_plays(self, color, current_discard):
        """
        Determines which cards in a player's `hand` are valid to play on their turn

        Parameters
        ----------
        color : str
            the "active" color for the turn. (necessary in case discard card was Wild)
        current_discard : Card object
            the Card at the top of the discard pile

        Returns
        -------
        list
            a list of Card objects which are valid to play on that turn
        """
        valid_plays = []

        if color == "Wild": #should only ever happen if the first discard of the game is a Wild
            #all cards in hand are valid
            return self.hand

        for card in self.hand:
            # all matching colors are valid
            if card.color == color:
                valid_plays.append(card)
            # check if Wild Draw Four is a valid play
            elif card.value == "Wild Draw Four":
                if self.valid_draw_four(color):
                    valid_plays.append(card)
            # add any value-matching, non-color-matching cards to valid_plays
            elif card.value == current_discard.value or card.value == "Wild":
                valid_plays.append(card)

        return valid_plays

    def valid_draw_four(self, color):
        """
        determines if a Wild Draw Four in hand is valid to play
        
        Parameters
        ----------
        color : str
            the current active color

        Returns
        ------
        bool
            represents whether the card is valid to play
        """
        valid = True
        for card in self.hand:
            if card.color == color:
                valid = False
        return valid