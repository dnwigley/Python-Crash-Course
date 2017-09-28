#print_models.py


def print_models(unprinted_designs , completed_models):
	"""simulate printing each design, until none are left.
	move each design to completed_models after printing."""

	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#simulate creating a 3D print from the design.
		print('Printing mode: ' + current_design)
		completed_models.append(current_design)



def show_completed_models(completed_models):
	"""display all completed models"""
	
	print('\nThe following models have been printed:')
	for completed_model in completed_models:
		print(completed_model)

