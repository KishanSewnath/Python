infile = open('C:/Users/Kishan Sewnath/Desktop/kaartnummers.txt', 'r')
for line in infile:
    nummer = (line[:6])
    naam = (line[7:].strip())
    zin = '{} heeft kaartnummer: {}'
    zinnetje = (zin.format(naam, nummer))
    print(zinnetje)
