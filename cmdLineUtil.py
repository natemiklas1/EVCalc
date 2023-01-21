import argparse
from maths import calcEv

parser = argparse.ArgumentParser()
parser.add_argument("-wager", help="", type=str)
parser.add_argument("-odds", help="", type=str, required=True)
parser.add_argument("-hitrate", help="in %", type=str, required=True)

args, leftovers = parser.parse_known_args()

ev, evPercent = calcEv(args.hitrate, args.odds, args.wager)

print('EV: ${}'.format(round(ev, 2)))
print('EV: {}%'.format(round(evPercent * 100, 2)))
# print('Total Returns: {}'.format(round(returns,2)))
