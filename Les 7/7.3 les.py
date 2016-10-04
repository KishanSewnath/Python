import csv

with open('namen.csv', 'r') as namen:
    reader = csv.reader(namen, delimiter=';')

    for row in reader:
        print(row)
        print('{} heeft als beroep : {}'.format(row[0], row[1]))
