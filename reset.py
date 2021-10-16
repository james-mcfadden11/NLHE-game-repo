def reset():
    # reset player ctp this round
    for player in live_players:
        player.ctp_this_round = 0

    # resert current bet and prev bet
    current_bet = 0
    prev_bet = 0
