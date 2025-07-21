from card import Deck

def game_start():
    print("********************")
    print("Welcome to UNO!")

    main_deck = Deck("Draw Deck")
    main_deck.build_new_game_deck()

    print(main_deck)
    print(main_deck.cards)
    print(f"The top card of the deck is {main_deck.cards[-1]}")

game_start()