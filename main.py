import sys

import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table


def calcEv():
    odds = input("ODDS: ")
    wager = input("WAGER: ", type=FLOAT)
    hitRate = input("HITRATE (%): ", type=FLOAT)

    hitRate = hitRate / 100.0

    if odds[0:1] not in ('+', '-'):
        print('TRASH!')
        sys.exit()

    positive = False
    if odds[0:1] == '+':
        positive = True

    winnings = 0
    ratio = int(odds[1:])
    if positive:
        winnings = (ratio / 100.0) * wager
    else:
        winnings = (100.0 / ratio) * wager

    part1 = winnings * hitRate
    part2 = wager * (1.0 - hitRate)
    ev = part1 - part2

    evPercent = ev / wager
    print('EV: ${}'.format(round(ev, 2)))
    print('EV: %{}'.format(round(evPercent, 2)))


    put_markdown('# **RESULTS**')
    put_text('EV: %{}'.format(evPercent))


if __name__ == '__main__':
    pywebio.start_server(calcEv, port=80)
