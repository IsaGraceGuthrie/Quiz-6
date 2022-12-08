#the authors name is Isa Grace Guthrie 
import dbm

photo_category=dbm.open("captions","c")

# photo_category["fish.png"]="a clown fish"
# photo_category["computer.png"]="one HP elite desk computer"
# photo_category["newsweater.png"]="a green and red christmas sweater"
# this part is copied from my writing portion
# for item in photo_category:
#     print(item,photo_category[item])
#this part was me testing out my word.

photo_category["fish.png"]="a yellow one and a blue one"
photo_category["computer.png"]="one macbok air in rose gold"
photo_category["newsweater.png"]="now actually new just borrowed from my roommate"


for item in photo_category:
    print(item,photo_category[item])
