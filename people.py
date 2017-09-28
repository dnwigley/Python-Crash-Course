#6-7 People
person1 = {
		'first_name' : 'david' ,
		'last_name' : 'wigley' ,
		'age' : '49' ,
		'city' : 'tadworth',
		}

person2 = {
		'first_name' : 'mel' ,
		'last_name' : 'bracey' ,
		'age' : '48' ,
		'city' : 'tadworth',
		}
	
person3 = {
		'first_name' : 'andrew' ,
		'last_name' : 'bracey' ,
		'age' : '14' ,
		'city' : 'tadworth',
		}

people = [person1 , person2 , person3]

for person in people:
	print(person['first_name'].title())
	print(person['last_name'].title())
	print(person['age'].title())
	print(person['city'].title())
	print('\n')