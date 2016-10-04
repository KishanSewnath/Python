leeftijd = eval(input('Geef je leeftijd: '))
Paspoort = input('Nederlands paspoort: ')

if leeftijd > 17:
   if Paspoort == 'Ja' or Paspoort == 'ja':
       print('Gefeliciteerd, je mag stemmen!')
   else:
       print ('Helaas, je mag niet stemmen.')


if leeftijd <= 17:
   if Paspoort == 'Nee' or Paspoort == 'nee':
       print ('Helaas, je mag niet stemmen.')
   else:
       print ('Helaas, je mag niet stemmen.')
