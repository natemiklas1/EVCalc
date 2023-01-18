import pywebio
from pywebio.input import input, input_group, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table
from maths import calcEv


def main():
    data = input_group('info', [
        input('odds (-110)', name='odds'),
        input('wager in $ (50)', name='wager'),
        input('Hit rate in percent (75)', name='hitrate'),
    ])

    odds = data['odds']
    wager = float(data['wager'])
    hitrate = float(data['hitrate'])

    ev = calcEv(hitrate, odds, wager)

    evPercent = ev / wager
    evPercentString = 'EV: %{}'.format(round(evPercent, 2))
    evString = 'EV: ${}'.format(round(ev, 2))
    print(evString)
    print(evPercentString)

    put_markdown('# **RESULTS**')
    put_text(evPercentString)
    put_text(evString)


if __name__ == '__main__':
    pywebio.start_server(main, port=80, debug=True)
