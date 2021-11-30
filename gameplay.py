# future steps:
# loops for game flow:
#   number of hands to play / "play another hand?" / keep track of win/loss
#   change user position programmatically
# create web app
# collect results of hands, automate some analysis of results

from GameState import GameState
from Player import Player
from Deck import Deck
from Card import Card
from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer

hand_index = 0
playing = True
print("-------------------------")
print("Welcome to terminal poker! Shuffle up and deal!")

# for i in range(10000):
while playing == True:
    print("-------------------------")
    print("Hand number " + str(hand_index + 1))
    print("-------------------------")

    deck = Deck()
    deck.shuffle()

    # instantiate players, deal cards
    ### FIND A WAY TO PROGRAMMATICALLY DO THIS!!!
    position_helper = hand_index % 6

    if position_helper == 0:
        p1 = ComputerPlayer('p1', [deck.deal(), deck.deal()], 1)  # small blind
        p2 = ComputerPlayer('p2', [deck.deal(), deck.deal()], 2)  # big blind
        p3 = HumanPlayer('p3', [deck.deal(), deck.deal()], 3)  # UTG
        p4 = ComputerPlayer('p4', [deck.deal(), deck.deal()], 4)  # MP
        p5 = ComputerPlayer('p5', [deck.deal(), deck.deal()], 5)  # CO
        p6 = ComputerPlayer('p6', [deck.deal(), deck.deal()], 6)  # button
    elif position_helper == 1:
        p1 = ComputerPlayer('p1', [deck.deal(), deck.deal()], 1)  # small blind
        p2 = ComputerPlayer('p2', [deck.deal(), deck.deal()], 2)  # big blind
        p3 = ComputerPlayer('p3', [deck.deal(), deck.deal()], 3)  # UTG
        p4 = HumanPlayer('p4', [deck.deal(), deck.deal()], 4)  # MP
        p5 = ComputerPlayer('p5', [deck.deal(), deck.deal()], 5)  # CO
        p6 = ComputerPlayer('p6', [deck.deal(), deck.deal()], 6)  # button
    elif position_helper == 2:
        p1 = ComputerPlayer('p1', [deck.deal(), deck.deal()], 1)  # small blind
        p2 = ComputerPlayer('p2', [deck.deal(), deck.deal()], 2)  # big blind
        p3 = ComputerPlayer('p3', [deck.deal(), deck.deal()], 3)  # UTG
        p4 = ComputerPlayer('p4', [deck.deal(), deck.deal()], 4)  # MP
        p5 = HumanPlayer('p5', [deck.deal(), deck.deal()], 5)  # CO
        p6 = ComputerPlayer('p6', [deck.deal(), deck.deal()], 6)  # button
    elif position_helper == 3:
        p1 = ComputerPlayer('p1', [deck.deal(), deck.deal()], 1)  # small blind
        p2 = ComputerPlayer('p2', [deck.deal(), deck.deal()], 2)  # big blind
        p3 = ComputerPlayer('p3', [deck.deal(), deck.deal()], 3)  # UTG
        p4 = ComputerPlayer('p4', [deck.deal(), deck.deal()], 4)  # MP
        p5 = ComputerPlayer('p5', [deck.deal(), deck.deal()], 5)  # CO
        p6 = HumanPlayer('p6', [deck.deal(), deck.deal()], 6)  # button
    elif position_helper == 4:
        p1 = HumanPlayer('p1', [deck.deal(), deck.deal()], 1)  # small blind
        p2 = ComputerPlayer('p2', [deck.deal(), deck.deal()], 2)  # big blind
        p3 = ComputerPlayer('p3', [deck.deal(), deck.deal()], 3)  # UTG
        p4 = ComputerPlayer('p4', [deck.deal(), deck.deal()], 4)  # MP
        p5 = ComputerPlayer('p5', [deck.deal(), deck.deal()], 5)  # CO
        p6 = ComputerPlayer('p6', [deck.deal(), deck.deal()], 6)  # button
    elif position_helper == 5:
        p1 = ComputerPlayer('p1', [deck.deal(), deck.deal()], 1)  # small blind
        p2 = HumanPlayer('p2', [deck.deal(), deck.deal()], 2)  # big blind
        p3 = ComputerPlayer('p3', [deck.deal(), deck.deal()], 3)  # UTG
        p4 = ComputerPlayer('p4', [deck.deal(), deck.deal()], 4)  # MP
        p5 = ComputerPlayer('p5', [deck.deal(), deck.deal()], 5)  # CO
        p6 = ComputerPlayer('p6', [deck.deal(), deck.deal()], 6)  # button

    game_state = GameState([p3, p4, p5, p6, p1, p2])

    # post blinds
    game_state.live_players[4].pip(1)
    game_state.live_players[5].pip(2)

    # pre-flop betting
    print("pre-flop")
    print("---------------------------------")

    game_state.betting(2)
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
    game_state.betting(0)
    game_state.print_status()

    game_state.reset_ctp_and_current_bet()
    game_state.add_card_to_board(deck.deal())

    # turn betting
    print("turn")
    print("---------------------------------")
    game_state.betting(0)
    game_state.print_status()

    game_state.reset_ctp_and_current_bet()
    game_state.add_card_to_board(deck.deal())

    # river betting
    print("river")
    print("---------------------------------")
    game_state.betting(0)
    game_state.print_status()

    game_state.showdown()
    game_state.results()

    while True:
        keep_playing = input("Play another hand? Y/N ")
        if keep_playing.lower() == "n":
            print("Thank you for playing!")
            playing = False
            break
        elif keep_playing.lower() == "y":
            break
        else:
            print("Please enter a valid response.")

    hand_index += 1
