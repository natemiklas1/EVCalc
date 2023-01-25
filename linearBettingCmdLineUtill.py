import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-odds", help="", type=str, required=True)
parser.add_argument("-bet", help="", type=str, required=True)
parser.add_argument("-purse", help="", type=str, required=True)

args, leftovers = parser.parse_known_args()

purse = float(args.purse)
betValue = float(args.bet)
odds = args.odds

positive = False
ratio = int(odds[1:])
if odds[0:1] == '+':
    positive = False
if positive:
    oddsRatio = ratio / 100.0
else:
    oddsRatio = 100.0 / ratio

oddsRatio = round(oddsRatio, 4)

winnings = betValue * oddsRatio

print('ODDS: {} ({})'.format(odds, oddsRatio))
print('BET: {}'.format(betValue))
print('PURSE: {}'.format(purse))
print('WINNINGS: {}'.format(round(winnings, 2)))


class BetInstance:
    def __init__(self, oddsRatio, initialBet, betList, goal, firstBet=False):
        self.oddsRatio = oddsRatio
        self.initialBet = initialBet
        self.firstBet = firstBet

        if self.firstBet:
            self.totalSpent = initialBet
            self.needToEarn = initialBet * oddsRatio
            self.newBet = initialBet
        else:
            lastBet = betList[len(betList) - 1]
            self.needToEarn = lastBet.totalSpent + goal
            self.newBet = self.needToEarn / oddsRatio
            self.totalSpent = lastBet.totalSpent + self.newBet


spent = 0.0
betList = []
while spent < purse:
    if len(betList) == 0:
        betInstance = BetInstance(oddsRatio, betValue, betList, winnings, firstBet=True)
        spent = betInstance.totalSpent
        betList.append(betInstance)
    else:
        betInstance = BetInstance(oddsRatio, betValue, betList, winnings)
        betList.append(betInstance)
        spent = betInstance.totalSpent


print('\n------LIST OF BETS------')
for i in betList:
    print('Need to bet: ${}'.format(round(i.newBet, 2)))