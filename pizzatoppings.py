#pizzatoppings.py
prompt ="\nEnter a pizza topping: "
prompt += "\nEnter 'quit' to end the program. "
message =""
while message != 'quit' :
	message = input(prompt)
	
	if message != 'quit':
		print("\n I will add " + message + " to your pizza")