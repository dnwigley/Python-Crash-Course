#checking usernames
curent_users = ['bob' , 'john' , 'dave', 'andrew' , 'robert']
curent_users = [x.lower() for x in curent_users]

new_users =  ['Dave' , 'john' , 'nick' , 'paul' , 'mathew']
new_users = [x.lower() for x in new_users]


for curent_users in curent_users:
	if curent_users in new_users:
		print("User name " + curent_users.title() + " taken please pick another name")
	else:
		print("User name " + curent_users.title() + " available")
