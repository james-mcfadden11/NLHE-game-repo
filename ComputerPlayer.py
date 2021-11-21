
from Player import Player
import random

class ComputerPlayer(Player):
    def __init__(self, name, hand, position_numeric, position_poker, ctp = 0, is_live = True, stack = 200, ctp_this_round = 0):
        super().__init__(name, hand, position_numeric, position_poker, ctp = 0, is_live = True, stack = 200, ctp_this_round = 0)

    # inherits all methods from Player class, and overrides act() methods

    def act(self, current_bet, prev_bet, live_players):

        # random number generator to make decisions on test version
        randomizer = random.randint(1, 100)
        # print(f'randomizer: {randomizer}')

        # SITUATION 1: player is not facing a bet: check or bet
        if (current_bet - self.ctp_this_round) == 0:
            # check 50% of time
            if randomizer < 50:
                print('checks')
                bet = 0

            # bet 50% of time
            else:
                # valid bet is > 2 and <= player stack
                # special case: BB facing all limps must raise to at least 2 BB's if raising
                if self.name == "p2" and live_players[-1].name =="p2" and current_bet == 2:
                    raise_to = random.randrange(4, self.stack)
                    self.pip(raise_to - self.ctp_this_round)

                    prev_bet = current_bet
                    current_bet = raise_to

                    print(f'raises to {raise_to}')
                    print(f'previous bet: {prev_bet}')
                    print(f'current bet: {current_bet}')

                # otherwise/normal case
                else:
                    # for de-bugging
                    print(f"{self.__str__()}'s stack: {self.stack}")

                    try:
                        bet = random.randint(2, self.stack)
                    except:
                        bet = random.randint(1, self.stack)

                    self.pip(bet)
                    prev_bet = current_bet
                    current_bet = bet

                    print(f'bets {bet}')

                print(f'previous bet: {prev_bet}')
                print(f'current bet: {current_bet}')


        # SITUATION 2: player is facing an all-in bet: call or fold
        elif current_bet >= (self.stack + self.ctp_this_round):
            # fold
            if randomizer > 50:
                self.fold()
                print('folds')
            # call
            else:
                self.pip(current_bet - self.ctp_this_round)
                print(f'calls {current_bet}')


        # SITUATION 3: player is facing a bet which is not all-in: fold, call, or raise
        else:
            # fold
            if randomizer > 75:
                self.fold()
                print('folds')
            # call
            elif 33 < randomizer <= 66:
                self.pip(current_bet - self.ctp_this_round)
                print(f'calls {current_bet}')
            # raise
            else:
                # minimum raise size is current_bet + (current_bet - prev_bet)
                # maximum raise is all-in
                try:
                    raise_to = random.randint((current_bet + (current_bet - prev_bet)), (self.stack + self.ctp_this_round))
                except:
                    raise_to = self.stack + self.ctp_this_round

                self.pip(raise_to - self.ctp_this_round)

                # re-define current bet to previous bet
                prev_bet = current_bet
                current_bet = raise_to

                print(f'raises to {raise_to}')
                print(f'previous bet: {prev_bet}')
                print(f'current bet: {current_bet}')

        return [current_bet, prev_bet]
