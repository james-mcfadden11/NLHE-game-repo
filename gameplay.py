# future steps:
# change betting function to have user inputs and check for validity
# create web app
# loop for changing table positions
# collect results of hands, automate some analysis of results

# connect to modules and functions
from setup import setup
from betting import betting
from reset import reset
from reorder_for_flop import reorder_for_flop
from showdown import showdown
from results import results
from test import test


# loops for game flow:
# number of hands to play / "play another hand?"
# change user position 


print("Starting game!")

setup()

betting()

reorder_for_flop()
reset()
board.append(deck.deal())
board.append(deck.deal())
board.append(deck.deal())
betting()

reset()
board.append(deck.deal())
betting()

reset()
board.append(deck.deal())
betting()

showdown()

results()
