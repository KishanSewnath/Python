import csv
import random


def nieuwe_kluis():
    with open('codes.csv', 'a', newline='')as kluizen:
        writer = csv.writer(kluizen, delimiter=';')
        code = random.randint(1000, 9999)
        beschikbaar = aantal_kluizen_vrij()
        if beschikbaar != 0:
            writer.writerow([beschikbaar, code])
            print('Uw kluisnummer is: {} met code {}.\n'. format(beschikbaar, code))
        else:
            print('Er zijn geen kluizen beschikbaar.\n')


def kluis_openen():
    with open('codes.csv', 'r', newline='') as kluizen:
        reader = csv.reader(kluizen, delimiter=';')
        print('Voer uw code in:')
        code = str(input())
        for row in reader:
            if row[1] == code:
                print('Kluisnummer {} is open.\n'.format(row[0]))


def kluis_teruggeven():
    print("Kluis teruggegeven\n")


def aantal_kluizen_vrij():
    with open('codes.csv', 'r', newline='') as kluizen:
        reader = csv.reader(kluizen, delimiter=';')
        gebruikt = []
        for row in reader:
            gebruikt.append(int(row[0]))
        aantal = len(gebruikt)
        return 12 - aantal


while True:
    print('1: Ik wil een nieuwe kluis')
    print('2: Ik wil mijn kluis openen')
    print('3: Ik geef mijn kluis terug')
    print('4: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('5: Ik wil stoppen')
    print('Maak een keuze')
    keuze = eval(input())
    if keuze == 1:
        nieuwe_kluis()
    elif keuze == 2:
        kluis_openen()
    elif keuze == 3:
        kluis_teruggeven()
    elif keuze == 4:
        aantal_kluizen_vrij()
        print('Er zijn nog {} kluisjes vrij.\n'.format(aantal_kluizen_vrij()))
    elif keuze == 5:
        print('Bedank voor het gebruiken van onze kluizen service!')
        break
