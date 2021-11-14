

# print("enter a number")
# input = input()
#
#
# print("input = " + input)
#
# input = int(input)
#
#
# print("type of input: " + str(type(input)))


while True:
    print("Enter a valid bet size as an integer:")
    try:
        bet = input()
        bet = int(bet)
        if bet > 2 and bet < 150:
            break
        else:
            continue
    except:
        continue

print("bet placed: " + str(bet))
