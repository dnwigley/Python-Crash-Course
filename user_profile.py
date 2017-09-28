#user_profile.py

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', location= 'princetown', field = 'physics')

print(user_profile)

user_profile = build_profile('david', 'wigley', location= 'job', field = 'consultant', hobby= 'cirus skills')
print(user_profile)