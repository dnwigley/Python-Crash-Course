#movie2.py
prompt ="\nTell me your age:"
prompt += "\nEnter 'quit' to end the program. "
message =""
count = 0
#active = True
while count<10:
		message = input(prompt)
		count +=1
		
		if message == "":
			count -=1
			continue
		
		elif message == 'quit':
			active = False
			break
		
		elif float(message) <3:	
			print("You get a free ticket")
		
		elif  (float(message)>= 3) & (float(message) <= 12):
			print("Your ticket is $10")
			
		elif float(message) >12:
			print("Your ticket is $15")