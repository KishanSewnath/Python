import requests
import xmltodict

api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=uw7tbns0awlo3ovvngkv55j4ofjq9u8m&dag=01-11-2016&sorteer=1'

response = requests.get(api_url)

filmsXML = xmltodict.parse(response.text)

for film in filmsXML['filmsoptv']['film']:
    titel = film['titel']
    starttijd = film['starttijd']
    print(titel)
    print(starttijd)
