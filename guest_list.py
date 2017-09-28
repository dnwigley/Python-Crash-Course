guest=['mark','dougie','simon']
print(guest[0].title()+" would you like to come to dinner?")
print(guest[1].title()+" would you like to come to dinner?")
print(guest[2].title()+" would you like to come to dinner?")
# 3 on list
print("\n")
print("woops "+ guest[0].title() + " Can't make it")
#swaps person on list
guest[0] = "Barry"
print("\n")
#print the list
print(guest[0].title()+" would you like to come to dinner?")
print(guest[1].title()+" would you like to come to dinner?")
print(guest[2].title()+" would you like to come to dinner?")
#insert more guests
print("\n")
print("I have a bigger table!")
guest.insert(0,"wayne")
guest.insert(3,"fred")
guest.append("mel")
#print(guest)
#6 on list? Yes!
#try it yourself 3.9
message="There are " + str(len(guest)) + " " + "Comming to dinner"
print(message)
print(guest[0].title()+" would you like to come to dinner?")
print(guest[1].title()+" would you like to come to dinner?")
print(guest[2].title()+" would you like to come to dinner?")
print(guest[3].title()+" would you like to come to dinner?")
print(guest[4].title()+" would you like to come to dinner?")
print(guest[5].title()+" would you like to come to dinner?")
print("\n")
print("My table is delayed I can only invite 2!")
print(guest.pop().title() +" Sorry you have been dropped!")
print(guest.pop().title() +" Sorry you have been dropped!")
print(guest.pop().title() +" Sorry you have been dropped!")
print(guest.pop().title() +" Sorry you have been dropped!")
#print(guest)
print("\n")
print(guest[0].title()+" you are still able to come to dinner")
print(guest[1].title()+" you are still able to come to dinner")
print("\n")
del guest[0]
del guest[0]
print(guest)
