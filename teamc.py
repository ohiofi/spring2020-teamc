roomArray = []
itemArray = []
for i in range(999):
    roomArray.append(False)
    itemArray.append(False)
roomArray[601] = "There is an antique box here with a jewel inside. There is a couch to the south and you hear loud screaming to the east."
roomArray[701] = "You found your brother!"
roomArray[702] = "There is a chair to the south and a couch to the west. You hear loud screaming to the north."
roomArray[703] = "There is a chair here with a hat sitting on it. You hear screaming to the north."
roomArray[202] = "there is a table to your east and a tv to your south"
roomArray[203] = "the tv is all static and doesnt work, there is a remote on the tv. looks like a hallway to your east"
roomArray[302] = "there is a interesting painting on the table. there is opening in the wall to the south"
roomArray[303] = "there is echoing coming down the hallway to your east and a tv to your west"
itemArray[601] = "Jewel"
itemArray[703] = "Hat"
itemArray[602] = "Scarf"
itemArray[503] = "Coin"
itemArray[203] = "Remote"
itemArray[302] = "Painting"

def doesRoomExist(roomNumber):
    try:
        if roomArray[roomNumber] == False:
            print("You can't go there.")
        else:
            return True
    except:
        print("You can't go there.")
        return False
