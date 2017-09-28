#deli
sandwich_orders = ['cheese' , 
					'tuna',
					'tomato',
					'ham',
					'salami',
					'salami',
					'salami'
					]
completed_orders = []
print("we are out of salami")

while 'salami' in sandwich_orders:
	sandwich_orders.remove('salami')
	
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich + '.')
	completed_orders.append(sandwich)
for order  in completed_orders:
	print(order)
	