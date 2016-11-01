stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

begin_station = input('Wat is het beginstation?: ')
if begin_station not in stations:
    print('Dit station is niet geldig, beginstation is %s' % (stations[0]))
    begin_station = stations[0]
    print('Het beginstation %s is het %se station in het traject.' % (begin_station, (stations.index(begin_station)+1)))
else:
    print('Het beginstation %s is het %se station in het traject.' % (begin_station, (stations.index(begin_station)+1)))

eind_station = input('Wat is het eindstation?: ')
if eind_station not in stations:
    print('Dit station is niet geldig, eindstation is %s' % (stations[-1]))
    eind_station = stations[-1]
    print('Het eindstation %s is het %se station in het traject.' % (eind_station, (stations.index(eind_station)+1)))
elif eind_station == begin_station:
    print('Dit station is niet geldig, eindstation is %s' % (stations[-1]))
    eind_station = stations[-1]
    print('Het eindstation %s is het %se station in het traject.' % (eind_station, (stations.index(eind_station)+1)))
else:
    print('Het eindstation %s is het %se station in het traject.' % (eind_station, (stations.index(eind_station)+1)))

eind = eind_station
begin = begin_station
haltes = stations.index(eind_station) - stations.index(begin_station)
haltes_tussen = stations[(stations.index(begin)+1):(stations.index(eind)-1)]

print('')
print('De afstand bedraagt %s station(s)' % (haltes))
print('De prijs van het kaartje is %s euro.' % (haltes*5.00))
print('')
print('Jij stapt in de trein in: %s' % (begin_station))
for halte in haltes_tussen:
    print ('\t- %s' % (halte))
print('Je stapt uit in : %s ' % (eind_station) )
