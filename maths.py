import sys


def calcEv(hitrate, odds, wager=10):
    try:
        bet = int(wager)
    except ValueError:
        print('TRASH!')
        sys.exit()

    if odds[0:1] not in ('+', '-'):
        print('TRASH!')
        sys.exit()

    positive = False
    if odds[0:1] == '+':
        positive = True

    winnings = 0
    ratio = int(odds[1:])
    if positive:
        winnings = (ratio / 100.0) * bet
    else:
        winnings = (100.0 / ratio) * bet

    # ev = (winnings * hitRate) + ((bet * 100.0) - hitRate)
    part1 = winnings * hitrate
    part2 = bet * (1.0 - hitrate)
    ev = part1 - part2

    return ev
