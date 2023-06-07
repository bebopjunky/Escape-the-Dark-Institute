import random
from player import player
from room import room
from items import item

#validate input

def validate(command,action):
    if action == "player":
        for player in chapter:                        
            if command == player.get_name():
                return(command)
                break
               
        
        

#Player Setup
actions = ["roll ranged","roll melee","trade","heal","flank"]
print("Escape The Dark Institution")
print("How many players will try and escape?")
player_count = int(input(": "))

players = [None]*player_count

for i in range(0,player_count):
    print("")
    print("Player",i+1)
    print("Name your character")
    choice = input(": ")
    
    players[i] = player(choice)
    players[i].get_description()    

#Room Setup
room_deck = [None]*2
for i in range(0,len(room_deck)):
    room_deck[i] = room(player_count)

#Item Setup
item_deck = [None]*10
for i in range(0,len(item_deck)):
    item_deck[i] = item()



#Main Game

#Moves through each card in the deck
for card in room_deck:
    card.get_room_description()
    chapter = players.copy()
    ranged_combat = True
#Runs until the card is beat
    while len(card.get_room_health())>0:        
#Player Selection        
        print("Who will take an action?")
        player_character = validate(input(": "),"player")        
        if player_character != False:
            if ranged_combat == True:
                print("Will you engage in ranged combat?")








            if len(chapter) == 0:
                chapter = players.copy()
            else:
                for tmp in chapter:
                    tmp_name = tmp.get_name()
                    if tmp_name == player_character:
                        chapter.remove(tmp)
                        break   

                




#set current player

        