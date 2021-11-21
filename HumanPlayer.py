
from Player import Player

class HumanPlayer(Player):
    def __init__(self, name, hand, position_numeric, position_poker, ctp = 0, is_live = True, stack = 200, ctp_this_round = 0):
        super().__init__(name, hand, position_numeric, position_poker, ctp = 0, is_live = True, stack = 200, ctp_this_round = 0)

    # inherits all methods from Player class, and overrides act() methods

    def act(self, current_bet, prev_bet, live_players):
        print(f'previous bet: {prev_bet}')
        print(f'current bet: {current_bet}')
        print(f'your stack is: {self.stack}')

        # SITUATION 1: player is not facing a bet: check or bet
        if (current_bet - self.ctp_this_round) == 0:
            print("Enter 'C' for check")
            print("Enter 'B' for bet")

            while True:
                action = input("Enter your choice: ").lower()

                if action == "c":
                    break
                elif action == "b":
                    # special case: BB facing all limps must raise to at least 2 BB's if raising
                    if self.name == "p2" and live_players[-1].name =="p2" and current_bet == 2:
                        while True:
                            try:
                                raise_to = int(input("Enter your bet amount: "))
                                if (raise_to >= 4 and raise_to < self.stack):
                                    self.pip(raise_to - self.ctp_this_round)
                                    break
                                elif (raise_to == self.stack):
                                    self.pip(self.stack)
                                    break
                                else:
                                    print("Please enter a valid bet amount.")
                            except:
                                print("Please enter a valid bet amount.")

                            prev_bet = current_bet
                            current_bet = raise_to

                            print(f'raises to {raise_to}')
                            print(f'previous bet: {prev_bet}')
                            print(f'current bet: {current_bet}')

                    else:
                        while True:
                            try:
                                bet = int(input("Enter your bet amount: "))
                                if (bet >= 2 and bet <= self.stack):
                                    self.pip(bet)
                                    break
                                # special case of being left with 1 small blind
                                elif (bet == 1 and self.stack == 1):
                                    self.pip(bet)
                                    break
                                else:
                                    print("Please enter a valid bet amount.")
                            except:
                                print("Please enter a valid bet amount.")

                        prev_bet = current_bet
                        current_bet = bet

                    print(f'previous bet: {prev_bet}')
                    print(f'current bet: {current_bet}')

                    break

                else:
                    print("Please enter a valid selection.")
                    print("Enter 'C' for check")
                    print("Enter 'B' for bet")


        # SITUATION 2: player is facing an all-in bet: call or fold
        elif current_bet >= (self.stack + self.ctp_this_round):
            print("Enter 'C' for call")
            print("Enter 'F' for fold")

            while True:
                action = input("Enter your choice: ").lower()

                if action == "c":
                    self.pip(current_bet - self.ctp_this_round)
                    break
                elif action == "f":
                    self.fold()
                    break
                else:
                    print("Please enter a valid selection.")
                    print("Enter 'C' for call")
                    print("Enter 'F' for fold")


        # SITUATION 3: player is facing a bet which is not all-in: fold, call, or raise
        else:
            print("Enter 'C' for call")
            print("Enter 'R' for raise")
            print("Enter 'F' for fold")

            while True:
                action = input("Enter your choice: ").lower()

                if action == "c":
                    self.pip(current_bet - self.ctp_this_round)
                    break
                elif action == "r":
                    while True:
                        try:
                            raise_to = int(input("Enter your raise amount: "))
                            if (raise_to >= (current_bet + (current_bet - prev_bet)) and raise_to < self.stack):
                                self.pip(raise_to - self.ctp_this_round)
                                break
                            elif (raise_to == self.stack):
                                self.pip(self.stack)
                                break
                            else:
                                print("Please enter a valid selection.")
                                print("Enter 'C' for call")
                                print("Enter 'R' for raise")
                                print("Enter 'F' for fold")

                    break
                elif action == "f":
                    self.fold()
                    break
                else:
                    print("Please enter a valid selection.")
                    print("Enter 'C' for call")
                    print("Enter 'R' for raise")
                    print("Enter 'F' for fold")
