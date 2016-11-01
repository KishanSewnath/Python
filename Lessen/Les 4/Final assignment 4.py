annulering1 = []
stations1 = []

treinritten = open('C:/Users/Kishan Sewnath/Desktop/treinritten.txt', 'r')
treinrittenList = treinritten.readlines()
treinritten.close()

annuleringen = open('C:/Users/Kishan Sewnath/Desktop/annuleringen.txt', 'r')
annuleringlijst = annuleringen.readlines()
annuleringen.close()

for station in annuleringlijst:
    rittenList = station.rstrip().split(':')
    annulering1.append(rittenList[1])

for treinStations in treinrittenList:
    stations2 = treinStations.rstrip().split('-')
    if stations2[1] not in annulering1:
        stations1.append(treinStations)

eind = open('C:/Users/Kishan Sewnath/Desktop/treinritten_nieuw.txt', 'w')
eind.writelines(stations1)
eind.close()

