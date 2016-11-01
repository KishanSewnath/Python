import datetime
import csv

vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
t = vandaag.strftime('%H:%M:%S')
tijd = '{} at {}'.format(s, t)

bestand = 'inloggers.csv'

with open(bestand, 'a', newline='\n') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')

    while True:

        naam = input("Wat is je achternaam? ")

        if naam == 'einde':
            break

        voorl = input("Wat zijn je voorletters? ")

        gbdatum = input("Wat is je geboortedatum? ")

        email = input("Wat is je e-mail adres? ")

        writer.writerow((tijd, voorl, naam, gbdatum, email))
