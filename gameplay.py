# future steps:
# change betting function to have user inputs and check for validity
# loops for game flow:
#   number of hands to play / "play another hand?"
#   change user position
# create web app
# collect results of hands, automate some analysis of results

from GameState import GameState
from Player import Player
from Deck import Deck
from Card import Card

import random

hand = 1

for i in range(500):
    print("-------------------------")
    print("Hand number " + str(hand))
    print("-------------------------")

    deck = Deck()
    deck.shuffle()

    # instantiate players, deal cards
    # p1 = Player('p1', [deck.deal(), deck.deal()], 1, 'sb', True)  # small blind
    # p2 = Player('p2', [deck.deal(), deck.deal()], 2, 'bb', True)  # big blind
    # p3 = Player('p3', [deck.deal(), deck.deal()], 3, 'utg', True)  # UTG
    # p4 = Player('p4', [deck.deal(), deck.deal()], 4, 'middle', True)  # MP
    # p5 = Player('p5', [deck.deal(), deck.deal()], 5, 'cut-off', True)  # CO
    # p6 = Player('p6', [deck.deal(), deck.deal()], 6, 'button', True)  # button

    p1 = Player('p1', [deck.deal(), deck.deal()], 1, 'sb', False)  # small blind
    p2 = Player('p2', [deck.deal(), deck.deal()], 2, 'bb', False)  # big blind
    p3 = Player('p3', [deck.deal(), deck.deal()], 3, 'utg', False)  # UTG
    p4 = Player('p4', [deck.deal(), deck.deal()], 4, 'middle', False)  # MP
    p5 = Player('p5', [deck.deal(), deck.deal()], 5, 'cut-off', False)  # CO
    p6 = Player('p6', [deck.deal(), deck.deal()], 6, 'button', False)  # button



    game_state = GameState([p3, p4, p5, p6, p1, p2])

    # post blinds
    game_state.add_to_pot(p1.pip(1))
    game_state.add_to_pot(p2.pip(2))

    # pre-flop betting
    print("pre-flop")
    print("---------------------------------")

    game_state.betting()
    game_state.print_status()

    game_state.reset_ctp_and_current_bet()
    game_state.reorder_for_flop()

    game_state.print_status()

    # deal flop
    game_state.add_card_to_board(deck.deal())
    game_state.add_card_to_board(deck.deal())
    game_state.add_card_to_board(deck.deal())

    game_state.print_status()

    # flop betting
    print("flop")
    print("---------------------------------")
    game_state.betting()
    game_state.print_status()

    game_state.reset_ctp_and_current_bet()
    game_state.add_card_to_board(deck.deal())

    # turn betting
    print("turn")
    print("---------------------------------")
    game_state.betting()
    game_state.print_status()

    game_state.reset_ctp_and_current_bet()
    game_state.add_card_to_board(deck.deal())

    # river betting
    print("river")
    print("---------------------------------")
    game_state.betting()
    game_state.print_status()

    # showdown()
    # results()

    hand += 1
