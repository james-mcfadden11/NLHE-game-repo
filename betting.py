
    round = 0

    if live_players[0].ctp < 200 and len(live_players) > 1:
    # run betting sequence if not all-in and more than one player live

        while len(live_players) > 1 and len(set(live_players_ctp_this_round)) != 1 or round == 0:

            for player in live_players:  # for loop for each player's action

                if len(live_players) == 1 or (len(set(live_players_ctp_this_round)) == 1 and round > 0):
                    # break if all fold except one player or if all players ctp same amount after first round
                    break

                player.__str__()

                # random number generator to make decisions on test version
                randomizer = random.randint(1, 100)
                #print(f'randomizer is {randomizer}')

                # if player is not facing a bet: check or bet
                if (current_bet - player.ctp_this_round) == 0:
                    # check 50% of time
                    if randomizer < 50:
                        player.pip(0)
                        print('checks')
                    # valid bet is > 2 and less than player stack
                    else:
                        bet = random.randint((2 + player.ctp_this_round), player.stack)
                        # special case: BB facing all limps must raise to at least 2 BB's if raising
                        player.pip(bet)
                        prev_bet = current_bet
                        current_bet = bet
                        print(f'bets {bet}')
                        print(f'previous bet is now {prev_bet}')
                        print(f'current bet is now {current_bet}')

                # if player is facing an all-in bet: call or fold
                elif current_bet >= (player.stack + player.ctp_this_round):
                    # fold
                    if randomizer > 50:
                        player.fold()
                        print('folds')
                    # call
                    else:
                        player.pip(current_bet - player.ctp_this_round)
                        print(f'calls {current_bet}')

                # if player is facing a bet which is not all-in: fold, call, raise
                else:
                    # fold
                    if randomizer > 75:
                        player.fold()
                        print('folds')
                    # call
                    elif 33 < randomizer <= 75:
                        player.pip(current_bet - player.ctp_this_round)
                        print(f'calls {current_bet}')
                    # raise
                    else:
                        # minimum raise size is current_bet + (current_bet - prev_bet)
                        # maximum raise is all-in
                        try:
                            raize = random.randint((current_bet + (current_bet - prev_bet)), (player.stack + player.ctp_this_round))
                        except:
                            raize = player.stack + player.ctp_this_round

                        player.pip(raize - player.ctp_this_round)

                        # re-define current bet to previous bet
                        prev_bet = current_bet
                        current_bet = raize

                        print(f'raises to {raize}')
                        print(f'previous bet is now {prev_bet}')
                        print(f'current bet is now {current_bet}')

                    round += 1

                # re-define parameters
                live_players = [x for x in live_players if x.is_live == True]
                live_players_ctp = [x.ctp for x in live_players]
                live_players_ctp_this_round = [x.ctp_this_round for x in live_players]
                pot = p1.ctp + p2.ctp + p3.ctp + p4.ctp + p5.ctp + p6.ctp
