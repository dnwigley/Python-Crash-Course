def build_car(manufacturer, model, **user_options):
	"""Build a dictionary containing car details."""
	car={'manufacturer':manufacturer,
		'model' :model,
		}
	
	for key, value in user_options.items():
		car[key] = value
	return car