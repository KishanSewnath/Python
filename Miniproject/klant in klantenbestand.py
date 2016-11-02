import csv
import random

def invoer_gegevens():
    with open('bezoekers.csv', 'a', newline='')as bezoekers:

        writer = csv.writer(bezoekers, delimiter=';')
        naam = input('Geef naam: ')
        email = input('Geef emailadres: ')


        randomnummer1 = random.randrange(10)
        randomnummer2 = random.randrange(10)
        randomnummer3 = random.randrange(10)
        randomnummer4 = random.randrange(10)
        helecode = ('{}{}{}{}'.format(randomnummer1, randomnummer2, randomnummer3, randomnummer4))
        unieke_code = ('Uw unieke code is: {}'.format(helecode))
        #return haalt none weg, maar print alleen het eerste
        print(unieke_code)
        writer.writerow([naam, email, helecode])

def gegevens_ophalen():
    with open('bezoekers.csv', 'r', newline='')as bezoekers:
        reader = csv.dictreader(bezoekers, delimiter=';')
        for rij in reader:
            #return haalt none weg, maar print alleen het eerste
            print('Naam: {}\nEmailadres: {}\nUnieke code: {}'.format(rij[0], rij[1], rij[2]))




