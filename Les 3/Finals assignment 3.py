def standaardprijs(afstandKM):
    if afstandKM <= 0:
        prijs = 0
    elif afstandKM <= 50:
        prijs = 0.80*afstandKM
    else:
        prijs = (0.60*afstandKM)+15
    return prijs
def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd in range(12,65) and weekendrit is True:
        prijs*=0.6
    elif leeftijd not in range(12,65) and weekendrit is True:
        prijs*=0.65
    elif leeftijd in range(12, 65) and weekendrit is False:
        prijs
    else:
        leeftijd not in range (12,65) and weekendrit is False
        prijs*=0.7
    return prijs
print(ritprijs(11, True, 50))
print(ritprijs(11, True, 25))
print(ritprijs(11, True, 100))
print(ritprijs(11, False, -10))
print(ritprijs(11, False, 25))
print(ritprijs(11, False, 100))
print(ritprijs(12, True, -10))
print(ritprijs(12, True, 25))
print(ritprijs(12, True, 100))
print(ritprijs(12, False, -10))
print(ritprijs(12, False, 25))
print(ritprijs(12, False, 100))
print(ritprijs(64, True, -10))
print(ritprijs(64, True, 25))
print(ritprijs(64, True, 100))
print(ritprijs(64, False, -10))
print(ritprijs(64, False, 25))
print(ritprijs(64, False, 100))
print(ritprijs(65, True, -10))
print(ritprijs(65, True, 25))
print(ritprijs(65, True, 100))
print(ritprijs(65, False, -10))
print(ritprijs(65, False, 25))
print(ritprijs(65, False, 100))
