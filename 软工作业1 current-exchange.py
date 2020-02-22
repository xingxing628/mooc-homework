"""write your code in method currency_exchange"""
def currency_exchange():
    euro = float(input('How many eruos are you exchanging?'))
    rate = float(input('What is the exchange rate?'))

    dollar = euro * rate/100

    print('{0} {1} {2} {3} {4:.2f} {5}'.format(euro,'euros at an exchange rate of',rate,'is',dollar,'U.S. dollars.'))

    return dollar




