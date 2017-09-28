#user
class User():
	"""User databse"""
	
	def __init__(self, first_name, last_name, password, age):
		"""Initialise name and user attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
		self.age = str(age)
	
	def describe_user(self):
		full_name = self.first_name.title() + ' ' + self.last_name.title()
		print(full_name + " is " + self.age + " years old")
		print(self.first_name.title() + "'s password is " + self.password)
		
	def greet_user(self):
		full_name = self.first_name.title() + ' ' + self.last_name.title()
		print("Hello " + full_name + " Oh it is you again!")
		
user_1 = User('david' , 'wigley', 'ghjkl', 49)
user_2 = User('bob', 'smith' , 'asda', 12)
user_3 = User('mel', 'bracey', 'ieqwqieuy', 31)

print('\n')
user_1.describe_user()
user_1.greet_user()
print('\n')
user_2.describe_user()
user_2.greet_user()
print('\n')	
user_3.describe_user()
user_3.greet_user()