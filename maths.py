import sys


def _exit():
    print('TRASH!')
    sys.exit()


def calcEv(hitrate, odds, wager=None):
    if wager is None:
        wager = 2
    try:
        hitrate = float(hitrate) / 100
    except ValueError:
        _exit()
    try:
        wager = float(wager)
    except ValueError:
        _exit()

    if odds[0:1] not in ('+', '-'):
        _exit()

    positive = False
    if odds[0:1] == '+':
        positive = True

    ratio = int(odds[1:])
    if positive:
        winnings = (ratio / 100.0) * wager
    else:
        winnings = (100.0 / ratio) * wager

    # ev = (winnings * hitRate) + ((bet * 100.0) - hitRate)
    part1 = winnings * hitrate
    part2 = wager * (1.0 - hitrate)
    ev = part1 - part2

    evPercent = ev/wager

    return ev, evPercent
