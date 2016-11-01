lst = []
while True:
    print("Geef een getal op")
    getal = int(input())
    if getal != 0:
        lst.append(getal)
        som = sum(lst)
        lengte = len(lst)
    else:
        print("Er zijn {} getallen ingevoerd, de som is: {}" .format(lengte +1,som))
        break
