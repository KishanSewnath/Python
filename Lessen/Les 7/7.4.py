import csv

with open('artikelen.csv', 'r') as artikelen:
    art = csv.reader(artikelen, delimiter=';')


    duurst = 'Het duurste artikel is {} en die kost {} Euro'.format(..., ...)
    kleinst = 'Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(..., ...)
    totaal = 'In totaal hebben wij {} producten in ons magazijn liggen'.format(...)
