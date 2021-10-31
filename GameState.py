from Player import Player
from Deck import Deck
from Card import Card

class GameState:
    def __init__(self, live_players):
        self.pot = 0
        self.board = []
        self.live_players = live_players
        self.live_players_ctp = [0, 0, 0, 0, 0, 0]
        self.live_players_ctp_this_round = [0, 0, 0, 0, 0, 0]
        self.current_bet = 2
        self.prev_bet = 0

# OK to use getters and setters...

    def set_live_players(self):
        self.live_players = []

    def set_live_players_ctp(self):
        self.live_players_ctp = [player.ctp for player in self.live_players]

    def set_live_players_ctp_this_round(self):
        self.set_live_players_ctp_this_round = [player.ctp_this_round for player in self.live_players]

    def add_to_pot(self, amount):
        self.pot += amount

    def add_card_to_board(self, card):
        self.board.append(card)

    def reset_ctp_and_bet(self):
        for player in self.live_players:
            player.ctp_this_round = 0
        self.current_bet = 0
        self.prev_bet = 0

    def reorder_for_flop(self):
        if self.live_players[5].is_live:
            self.live_players.insert(0, self.live_players.pop())
        if self.live_players[4].is_live:
            self.live_players.insert(0, self.live_players.pop())
