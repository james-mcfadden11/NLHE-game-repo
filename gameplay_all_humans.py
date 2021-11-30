
from GameState import GameState
from Player import Player
from Deck import Deck
from Card import Card
from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer

hand = 1

for i in range(1):
    print("-------------------------")
    print("Hand number " + str(hand))
    print("-------------------------")

    deck = Deck()
    deck.shuffle()

    # instantiate players, deal cards
    p1 = HumanPlayer('p1', [deck.deal(), deck.deal()], 1, 'sb')  # small blind
    p2 = HumanPlayer('p2', [deck.deal(), deck.deal()], 2, 'bb')  # big blind
    p3 = HumanPlayer('p3', [deck.deal(), deck.deal()], 3, 'utg')  # UTG
    p4 = HumanPlayer('p4', [deck.deal(), deck.deal()], 4, 'middle')  # MP
    p5 = HumanPlayer('p5', [deck.deal(), deck.deal()], 5, 'cut-off')  # CO
    p6 = HumanPlayer('p6', [deck.deal(), deck.deal()], 6, 'button')  # button

    game_state = GameState([p3, p4, p5, p6, p1, p2])

    # post blinds
    p1.pip(1)
    p2.pip(2)

    # pre-flop betting
    print("pre-flop")
    print("---------------------------------")

    game_state.print_status()
    game_state.betting(2)

    game_state.reset_ctp_and_current_bet()
    game_state.reorder_for_flop()

    # deal flop
    game_state.add_card_to_board(deck.deal())
    game_state.add_card_to_board(deck.deal())
    game_state.add_card_to_board(deck.deal())

    game_state.print_status()

    # flop betting
    print("flop")
    print("---------------------------------")
    game_state.betting(0)
    game_state.print_status()

    game_state.reset_ctp_and_current_bet()
    game_state.add_card_to_board(deck.deal())

    # turn betting
    print("turn")
    print("---------------------------------")
    game_state.print_status()
    game_state.betting(0)


    game_state.reset_ctp_and_current_bet()
    game_state.add_card_to_board(deck.deal())

    # river betting
    print("river")
    print("---------------------------------")
    game_state.print_status()
    game_state.betting(0)

    game_state.showdown()
    game_state.results()

    hand += 1
