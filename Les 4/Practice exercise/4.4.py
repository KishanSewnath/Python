import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y,")

infile = open('C:/Users/Kishan Sewnath/Desktop/hardlopers.txt', 'a')
naam = input('Wat is de naam van de hardloper: ')
tijd = vandaag.strftime('%H:%M:%S, ')
infile.write(s+' '+tijd +naam+'\n')

infile.close()

infile = open('C:/Users/Kishan Sewnath/Desktop/hardlopers.txt', 'r')
print(infile.read())
