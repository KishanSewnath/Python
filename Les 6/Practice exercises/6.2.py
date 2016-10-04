import csv

with open('tickerbestand', 'r') as ticker:
    reader = csv.reader(ticker, delimiter=':')

    bedrijf = input("Enter Company name: ")
    for (key,value) in reader:
        if (key) == bedrijf:
            print('Ticker symbol: {}' .format(value))
            break
    symbol = input("Enter Ticker symbol: ")
    for (key,value) in reader:
        if (value) == symbol:
            print('Company name: {}' .format(key))
