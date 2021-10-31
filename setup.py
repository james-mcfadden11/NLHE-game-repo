def setup():

    print("setup() called")

    import random

    suits = ['h','d','c','s']
    ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    ranks_ace_high = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    ranks_ace_low = {'A':1,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

    # create object class Card with attributes rank, suit
    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value_ace_high = ranks_ace_high[rank]
            self.value_ace_low = ranks_ace_low[rank]
        def __str__(self):
            return self.rank + self.suit

    # create object class Deck
    class Deck:
        def __init__(self):
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))  # adds cards to the deck one by one
        def __str__(self):
            deck_comp = ''
            for card in self.deck:
                deck_comp += card.__str__() + ' '
                # card here is still an instance of the Card class, so need to call the .__str__ to get a string of a single card
            return deck_comp
        def shuffle(self):
            random.shuffle(self.deck)
        def deal(self):
            single_card = self.deck.pop()
            return single_card
            # returns a card from the deck (bottom of the deck) as variable single_card

    #instantiate a deck and shuffle
    deck = Deck()
    deck.shuffle()

    # create object class Player
    class Player:

        def __init__(self, name, ctp = 0, is_live = True, stack = 200, ctp_this_round = 0):
            self.name = name
            self.is_live = is_live  # Boolean
            self.hand = [deck.deal(), deck.deal()]  # composed of 2 card objects supplied by deck.deal()
            self.stack = stack  # integer, default 100
            self.ctp = ctp  # integer, contributed to pot
            self.ctp_this_round = ctp_this_round  # to reset each betting round to 0
            self.hand_values = [card.value_ace_high for card in self.hand]
            self.hand_suits = [card.suit for card in self.hand]

        def __str__(self):
            return print(self.name)
            # return f"{self.name}'s hand is {self.hand[0]} {self.hand[1]} and stack is {self.stack}"

        # pip = put in pot
        # ctp = contributed to pot
        def pip(self, amount):
            self.amount = amount
            self.ctp = self.ctp + self.amount
            self.stack = self.stack - self.amount
            self.ctp_this_round = self.ctp_this_round + self.amount

        def fold(self):
            self.is_live = False
            # remove folded players from live_players is done in each betting round loop


    # instantiate players, deal cards
    p1 = Player('p1')  # small blind
    p2 = Player('p2')  # big blind
    p3 = Player('p3')  # UTG
    p4 = Player('p4')  # MP
    p5 = Player('p5')  # CO
    p6 = Player('p6')  # button

    live_players = [p3, p4, p5, p6, p1, p2]

    # post blinds
    p1.pip(1)
    p2.pip(2)

    current_bet = 2
    prev_bet = 0

    live_players_ctp = [x.ctp for x in live_players]
    live_players_ctp_this_round = [x.ctp_this_round for x in live_players]

    pot = p1.ctp + p2.ctp + p3.ctp + p4.ctp + p5.ctp + p6.ctp

    board = []
