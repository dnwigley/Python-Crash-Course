#magicians
magicians =['paul daniels' ,
			'stephen mulhern' ,
			'david wigley',
			]
			
def show_magicians(magicians):
	for magicians in magicians:
		print(magicians.title())
		
#show_magicians(magicians)

def make_great(magicians):
	
	great_magicians = []
	
	while  magicians:
		magician = magicians.pop()
		great_magician = magician + ' The Great'
		great_magicians.append(great_magician)
		
	for great_magician in great_magicians:
		magicians.append(great_magician)
		
		print(great_magicians)
		return great_magicians
		
		
print("The original list")		
show_magicians(magicians)

print('\nNew list')
great_magic = make_great(magicians)
show_magicians(great_magic)		

print('\nOrignal list')
show_magicians(magicians)
