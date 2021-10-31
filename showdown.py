def showdown():

    print("showdown() called")

    for player in live_players:

        # combine player hand with board to make a 7-card hand
        for card in board:
            player.hand.append(card)

        # divide into values/suits, sort 7-card hand
        player.hand_values = [card.value_ace_high for card in player.hand]
        player.hand_values_ace_low = [card.value_ace_low for card in player.hand]
        player.hand_suits = [card.suit for card in player.hand]
        player.hand_values.sort(reverse = True)
        player.hand_suits.sort()

        # check player hand for pairs, sets, quads to use throughout this function
        pairs = 0
        sets = 0
        quads = 0

        for card in set(player.hand_values):
            if player.hand_values.count(card) == 2:
                pairs += 1
            elif player.hand_values.count(card) == 3:
                sets += 1
            elif player.hand_values.count(card) == 4:
                quads += 1

        # player.hand_score atrribute - store hand strength as a variable and overwrite as needed
        # hand classification, player.hand_score, arrangement of player.hand_values

        # high card --> 1, sort high to low
        player.hand_score = 1
        # player.hand_values is already sorted high to low

        # pair --> 2, pair then high to low
        if pairs == 1 and sets == quads == 0:

            player.__str__()
            print('pair')
            for card in player.hand:
                print(card.__str__())
            print('\n')
            player.hand_score = 2

            # sort player.hand_values accordingly
            for i, value in enumerate(player.hand_values):
                if player.hand_values[i] == player.hand_values[i + 1]:
                    player.hand_values.insert(0, player.hand_values.pop(i))
                    player.hand_values.insert(0, player.hand_values.pop(i + 1))
                    break

        # 2 pair --> 3, higher pair, lower pair, kicker
        if pairs > 1 and sets == quads == 0:

            player.__str__()
            print('2 pair')
            for card in player.hand:
                print(card.__str__())
            print('\n')
            player.hand_score = 3

            # sort in ascending order
            player.hand_values.sort()

            # sort player.hand_values accordingly
            for i in [0,1,2,3,4,5]:
                if player.hand_values[i] == player.hand_values[i + 1]:
                    player.hand_values.insert(0, player.hand_values.pop(i))
                    player.hand_values.insert(0, player.hand_values.pop(i + 1))

            two_pair = player.hand_values[:4]  # higher pair will be first
            kickers = player.hand_values[4:]  # sort to place higher kicker
            kickers.sort(reverse = True)

            player.hand_values = two_pair + kickers  # higher pair, lower pair, kickers in order of rank

        # set --> 4, set then high to low
        if sets == 1 and pairs == quads == 0:

            player.__str__()
            print('set')
            for card in player.hand:
                print(card.__str__())
            print('\n')
            player.hand_score = 4

            for i in [0,1,2,3,4]:

                if player.hand_values[i] == player.hand_values[i + 1] == player.hand_values[i + 2]:
                    player.hand_values.insert(0, player.hand_values.pop(i))
                    player.hand_values.insert(0, player.hand_values.pop(i + 1))
                    player.hand_values.insert(0, player.hand_values.pop(i + 2))
                break

        # straight --> 5, straight in order high to low (run for ace low then ace high)
        if len(set(player.hand_values)) > 4:

            if 14 in player.hand_values:  # if hand includes an ace, check for wheel straight

                temp_hand = list(set(player.hand_values_ace_low))
                temp_hand.sort()

                if temp_hand[0] == temp_hand[1] - 1 == temp_hand[2] - 2 == temp_hand[3] - 3 == temp_hand[4] - 4:

                    player.__str__()
                    print('straight')
                    for card in player.hand:
                        print(card.__str__())
                    print('\n')
                    player.hand_score = 5

                    # reset player.hand_values for 5-high straight

                    straight_cards = [5,4,3,2,1]
                    non_straight_cards = []

                    for card in set(player.hand_values_ace_low):
                        if player.hand_values_ace_low.count(card) == 3:  # if set + straight
                            non_straight_cards.append(card)
                            non_straight_cards.append(card)
                            break
                        elif player.hand_values_ace_low.count(card) == 2:  # if pair or 2 pair + straight
                            non_straight_cards.append(card)
                        elif card not in straight_cards:  # if card is not part of wheel straight
                            non_straight_cards.append(card)

            # reset temp_hand for non-wheel straight
            temp_hand = list(set(player.hand_values))
            temp_hand.sort(reverse = True)

            for i,card in enumerate(range(0, len(temp_hand) - 4)):  # check for non-wheel straight

                if temp_hand[i] == temp_hand[i + 1] + 1 == temp_hand[i + 2] + 2 == temp_hand[i + 3] + 3 == temp_hand[i + 4] + 4:

                    player.__str__()
                    print('straight')
                    for card in player.hand:
                        print(card.__str__())
                    print('\n')
                    player.hand_score = 5

                    # reset player.hand_values for straight
                    # overwrites from wheel straight if hand contains wheel-6-7 straight
                    straight_cards = []

                    straight_cards.append(temp_hand[i])
                    straight_cards.append(temp_hand[i + 1])
                    straight_cards.append(temp_hand[i + 2])
                    straight_cards.append(temp_hand[i + 3])
                    straight_cards.append(temp_hand[i + 4])

                    non_straight_cards = []

                    for card in set(player.hand_values):
                        if player.hand_values.count(card) == 3:  # if set + straight
                            non_straight_cards.append(card)
                            non_straight_cards.append(card)
                            break
                        elif player.hand_values.count(card) == 2:  # if pair or 2 pair + straight
                            non_straight_cards.append(card)
                        elif card not in straight_cards:  # if card is not part of wheel straight
                            non_straight_cards.append(card)

                    # to prevent running for loop another iteration if highest straight already found
                    break

            if player.hand_score == 5:  # if straight, overwrite player.hand_values
                non_straight_cards.sort(reverse = True)
                player.hand_values = straight_cards + non_straight_cards

        # flush --> 6, high to low
        for suit in ['c','s','h','d']:

            if player.hand_suits.count(suit) > 4:

                player.__str__()
                print('flush')
                for card in player.hand:
                    print(card.__str__())
                print('\n')
                player.hand_score = 6

                player.hand_values.sort(reverse = True)

                # re-define player.hand_values
                flush_cards = [card.value_ace_high for card in player.hand if card.suit == suit]
                flush_cards.sort(reverse = True)
                flush_cards_ace_low = [card.value_ace_low for card in player.hand if card.suit == suit]
                flush_cards_ace_low.sort()  # to check for straight flush
                nonflush_cards = [card.value_ace_high for card in player.hand if card.suit != suit]
                nonflush_cards.sort(reverse = True)

                player.hand_values = flush_cards + nonflush_cards

        # boat --> 7, 3 of kind then 2 of kind

        if (sets == 1 and pairs > 0) or (sets > 1):

            player.__str__()
            print('boat')
            for card in player.hand:
                print(card.__str__())
            print('\n')
            player.hand_score = 7

            player.hand_values.sort()  # sort in ascending order

            if sets > 1:  # 2 sets
                for i in [0,1,2,3,4]:
                    if player.hand_values[i] == player.hand_values[i + 1] == player.hand_values[i + 2]:
                        player.hand_values.insert(0, player.hand_values.pop(i))
                        player.hand_values.insert(0, player.hand_values.pop(i + 1))
                        player.hand_values.insert(0, player.hand_values.pop(i + 2))

            else:  # 1 set + 1-2 pair
                for i in [0,1,2,3,4]:
                    if player.hand_values[i] == player.hand_values[i + 1] == player.hand_values[i + 2]:
                        player.hand_values.insert(0, player.hand_values.pop(i))
                        player.hand_values.insert(0, player.hand_values.pop(i + 1))
                        player.hand_values.insert(0, player.hand_values.pop(i + 2))
                        break

                three_same = player.hand_values[:3]
                two_same = player.hand_values[3:]

                for i in [0,1,2,3]:
                    if player.hand_values[i] == player.hand_values[i + 1]:
                        player.hand_values.insert(0, player.hand_values.pop(i))
                        player.hand_values.insert(0, player.hand_values.pop(i + 1))

                player.hand_values = three_same + two_same

        # quads --> 8, 4 of kind then kicker
        if quads == 1:

            player.__str__()
            print('quads')
            for card in player.hand:
                print(card.__str__())
            print('\n')
            player.hand_score = 8

            for i in [0,1,2,3]:
                if player.hand_values[i] == player.hand_values[i + 1] == player.hand_values[i + 2] == player.hand_values[i + 3]:
                    player.hand_values.insert(0, player.hand_values.pop(i))
                    player.hand_values.insert(0, player.hand_values.pop(i + 1))
                    player.hand_values.insert(0, player.hand_values.pop(i + 2))
                    player.hand_values.insert(0, player.hand_values.pop(i + 3))

        # straight flush --> 9, straight in order high to low (run for ace low then ace high)

        if player.hand_score == 6:  # if flush, check for straight flush

            if 14 in player.hand_values:  # if hand includes an ace, check for wheel straight flush

                if flush_cards_ace_low[0] == flush_cards_ace_low[1] - 1 == flush_cards_ace_low[2] - 2 == flush_cards_ace_low[3] - 3 == flush_cards_ace_low[4] - 4:

                    player.__str__()
                    print('straight flush')
                    for card in player.hand:
                        print(card.__str__())
                    print('\n')
                    player.hand_score = 9

                    # reset player.hand_values for 5-high straight flush

                    straight_cards = [5,4,3,2,1]
                    non_straight_cards = []

                    for card in set(player.hand_values_ace_low):
                        if player.hand_values_ace_low.count(card) == 3:  # if set + straight
                            non_straight_cards.append(card)
                            non_straight_cards.append(card)
                            break
                        elif player.hand_values_ace_low.count(card) == 2:  # if pair or 2 pair + straight
                            non_straight_cards.append(card)
                        elif card not in straight_cards:  # if card is not part of wheel straight
                            non_straight_cards.append(card)

            # check for non-wheel straight flush

            for i,card in enumerate(range(0, len(flush_cards) - 4)):  # check for non-wheel straight flush

                if flush_cards[i] == flush_cards[i + 1] + 1 == flush_cards[i + 2] + 2 == flush_cards[i + 3] + 3 == flush_cards[i + 4] + 4:

                    player.__str__()
                    print('straight flush')
                    for card in player.hand:
                        print(card.__str__())
                    print('\n')
                    player.hand_score = 9

                    # reset player.hand_values for straight
                    # overwrites from wheel straight if hand contains wheel-6-7 straight
                    straight_cards = []

                    straight_cards.append(flush_cards[i])
                    straight_cards.append(flush_cards[i + 1])
                    straight_cards.append(flush_cards[i + 2])
                    straight_cards.append(flush_cards[i + 3])
                    straight_cards.append(flush_cards[i + 4])

                    non_straight_cards = []

                    for card in set(player.hand_values):
                        if player.hand_values.count(card) == 3:  # if set + straight
                            non_straight_cards.append(card)
                            non_straight_cards.append(card)
                            break
                        elif player.hand_values.count(card) == 2:  # if pair or 2 pair + straight
                            non_straight_cards.append(card)
                        elif card not in straight_cards:  # if card is not part of wheel straight
                            non_straight_cards.append(card)

                    # to prevent running for loop another iteration if highest straight already found
                    break

            if player.hand_score == 9:  # if straight flush, overwrite player.hand_values
                non_straight_cards.sort(reverse = True)
                player.hand_values = straight_cards + non_straight_cards
