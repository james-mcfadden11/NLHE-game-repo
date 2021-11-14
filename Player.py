
class Player:
    def __init__(self, name, hand, position_numeric, position_poker, is_human, ctp = 0, is_live = True, stack = 200, ctp_this_round = 0):
        self.name = name
        self.position_numeric = position_numeric
        self.position_poker = position_poker
        self.is_human = is_human
        self.is_live = is_live  # Boolean
        self.hand = hand  # composed of 2 card objects supplied by deck.deal()
        self.stack = stack  # integer, default 100
        self.ctp = ctp  # integer, contributed to pot
        self.ctp_this_round = ctp_this_round  # to reset each betting round to 0
        # self.hand_values = [card.value_ace_high for card in self.hand]
        # self.hand_suits = [card.suit for card in self.hand]

    def __str__(self):
        return self.name

    # pip --> put in pot
    # ctp --> contributed to pot
    def pip(self, amount):
        self.amount = amount
        self.ctp +=  self.amount
        self.stack -= self.amount
        self.ctp_this_round += self.amount
        return amount

    def fold(self):
        self.is_live = False

    def human_action(self):
        print("Enter your choice: check (c) or bet (b)")
        selection = input()
        if selection == "c":
            print("checks")
            bet = 0
        elif selection == "b":
            while True:
                print("Enter a valid bet size as an integer:")
                try:
                    bet = input()
                    bet = int(bet)
                    if bet > 2 and bet < self.stack:
                        break
                    else:
                        continue
                except:
                    continue
        return bet




    # def computer_action(self):
