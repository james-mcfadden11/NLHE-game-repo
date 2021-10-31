def betting():

    print("betting() called")

    counter = 0

    global live_players
    global live_players_ctp_this_round
    global current_bet
    global prev_bet
    global live_players_ctp
    global pot

    if live_players[0].ctp < 200 and len(live_players) > 1:
    # run betting sequence if not all-in and more than one player live

        while len(live_players) > 1 and len(set(live_players_ctp_this_round)) != 1 or counter == 0:

            print(f'counter is {counter}')

            for player in live_players:  # for loop for each player's action

                if len(live_players) == 1 or (len(set(live_players_ctp_this_round)) == 1 and counter > 0):
                    # break if all fold except one player or if all players ctp same amount after first round
                    break

                player.__str__()

                randomizer = random.randint(1, 100)  # to make decisions on test version
                #print(f'randomizer is {randomizer}')

                if (current_bet - player.ctp_this_round) == 0:  # if player is not facing a bet: check or bet

                    if randomizer < 50:  # check 50% of time
                        player.pip(0)
                        print('checks')

                    else:
                        bet = random.randint((2 + player.ctp_this_round), player.stack)  # valid bet is > 2 and less than player stack
                        # special case: BB facing all limps must raise to at least 2 BB's if raising
                        player.pip(bet)
                        prev_bet = current_bet
                        current_bet = bet
                        print(f'bets {bet}')
                        print(f'previous bet is now {prev_bet}')
                        print(f'current bet is now {current_bet}')

                elif current_bet >= (player.stack + player.ctp_this_round):  # if players is facing an all-in bet: call or fold

                    if randomizer > 50:  # fold
                        player.fold()
                        print('folds')

                    else:  # call
                        player.pip(current_bet - player.ctp_this_round)
                        print(f'calls {current_bet}')

                else:  # if player is facing a bet which is not all-in: fold, call, raise

                    if randomizer > 75:  # fold
                        player.fold()
                        print('folds')

                    elif 33 < randomizer <= 75:  # call
                        player.pip(current_bet - player.ctp_this_round)
                        print(f'calls {current_bet}')

                    else:  # raise
                        # minimum raise size is current_bet + (current_bet - prev_bet)
                        # maximum raise is all-in

                        try:
                            raize = random.randint((current_bet + (current_bet - prev_bet)), (player.stack + player.ctp_this_round))
                        except:
                            raize = player.stack + player.ctp_this_round

                        player.pip(raize - player.ctp_this_round)

                        prev_bet = current_bet  # re-define current bet to previous bet
                        current_bet = raize

                        print(f'raises to {raize}')
                        print(f'previous bet is now {prev_bet}')
                        print(f'current bet is now {current_bet}')

                # re-define parameters
                live_players = [x for x in live_players if x.is_live == True]
                live_players_ctp = [x.ctp for x in live_players]
                live_players_ctp_this_round = [x.ctp_this_round for x in live_players]
                pot = p1.ctp + p2.ctp + p3.ctp + p4.ctp + p5.ctp + p6.ctp

            counter += 1

            if counter > 30:
                break

            print('----------------------------------------------------------------------')

    print(f'pot is {pot}')
    print(f'there are {len(live_players)} live players')
    print(f'live players ctp are {live_players_ctp}')
    print(f'live players ctp this round are {live_players_ctp_this_round}')
