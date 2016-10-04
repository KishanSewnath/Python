cijferICOR=7.55
cijferPROG=4.64
cijferCSN=8.9
som = cijferICOR + cijferPROG + cijferCSN
gemiddelde = som / 3),1)
beloning = round((som * 30),1)
overzicht = ('Mijn cijfers (gemiddeld een %s) leveren een beloning van € %s op!' % (gemiddelde, beloning))
print (overzicht)
