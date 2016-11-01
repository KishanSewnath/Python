score = eval(input('Geef je score: '))

if score > 15:
   print('Gefeliciteerd!')
   print('Met een score van %s ben je geslaagd!' % (score))
if score <= 15:
   print('Helaas.')
   print('Met een score van %s ben je gezakt.' % (score))
