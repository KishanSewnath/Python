cijferICOR=7.6
cijferPROG=9.6
cijferCSN=3.8
gemiddelde=((cijferCSN+cijferPROG+cijferICOR)/3)
beloning=(gemiddelde*30.0)
overzicht=('Mijn cijfers (gemiddeld een %s) leveren een beloning van € %s op!') % (gemiddelde, beloning)
print(overzicht)
