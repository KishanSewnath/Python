#n is een getal
#nummers tussen 2 en n, deelbaar door 2 of 3

def even(n):
    for x in range(2, n):
        if x%2 == 0 or x%3 == 0:
            print(x, end=', ')
        else:
            print('Not', end=', ')
even(17)
