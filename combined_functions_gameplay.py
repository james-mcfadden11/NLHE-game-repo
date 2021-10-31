import random

def setup():

    print("setup() called")

    # define global variables for access in all functions
    global live_players
    global live_players_ctp_this_round
    global current_bet
    global prev_bet
    global live_players_ctp
    global pot
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global board
    global deck

    suits = ['h','d','c','s']
    ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    ranks_ace_high = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    ranks_ace_low = {'A':1,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

    # create object class Card with attributes rank, suit
    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value_ace_high = ranks_ace_high[rank]
            self.value_ace_low = ranks_ace_low[rank]
        def __str__(self):
            return self.rank + self.suit

    # create object class Deck
    class Deck:
        def __init__(self):
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))  # adds cards to the deck one by one
        def __str__(self):
            deck_comp = ''
            for card in self.deck:
                deck_comp += card.__str__() + ' '
                # card here is still an instance of the Card class, so need to call the .__str__ to get a string of a single card
            return deck_comp
        def shuffle(self):
            random.shuffle(self.deck)
        def deal(self):
            single_card = self.deck.pop()
            return single_card
            # returns a card from the deck (bottom of the deck) as variable single_card

    #instantiate a deck and shuffle
    deck = Deck()
    deck.shuffle()

    # create object class Player
    class Player:

        def __init__(self, name, ctp = 0, is_live = True, stack = 200, ctp_this_round = 0):
            self.name = name
            self.is_live = is_live  # Boolean
            self.hand = [deck.deal(), deck.deal()]  # composed of 2 card objects supplied by deck.deal()
            self.stack = stack  # integer, default 100
            self.ctp = ctp  # integer, contributed to pot
            self.ctp_this_round = ctp_this_round  # to reset each betting round to 0
            self.hand_values = [card.value_ace_high for card in self.hand]
            self.hand_suits = [card.suit for card in self.hand]

        def __str__(self):
            return print(self.name)
            # return f"{self.name}'s hand is {self.hand[0]} {self.hand[1]} and stack is {self.stack}"

        # pip = put in pot
        # ctp = contributed to pot
        def pip(self, amount):
            self.amount = amount
            self.ctp = self.ctp + self.amount
            self.stack = self.stack - self.amount
            self.ctp_this_round = self.ctp_this_round + self.amount

        def fold(self):
            self.is_live = False
            # remove folded players from live_players is done in each betting round loop


    # instantiate players, deal cards
    p1 = Player('p1')  # small blind
    p2 = Player('p2')  # big blind
    p3 = Player('p3')  # UTG
    p4 = Player('p4')  # MP
    p5 = Player('p5')  # CO
    p6 = Player('p6')  # button

    live_players = [p3, p4, p5, p6, p1, p2]

    # post blinds
    p1.pip(1)
    p2.pip(2)

    current_bet = 2
    prev_bet = 0

    live_players_ctp = [x.ctp for x in live_players]
    live_players_ctp_this_round = [x.ctp_this_round for x in live_players]

    pot = p1.ctp + p2.ctp + p3.ctp + p4.ctp + p5.ctp + p6.ctp

    board = []


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


def reorder_for_flop():

    print("reorder_for_flop() called")

    if p2.is_live:
        live_players.insert(0, live_players.pop())
    if p1.is_live:
        live_players.insert(0, live_players.pop())


def reset():

    print("reset() called")

    # reset player ctp this round
    for player in live_players:
        player.ctp_this_round = 0

    # resert current bet and prev bet
    current_bet = 0
    prev_bet = 0


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





################################
# GAMEPLAY
################################

print("Starting game!")

setup()

betting()

reorder_for_flop()
reset()
board.append(deck.deal())
board.append(deck.deal())
board.append(deck.deal())
betting()

reset()
board.append(deck.deal())
betting()

reset()
board.append(deck.deal())
betting()

showdown()

results()
