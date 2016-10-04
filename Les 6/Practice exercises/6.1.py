cijfers = {
    'Kishan Sewnath':6.3,
    'Gokmen Simsek':7.9,
    'Ozgur Ozturk':9.3,
    'Sebastiaan van Rijn':7.8,
    'Kendrick Lamar':8.6,
    'Lil Kleine':3.6,
    'Lange Frans':4.6,
    'Arsalan Anwari':9.9}

for (key, waarde) in cijfers.items():
    if waarde > 9:
        print('{} heeft een {}'.format(key, str(waarde)))

