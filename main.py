import random
from player import player
from room import room
from items import item

#validate input

def validate(command,action):
    if action == "player":
        for a in chapter:
            if command == a.get_name():
                return command
        return False


def roll_ranged(current_player):
    #Ranged Combat
    print("")
    print("*****************************************")
    print("You are carrying: ")
    print()
    pass

def roll_melee(current_player):
    pass

def trade(current_player):
    pass
    
def heal(current_player):
    pass

def flank(current_player):
    pass

#Item Setup
item_deck = [None]*10
for i in range(0,len(item_deck)):
    item_deck[i] = item()

#Player Setup
actions = ["roll ranged","roll melee","trade","heal","flank"]
print("Escape The Dark Institution")
print("How many players will try and escape?")
player_count = int(input(": "))

players = [None]*player_count

# for i in range(0,player_count):
#     print("")
#     print("Player",i+1)
#     print("Name your character")
#     choice = input(": ")
#     players[i] = player(choice)
#     players[i].set_inventory(random.choice(item_deck))
#     players[i].get_description()

for tmp in players:
    print("")
    print("Player",i+1)
    print("Name your character")
    choice = input(": ")
    tmp = player(choice)
    tmp.set_inventory(random.choice(item_deck))
    tmp.get_description()

# for tmp in players:    
#     tmp.set_inventory(random.choice(item_deck))


#Room Setup
room_deck = [None]*2
for tmp in room_deck:
    tmp = room(player_count)

#Main Game

#Moves through each card in the deck
for card in room_deck:
    card.get_room_description()
    chapter = players.copy()
    ranged_combat = True
#Runs until the card is beat
    while len(card.get_room_health())>0:
#Player Selection
        if len(chapter) == 0:
            chapter = players.copy()
        print("")
        print("Who will take an action?")
        choice = validate(input(": "),"player")
        if choice is not False:
            for tmp in chapter:
                tmp_name = tmp.get_name()
                if tmp_name == choice:
                    current_player = tmp
            if ranged_combat is True:
                print("Will you engage in ranged combat? y/n")
                choice = input(": ")
                if choice == "y":
                    roll_ranged(current_player)
                chapter.remove(current_player)                
        else:
            print("*****************************************")
            print("Invalid Choice")
            print("*****************************************")
#set current player