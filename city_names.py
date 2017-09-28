#city names

def city_country(city , country):
	"""This function returns a string formatted 'Santiago, Chile'"""
	output = (city.title() + ', ' + country.title())
	return output

output = city_country('london','england')
print (output)

output=city_country('new york' , 'u s a')
print (output)

output=city_country('tokya' , 'japan')
print (output)