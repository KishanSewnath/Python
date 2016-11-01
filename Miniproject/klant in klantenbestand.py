import csv
import requests
import xmltodict


def invoer_gegevens():
    with open('bezoekers.csv', 'a', newline='')as bezoekers:
        writer = csv.writer(bezoekers, delimiter=';')
        naam = input('Geef naam: ')
        email = input('Geef emailadres: ')
        writer.writerow([naam, email])


def filmkeuze():
    api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=uw7tbns0awlo3ovvngkv55j4ofjq9u8m&dag=01-11-2016&sorteer=1'

    response = requests.get(api_url)

    filmsXML = xmltodict.parse(response.text)

    for film in filmsXML['filmsoptv']['film']:
        titel = film['titel']
        starttijd = film['starttijd']



