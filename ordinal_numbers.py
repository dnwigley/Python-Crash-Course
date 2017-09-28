#ordinal numbers

numbers =[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
for numbers in numbers:
	if numbers == 1:
		print(str(numbers) + "st" )
	
	elif numbers == 2:
		print(str(numbers) + "nd" )
		
	elif numbers ==3:
		print(str(numbers) + "rd" )
		
	elif  (numbers > 3) and (numbers <= 9):
		print(str(numbers) + "th")
		
#note the str() function it was needed to print an int as a str
#I could have stored the list a strings !