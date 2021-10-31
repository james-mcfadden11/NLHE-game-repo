suits = ['h','d','c','s']
ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
ranks_ace_high = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
ranks_ace_low = {'A':1,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value_ace_high = ranks_ace_high[rank]
        self.value_ace_low = ranks_ace_low[rank]

    def __str__(self):
        return self.rank + self.suit
