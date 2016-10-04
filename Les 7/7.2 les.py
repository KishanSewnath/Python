with open('namen.csv', 'a', newline='\n') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')

    while True:
        name = input('name? ')

        if name == '':
            break

        age = input('age? ')

        job = input('job? ')

        writer.writerow((name, age, job))
