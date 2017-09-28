#aliens
#make an empty list for storing aliens

aliens = []
for alien_number in range(30):
	new_alien = {'colour' : 'green' , 'points' : 5 , 'speed' : 'slow'}
	aliens.append(new_alien)

	#changing a slice of aliens
for alien in aliens[0:3]:
	if alien['colour'] == 'green' :
		alien['colour'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = '10'

	
	
#show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

#show how many aliens have  been created
print("Total number of aliens: " + str(len(aliens)))