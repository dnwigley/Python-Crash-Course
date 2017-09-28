#Restaurant

class Restaurant():
	"""Resturant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialise name and cuisine attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print("This restaurant is called " + self.restaurant_name.title())
		print("It sells " + self.cuisine_type +" food")
		
	def open_restaurant(self):
		print(self.restaurant_name + " is open!")
		
fish_shop = Restaurant('Siene Rigger', 'Fish and Chips')
fish_shop.describe_restaurant()

chinese_shop = Restaurant('Tiger Lilly', 'Chineese')
chinese_shop.describe_restaurant()

Thai_shop = Restaurant('Thai palace', 'Thai')
Thai_shop.describe_restaurant()


print("\nMy fish shop is called " + fish_shop.restaurant_name.title() + ".")
print("My fish shop sells " + fish_shop.cuisine_type + ".")
fish_shop.open_restaurant()

print("\nMy local shop is called " + chinese_shop.restaurant_name.title() + ".")
print("My local shop sells " + chinese_shop.cuisine_type + ".")

chinese_shop.open_restaurant()