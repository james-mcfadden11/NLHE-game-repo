def reorder_for_flop():

    print("reorder_for_flop() called")

    if p2.is_live:
        live_players.insert(0, live_players.pop())
    if p1.is_live:
        live_players.insert(0, live_players.pop())
