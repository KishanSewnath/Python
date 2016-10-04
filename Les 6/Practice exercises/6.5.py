import random

def monoplyworp():

    aantal_dubbel = 0

    eindeRonde = True
    while eindeRonde:

        eersteWorp = random.randrange(1, 7)

        tweedeWorp = random.randrange(1, 7)

        totaal = eersteWorp + tweedeWorp

        if eersteWorp != tweedeWorp:
            print('{} + {} = {}'.format(eersteWorp, tweedeWorp, totaal))
            eindeRonde = False

        elif eersteWorp == tweedeWorp:
            aantal_dubbel += 1
            print('{} + {} = {} (dubbel)'.format(eersteWorp, tweedeWorp, totaal))

            if aantal_dubbel == 3:
                print('{} + {} = (direct naar gevangenis)'. format(eersteWorp, tweedeWorp, totaal))
                eindeRonde = False


monoplyworp()
