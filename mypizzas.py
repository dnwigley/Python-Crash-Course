#try it yourself 4-1 pizzas
pizzas=['hawaiian',"cheese and tomato",'peperoni']
friend_pizza = pizzas[:]
for food in pizzas:
	print('My favourite pizzas are '+food)
print("\nI really like pizza\n")
friend_pizza.append('ham')

for food in friend_pizza:
	print('My friend favourite pizzas are '+food)
print("\nHe really like pizza\n")