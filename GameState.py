from Player import Player
import random

class GameState:
    def __init__(self, live_players):
        self.pot = 0
        self.board = []
        self.live_players = live_players
        self.live_players_ctp = [0, 0, 0, 0, 0, 0]
        self.live_players_ctp_this_round = [0, 0, 0, 0, 0, 0]
        self.current_bet = 2
        self.prev_bet = 0

    def update_live_players(self):
        self.live_players = [player for player in self.live_players if player.is_live == True]
        self.live_players_ctp = [player.ctp for player in self.live_players]
        self.set_live_players_ctp_this_round = [player.ctp_this_round for player in self.live_players]

    def add_to_pot(self, amount):
        self.pot += amount

    def add_card_to_board(self, card):
        self.board.append(card)

    def reset_ctp_and_current_bet(self):
        for player in self.live_players:
            player.ctp_this_round = 0
        self.current_bet = 0
        self.prev_bet = 0

    def reorder_for_flop(self):
        if self.live_players[5].is_live:
            self.live_players.insert(0, self.live_players.pop())
        if self.live_players[4].is_live:
            self.live_players.insert(0, self.live_players.pop())

    def print_status(self):
        print("pot: " + str(self.pot))
        print("board: " + str([card.__str__() for card in self.board]))
        print("live players: " + str([player.__str__() for player in self.live_players]))

    def betting(self):
        round = 0
        # run betting sequence if not all-in and more than one player live
        if self.live_players[0].ctp < 200 and len(self.live_players) > 1:

            while len(self.live_players) > 1 and len(set(self.live_players_ctp_this_round)) != 1 or round == 0:

                for player in self.live_players:
                    # break if all fold except one player or if all players ctp same amount after first round
                    if len(self.live_players) == 1 or (len(set(self.live_players_ctp_this_round)) == 1 and round > 0):
                        break

                    player.__str__()

                    # random number generator to make decisions on test version
                    randomizer = random.randint(1, 100)
                    print(f'randomizer is {randomizer}')

                    # if player is not facing a bet: check or bet
                    if (self.current_bet - player.ctp_this_round) == 0:
                        # check 50% of time
                        if randomizer < 50:
                            print('checks')
                        # bet 50% of time
                        # valid bet is > 2 and less than player stack
                        else:
                            # special case: BB facing all limps must raise to at least 2 BB's if raising
                            bet = random.randint((2 + player.ctp_this_round), player.stack)
                            self.add_to_pot(player.pip(bet))
                            self.prev_bet = self.current_bet
                            self.current_bet = bet
                            print(f'bets {bet}')
                            print(f'previous bet is now {self.prev_bet}')
                            print(f'current bet is now {self.current_bet}')

                    # if player is facing an all-in bet: call or fold
                    elif self.current_bet >= (player.stack + player.ctp_this_round):
                        # fold
                        if randomizer > 50:
                            player.fold()
                            print('folds')
                        # call
                        else:
                            self.add_to_pot(player.pip(self.current_bet - player.ctp_this_round))
                            print(f'calls {self.current_bet}')

                    # if player is facing a bet which is not all-in: fold, call, or raise
                    else:
                        # fold
                        if randomizer > 75:
                            player.fold()
                            print('folds')
                        # call
                        elif 33 < randomizer <= 75:
                            self.add_to_pot(player.pip(self.current_bet - player.ctp_this_round))
                            print(f'calls {self.current_bet}')
                        # raise
                        else:
                            # minimum raise size is current_bet + (current_bet - prev_bet)
                            # maximum raise is all-in
                            try:
                                raise_to = random.randint((self.current_bet + (self.current_bet - self.prev_bet)), (player.stack + player.ctp_this_round))
                            except:
                                raise_to = player.stack + player.ctp_this_round

                            self.add_to_pot(player.pip(raise_to - player.ctp_this_round))

                            # re-define current bet to previous bet
                            self.prev_bet = self.current_bet
                            self.current_bet = raise_to

                            print(f'raises to {raise_to}')
                            print(f'previous bet is now {self.prev_bet}')
                            print(f'current bet is now {self.current_bet}')

                        round += 1

                    self.update_live_players()
