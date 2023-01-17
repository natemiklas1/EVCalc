import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-bet", help="", type=str, required=True)
parser.add_argument("-odds", help="", type=str, required=True)
parser.add_argument("-hitRate", help="in %", type=str, required=True)

args, leftovers = parser.parse_known_args()

hitRate = (int(args.hitRate) / 100.0)
bet = args.bet

print('HitRate: {}%'.format(args.hitRate))

try:
    bet = int(bet)
except:
    print('TRASH!')
    sys.exit()
print('Bet: ${}'.format(bet))

if args.odds[0:1] not in ('+', '-'):
    print('TRASH!')
    sys.exit()
print('Odds: {}'.format(args.odds))

positive = False
if args.odds[0:1] == '+':
    positive = True

winnings = 0
ratio = int(args.odds[1:])
if positive:
    winnings = (ratio / 100.0) * bet
else:
    winnings = (100.0 / ratio) * bet

print('Winnings: ${}'.format(round(winnings, 2)))

# ev = (winnings * hitRate) + ((bet * 100.0) - hitRate)
part1 = winnings * hitRate
part2 = bet * (1.0 - hitRate)
ev = part1 - part2

print('EV: ${}'.format(round(ev, 2)))
# print('Total Returns: {}'.format(round(returns,2)))
