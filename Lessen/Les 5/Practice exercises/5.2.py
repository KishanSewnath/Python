lijst4letter = []

lijstinvoer = eval(input('Geef een lijst met minimaal 10 strings: '))
print('De nieuw-gemaakte lijst met alle vier-letter strings is:')
for woord in lijstinvoer:
    if len(lijstinvoer) >= 10:
        if len(woord) <= 4:
            lijst4letter.append(woord)
print(lijst4letter)
#["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]
