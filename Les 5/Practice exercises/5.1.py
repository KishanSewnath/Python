def seizoen(maand):
    if maand in range(3, 6):
        print('Het is lente.')
    elif maand in range(6, 9):
        print('Het is zomer.')
    elif maand in range(9, 12):
        print('Het is herfst.')
    elif maand in range (12, 3):
        print('Het is winter.')
    else:
        print('Dit kan niet!')

print(seizoen(eval(input('Hoeveelste maand is het?: '))))
