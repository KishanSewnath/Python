stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam', 'Sloterdijk', 'Amsterdam Centraal',
'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginpunt():
    while True:
        print("Wat is je beginstation?")
        begin = input()
        if begin in stations:
            print("Beginstation is: %s" %(begin))
            return begin
        else:
            print("Deze trein komt niet in %s" %(begin))

def inlezen_eindpunt(begin):
    while True:
        print("Wat is je eindstation?")
        eind =input()
        if eind in stations and stations.index(begin) < stations.index(eind):
            print("Eindstation is: %s" %(eind))
            return eind
        else:
            print("Deze trein komt niet in %s" %(eind))

def omroepen_reis(begin, eind):
    beginIndex = stations.index(begin) +1
    eindIndex = stations.index(eind) +1
    afstandStation = eindIndex- beginIndex
    prijs = afstandStation * 5
    print("Het beginstation %s is het %se station in het traject\nHet eindstation %s is het %se station in het traject" %(begin, beginIndex, eind, eindIndex))
    print("De afstand bedraagt %s station(s)\nDe prijs van het kaartje is %s euro.\nJij stapt in de trein in: %s" %(afstandStation, prijs, begin))
    haltes = range(beginIndex, eindIndex -1)
    for i in haltes:
        print('  -' + stations[i])
    print("Jij stapt uit in: %s" %(eind))

begin = inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
omroepen_reis(begin, eind)
