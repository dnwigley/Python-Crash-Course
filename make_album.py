#make album

def make_album(artist_name , album_title):
	""""Returns a dictionary based on artist name and album title"""
	album = {
			'Artist' : artist_name.title(),
			'Title' : album_title.title(),
			}
	return album
		
		
print("Enter q to quit")

while True:
	title = input("Enter album title: ")
	if title == "q":
		break
		
	artist = input("Enter artist: ")
	if artist =="q":
		break
		
	album = make_album(artist , title)
	print(album)
	
print("Good-bye!")
