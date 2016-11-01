bedrag = 4356
try:
    aant_mensen = int(input('Hoeveel mensen gaan er mee op reis?: '))
    bedragPP = bedrag/aant_mensen


    if aant_mensen <0:
        print('Negatieve getallen zijn niet toegestaan!')
    else:
        print('Het bedrag per persoon is: €{}'.format(bedragPP))
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')

