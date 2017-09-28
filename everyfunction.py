#try it yourself 3-10
juggle=['2 ball','3 ball','5 ball','3 clubs','6 club passing','7 club passing','fire breathing','unicycling']
#accessing items in the list
print(juggle[3])
#modifying an item in a list
juggle[0]='stilts'
print(juggle)
#appending to a list to the end
juggle.append('fire poy')
print(juggle)
#inserting into a list
juggle.insert(0,'hula hoop')
print(juggle)
#deleting a item from a list
del juggle[0]
print(juggle)
#removing, popping, an item from a list and using it pop(n)
popped_juggle=juggle.pop()
print(juggle)
print(popped_juggle)
#removing an item by postion in list
difficlut_pop=juggle.pop(5)
print(juggle)
print(difficlut_pop+" is too diffcult for me")
#removing an item by value
print(juggle)
juggle.remove('5 ball')
print(juggle)
#sorting a list
juggle.sort()
print(juggle)
#sorting in reverse order not not alphabetical
juggle.reverse()
print(juggle)
#sorting a list temporarily
print('\nHere is the sorted list:')
print(sorted(juggle))
print('\nHere is the original list:')
print(juggle)
#printing the legth of a list
length=len(juggle)
print(length)
#print(juggle[11]) - testing for index out of range