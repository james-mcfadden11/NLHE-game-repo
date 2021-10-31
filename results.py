def results():

    print("results() called")

    hand_scores = [player.hand_score for player in live_players]

    if hand_scores.count(max(hand_scores)) == 1:
        for player in live_players:
            if player.hand_score == max(hand_scores):
                winner = player
                player.__str__()
                print(f'wins pot {pot}')

    else:  # if 2 or more players have highest hand_score

        # list of player.hand_values for players with highest hand_score
        hands_to_check = [player.hand_values[:5] for player in live_players if player.hand_score == max(hand_scores)]
        hands_to_check.sort(reverse = True)

        # list of hands that are equal to best hand
        winning_hand = [hand for hand in hands_to_check if hand == hands_to_check[0]]

        # if only one hand matches best hand
        if len(winning_hand) == 1:

            for player in live_players:
                if player.hand_values[:5] == winning_hand[0]:
                    player.__str__()
                    print(f'wins pot {pot}')

        # if 2 or more hands are equal to the best hand, chopped pot
        else:
            # list of players who chop the pot
            winners = [player for player in live_players if player.hand_values[:5] == hands_to_check[0]]
            chop = pot/len(winners)

            print(f'split pot, {len(winners)} players win {chop} each')
