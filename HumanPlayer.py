
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
                    # betting logic - refer to ComputerPlayer for validation
                    break
                else:
                    print("Please enter a valid selection.")


        # SITUATION 2: player is facing an all-in bet: call or fold
        elif current_bet >= (self.stack + self.ctp_this_round):
            print("Enter 'C' for call")
            print("Enter 'F' for fold")

            while True:
                action = input("Enter your choice: ").lower()

                if action == "c":
                    self.pip(current_bet)
                    break
                elif action == "f":
                    self.fold()
                    break
                else:
                    print("Please enter a valid selection.")


        # SITUATION 3: player is facing a bet which is not all-in: fold, call, or raise
        else:
            print("Enter 'C' for call")
            print("Enter 'R' for raise")
            print("Enter 'F' for fold")

            while True:
                action = input("Enter your choice: ").lower()

                if action == "c":
                    self.pip(current_bet)
                    break
                elif action == "r":
                    # raising logic - refer to ComputerPlayer for validation
                    break
                elif action == "f":
                    self.fold()
                    break
                else:
                    print("Please enter a valid selection.")
