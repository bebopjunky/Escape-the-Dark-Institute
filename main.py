import random
from player import player
from room import room
from items import item

#validate input

def validate(current_player,action):
    actions = ["roll ranged","roll melee","trade","heal","flank","stats"]
    if action == "player":
        for a in chapter:
            if current_player == a.get_name():
                return current_player
        print("*****************************************")
        print("Invalid Choice")
        print("*****************************************")
        return False
    elif action == "stats":
        current_player.get_description()
    elif action in actions:
        print("")
        if action == "help":
            print("Available Actions")
            print(actions)
        elif action == "roll ranged":
            roll_ranged(current_player)            
        elif action == "roll melee":
            global ranged_combat
            ranged_combat = False
            roll_melee(current_player)
        elif action == "trade":
            trade(current_player)
        elif action == "heal":
            heal(current_player)
        elif action == "flank":
            flank(current_player)
        return True
    else:
        print("")
        print("Invalid Action")
        print("")
        return False
    
#Actions
def roll_ranged(current_player):
    #Ranged Combat
    weapon = current_player.get_weapon()
    if weapon is not False:        
        ranged_dice = ["Hit","Hit","Miss"]
        choices = ["c","m","w"]        
        print("you are fighting with",weapon)
        print("Ammo:",weapon.get_ammo())
        for i in range(0,int(weapon.get_ammo())): 
            valid = False
            roll = random.choice(ranged_dice)
            print("You rolled a ",roll)
            if roll == "Hit":
                if weapon.get_type() == "b":
                    ammo = card.get_room_bdamage()
                elif card.get_room_edamage():
                    ammo = card.get_room_edamage()
                else:
                    ammo = card.get_room_xdamage()
                ####### ADD IN THE FOR LOOP BELOW!
                for i in range (0,(int(ammo))):
                    while valid is not True:
                        print("How do you want to allocate the damage?")
                        print(choices)
                        choice = input()
                        if choice in choices:

                            valid = True
                            card.remove_room_health(choice,current_player.get_mod())                        
                            current_player.remove_health(int(card.get_room_rdamage()))
                        else:
                            print("Invalid Choice")        

                
def roll_melee(current_player):
        roll = random.choice(current_player.dice)
        print("You rolled a ",roll)
        card.remove_room_health(roll,current_player.get_mod())
        current_player.remove_health(int(card.get_room_rdamage()))

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
print("Escape The Dark Institution")
print("How many players will try and escape?")
player_count = int(input(": "))
players = [None]*player_count
for counter,tmp in enumerate(players):
    print("")
    print("Player",i+1)
    print("Name your character")
    choice = input(": ")
    players[counter] = player(choice)
    players[counter].set_inventory(random.choice(item_deck))
    players[counter].get_description()

#Room Setup
room_deck = [None]*2
for counter, tmp in enumerate(room_deck):
    room_deck[counter] = room(player_count)

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
        print("Available Players: ")
        for a in chapter:
            print(a)
        print("")
        print("Who will take an action?")
        choice = validate(input(": "),"player")
        if choice is not False:
            for tmp in chapter:
                tmp_name = tmp.get_name()
                if tmp_name == choice:
                    current_player = tmp
            valid = False
            while valid is not True:
                print("Available Actions")
                print("roll ranged","¦","roll melee","¦","trade","¦","heal","¦","flank","¦","stats")
                print("")                   
                print("What action will you take?")
                valid = validate(current_player,input(": "))
            chapter.remove(current_player)
    print("")
    print("ROOM COMPLETED")
    print("")
    