grondgetallen =  [4, 6, 3, -81]

def kwadraten_som(grondgetallen):

    for getal in grondgetallen:
        if getal < 0:
            grondgetallen.remove(getal)

    res = 0
    for cijfer in grondgetallen:
        res = cijfer**2 + res
    return res


print(kwadraten_som(grondgetallen))
