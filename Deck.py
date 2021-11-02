from Card import Card
import random

suits = ['h','d','c','s']
ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
ranks_ace_high = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
ranks_ace_low = {'A':1,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

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
