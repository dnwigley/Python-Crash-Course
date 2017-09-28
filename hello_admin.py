#hello_admin 5-8, 5-9
usernames = []#'admin' , 'dave' , "ian" , "andrew" , "robert"]

for usernames in usernames:
	if usernames in usernames:
		if usernames == 'admin':
			print("Hellow admin would you like to see a stuatus report?")
		else:
			print("Hello " + usernames + ".")
else:
	print("We need some more users!")