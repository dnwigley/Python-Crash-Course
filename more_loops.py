#4.12
my_foods =['pizza','falafel','carrot cake']
fried_foods = my_foods[:]

print("My favorite foods are;-")
for food in my_foods:
	print(food.title())
	
print("My friends favorite foods are ;-")
for food in fried_foods:
	print(food.title())