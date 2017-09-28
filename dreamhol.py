#dreamhol

responses = {}

polling_active = True

while polling_active:
	name = input("What is your name ")
	where = input("Where do you want to go ")
	#store the responses
	responses[name] = where
	
	again  = input('press y to go again ')
	
	if again == 'y':
		continue
	else:
		break
for name, where in responses.items():
			print(name + "  " + where)
			