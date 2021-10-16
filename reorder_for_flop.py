def reorder_for_flop():
    if p2.is_live:
        live_players.insert(0, live_players.pop())
    if p1.is_live:
        live_players.insert(0, live_players.pop())
