import time
from map import *

correctAnswers = []
wrongAnswers = []
roomArray = []
itemArray = []
for i in range(999):
    roomArray.append(False)
    itemArray.append(False)
roomArray[601] = "There is an antique box here. There is a couch to the south and you see something shiny to the east."
roomArray[701] = "You are in the north east corner of the study"
roomArray[702] = "There is a chair to the south and a couch to the west. You see something shiny to the north."
roomArray[703] = "There is a chair here. There is a door to the west."
roomArray[202] = "There is a table to your east and a TV to your south."
roomArray[203] = "The TV is all static and doesn't work. It looks like there is a hallway to your east."
roomArray[302] = "There is a table here. There is opening in the wall to the south."
roomArray[303] = "There is echoing coming down the hallway to your east and a tv to your west."
roomArray[403] = "You have entered the hallway. There is something on the ground. There are more rooms east. An echo is getting slightly louder."
roomArray[503] = "You are close to the end of the hallway. There is a window here and the echo is louder. There is a room to your east."
roomArray[603] = "You are not in the hallway anymore, you are in a study. There is a chair to the east, a couch to the north, and a door to the south."
roomArray[602] = "There is a couch here. There is an antique box to the north."
roomArray[604] = "You are now in the kitchen. There is a table in front of you."
roomArray[605] = "There is a table here. There is a counter to the east."
roomArray[606] = "You found your brother!"
roomArray[705] = "knife"
roomArray[706] = "bowl"
itemArray[601] = "Jewel"
itemArray[703] = "Hat"
itemArray[602] = "Scarf"
itemArray[503] = "Coin"
itemArray[203] = "Remote"
itemArray[302] = "Painting"
roomArray[705] = "knife"
roomArray[706] = "bowl"
itemArray[604] = "spoon"
itemArray[605] = "plate"
itemArray[403] = "glove"
itemArray[701] = "key"

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
    elif userInput == "s" and doesRoomExist(room + 1) == True:
        room = room + 1
    elif userInput == "e" and doesRoomExist(room + 100) == True:
        room = room + 100
    elif userInput == "w" and doesRoomExist(room - 100) == True:
        room = room - 100
    return room

def doesItemExist(itemNumber):
    try:
        if not itemArray[itemNumber] == False:
            print("Item" + itemArray[room])
    except:
      return

def specialRooms():
  if room == 604:
    if "key" not in inventory:
      print("the room to the south is locked. You need a key to unlock it.")
      roomArray[603] = False
    else:
      print("You used the key to unlock the door.")
      roomArray[304] = "The unlocked door leads into the kitchen"

score = 0
def askQuestion(question , answer):
  while True:
    global score
    print(question)
    userInput = str(input())
    userInput = userInput.lower()
    if userInput == answer:
      score = score + 5
      correctAnswers.append(userInput)
      print("Correct, your score is " + str(score))
      break
    else:
      score = score - 3
      wrongAnswers.append(userInput)
      print("Incorrect, your score is " + str(score))

def startQuiz():
  askQuestion("Using letters, what does 5 times 2 equal?", answer = "ten")
  askQuestion("Using letters, what does 9 divided by 3 equal?", answer = "three")
  askQuestion("Using letters, what does 7 plus 5 equal?", answer = "twelve")
  askQuestion("Using letters, what does 4 times 2 equal?", answer = "eight")
  askQuestion("Using letters, what does 2 divided by 1 equal?", answer = "two")
  askQuestion("Using letters, what does 4 plus 5 equal", answer = "nine")


def main():
    room = 202
    map = Map()
    print("Welcome to Mansion Mystery!")
    time.sleep(1)
    print("By Callie, Shayan, and Dalton.")
    time.sleep(1)
    print("You are in the living room of a mansion. You're brother has been captured by some angry ghosts, and it is your job to save him.")
    time.sleep(2)
    while True:
        print(roomArray[room])
        map.draw(roomArray, itemArray, room)
        if not itemArray[room] == False:
            print("Items here: " + itemArray[room])
            print("Please type: n, s, e, w, take or quit.")
            userInput = input()
            room = moveFunction(userInput, room)
        else:
            print("Please type: n, s, e, w,  or quit.")
            userInput = input()
            room = moveFunction(userInput, room)
        if userInput == "take":
            print("You have taken this item: " + itemArray[room])
            itemArray[room] = False
        if userInput == "quit":
            break
