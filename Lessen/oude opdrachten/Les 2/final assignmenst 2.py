lst = ['aap', 'noot', 'mies', 'blaa', 'fooo', 'bar', 'bnb']

beginIndex = 3
eindIndex = 6

totaal = 0
for indexWoord in range(beginIndex, eindIndex + 1):
    lengteWoord = len(woord)
    woord = lst[indexWoord ]
    totaal = totaal + lengteWoord
    print(woord)

print(totaal)
