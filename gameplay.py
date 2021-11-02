# future steps:
# change betting function to have user inputs and check for validity
# create web app
# loop for changing table positions
# collect results of hands, automate some analysis of results

# loops for game flow:
# number of hands to play / "play another hand?"
# change user position

from GameState import GameState
from Player import Player
from Deck import Deck
from Card import Card

import random

deck = Deck()
deck.shuffle()

# instantiate players, deal cards
p1 = Player('p1', 1, [deck.deal(), deck.deal()])  # small blind
p2 = Player('p2', 2, [deck.deal(), deck.deal()])  # big blind
p3 = Player('p3', 3, [deck.deal(), deck.deal()])  # UTG
p4 = Player('p4', 4, [deck.deal(), deck.deal()])  # MP
p5 = Player('p5', 5, [deck.deal(), deck.deal()])  # CO
p6 = Player('p6', 6, [deck.deal(), deck.deal()])  # button

game_state = GameState([p3, p4, p5, p6, p1, p2])

# post blinds
game_state.add_to_pot(p1.pip(1))
game_state.add_to_pot(p2.pip(2))

game_state.print_status()

# pre-flop betting
game_state.betting()

game_state.reset_ctp_and_current_bet()
game_state.reorder_for_flop()

# deal flop
game_state.add_card_to_board(deck.deal())
game_state.add_card_to_board(deck.deal())
game_state.add_card_to_board(deck.deal())

game_state.print_status()

# flop betting
game_state.betting()

game_state.reset_ctp_and_current_bet()
game_state.add_card_to_board(deck.deal())

# turn betting
game_state.betting()

game_state.reset_ctp_and_current_bet()
game_state.add_card_to_board(deck.deal())

# river betting
game_state.betting()

# showdown()
# results()
