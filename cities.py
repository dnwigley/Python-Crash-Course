#cities
lon = {	'country':
		'UK',
		'Population':
		'4000',
		'fact':
		'4 square miles',
		
		}

bat = {	'country':
		'UK',
		'Population':
		'5000',
		'fact':
		'roman town',	
		}	

bris = {'country':
		'UK',
		'Population':
		'9000',
		'fact':
		'it has a lovely suspension bridge',
		
		}

cities ={ 	'London':
			lon,
			'Bath':
			bat,
			'Bristol':
			bris,
			
			}
for city,fact in cities . items():
	print(city.title() + ' is located in the ' + fact['country'] + ' ' + fact['Population'] + ' people live there and it has ' + fact['fact'])
