#printing_models.py

import print_models


#start with some designs that need to be printed.		
unprinted_designs = ['iphone case' , 'robot pendant' , 'dodecahedron']
completed_models = []

print_models.print_models(unprinted_designs, completed_models)
print_models.show_completed_models(completed_models)