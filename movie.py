#movie.py
prompt ="\nTell me your age:"
prompt += "\nEnter 'quit' to end the program. "
message =""
active = True
while active:
		message = input(prompt)
		 
		if message == 'quit':
			active = False
			break
		
		elif float(message) <3:	
			print("You get a free ticket")
		
		elif  (float(message)>= 3) & (float(message) <= 12):
			print("Your ticket is $10")
			
		elif float(message) >12:
			print("Your ticket is $15")