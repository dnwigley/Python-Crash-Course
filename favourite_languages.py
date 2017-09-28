#favourite languages
favourite_languages = {
						'jen':'python',
						'sarah' : 'c',
						'edward' : 'python',
						'phil' : 'python',
						}

Friends = ['phil' , 'sarah']
for name in favourite_languages.keys():
	print(name.title())
	#print(favourite_languages[name])
	if name in Friends:
		print(" Hi " + name.title() +
				", I see your favourite language is " +
				favourite_languages[name].title() + "!")