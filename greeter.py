#greeter

#defining the function
def greet_user(username):
	"""Display a simple greeting."""
	print('Hello ' + username.title())

	#calling the function	
greet_user('david')

#tripple quotes are a docstring python looks for this when generating documentation