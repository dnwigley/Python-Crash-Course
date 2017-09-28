#6-6 favourite languages

favourite_languages = {
						'jen':'python',
						'sarah' : 'c',
						'edward' : 'python',
						'phil' : 'python',
						}
				for name, language in favourite_languages.items():
print(name.title() +"'s favourite language is " + language.title() +".")
print('\n')			
						
poll_list =['jen' ,  'dave' , 'sarah' , 'robert' , 'andrew']

for poller in poll_list:
	if poller in favourite_languages.keys():
		print("Thank you " + name.title() +" for taking the poll")
	else:
		print(poller.title() +" please take the poll")