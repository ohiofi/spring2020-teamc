import time

roomArray = []
itemArray = []
for i in range(999):
    roomArray.append(False)
    itemArray.append(False)
roomArray[601] = "There is an antique box here with a jewel inside. There is a couch to the south and you hear loud screaming to the east."
roomArray[701] = "You found your brother!"
roomArray[702] = "There is a chair to the south and a couch to the west. You hear loud screaming to the north."
roomArray[703] = "There is a chair here with a hat sitting on it. You hear screaming to the north."
roomArray[202] = "There is a table to your east and a TV to your south."
roomArray[203] = "The TV is all static and doesnt work, there is a remote on the tv. It looks like there is a hallway to your east."
roomArray[302] = "There is a interesting painting on the table. There is opening in the wall to the south."
roomArray[303] = "There is echoing coming down the hallway to your east and a tv to your west."
roomArray[403] = "You have enetered the hallway. There are more rooms east. An Echo is getting slightly louder."
roomArray[503] = "You are close to the end of the hallway. There is a clear echo of someone. There is a coin in this room and a room to your east."
roomArray[603] = "You are not in the hallway anymore, you are in a study. There is a chair to the east and a couch to the north."
roomArray[602] = "You are in a room with a couch and a scarf. There is an antique painting to the north."
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
            return False
        else:
            return True
    except:
        print("You can't go there.")
        return False

def moveFunction(userInput, room):
    if userInput == "n" and doesRoomExist(room - 1) == True:
        room = room - 1
    else:
        print("you can not go here")
    if userInput == "s" and doesRoomExist(room + 1) == True:
        room = room + 1
    else:
        print("you can not go here")
    if userInput == "e" and doesRoomExist(room + 100) == True: 
        room = room + 100
    else:
        print("you can not go here")
    if userInput == "w" and doesRoomExist(room - 100) == True:
        room = room - 100
    else:
        print("you can not go here")
    return room

def main():
    room = 202
    print("Welcome to Mansion Mystery!")
    time.sleep(1)
    print("By Callie, Shayan, and Dalton.")
    time.sleep(1)
    print("You are in the living room of a mansion. You're brother has been captured by some angry ghosts, and it is your job to save him.")
    time.sleep(2)
    while True:
        print(roomArray[room])
        print("Please type: n, s, e, w, or quit.")
        userinput = input()
        room = moveFunction(userinput, room)
