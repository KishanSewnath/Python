import csv

with open('gamers.csv', 'r') as namen:
    gamers = csv.reader(namen, delimiter=';')

    maximaal = 0

    for naam in gamers:

        score = int(naam[2])
        if score > maximaal:
            maximaal = score
    print('De hoogste score is: {} op {} behaald door {}'.format(naam[2], naam[1], naam[0]))
