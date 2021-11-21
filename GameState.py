from Player import Player

class GameState:
    def __init__(self, live_players):
        self.pot = 0
        self.board = []
        self.all_players = live_players
        self.live_players = live_players
        self.live_players_ctp = [0, 0, 0, 0, 0, 0]
        self.live_players_ctp_this_round = [0, 0, 0, 0, 0, 0]
        self.current_bet = 2
        self.prev_bet = 0

    def update_game_state(self, bets):
        self.live_players = [player for player in self.live_players if player.is_live == True]
        self.live_players_ctp = [player.ctp for player in self.live_players]
        self.live_players_ctp_this_round = [player.ctp_this_round for player in self.live_players]
        self.pot = sum([player.ctp for player in self.all_players])
        self.current_bet = bets[0]
        self.prev_bet = bets[1]

    def add_card_to_board(self, card):
        self.board.append(card)

    def reset_ctp_and_current_bet(self):
        for player in self.live_players:
            player.ctp_this_round = 0
        self.current_bet = 0
        self.prev_bet = 0

    def reorder_for_flop(self):
        if self.live_players[-1].name == 'p2':
            self.live_players.insert(0, self.live_players.pop())
        if self.live_players[-1].name == 'p1':
            self.live_players.insert(0, self.live_players.pop())

    def print_status(self):
        print("pot: " + str(self.pot))
        print("board: " + str([card.__str__() for card in self.board]))
        print("live players: " + str([player.__str__() for player in self.live_players]))
        print("---------------------------------")

    def betting(self, current_bet):
        round = 0
        self.current_bet = current_bet

        # run betting sequence if not all-in and more than one player live
        if self.live_players[0].ctp < 200 and len(self.live_players) > 1:

            while len(self.live_players) > 1 and len(set(self.live_players_ctp_this_round)) != 1 or round == 0:

                for player in self.live_players:
                    # break if all fold except one player or if all players ctp same amount after first round
                    if len(self.live_players) == 1 or (len(set(self.live_players_ctp_this_round)) == 1 and round > 0):
                        break

                    print(f'{player.__str__()} in position {player.position_poker}')

                    self.update_game_state(player.act(self.current_bet, self.prev_bet, self.live_players, self.pot))

                    print("---------------------------------")

                print("---------------------------------")

                round += 1
