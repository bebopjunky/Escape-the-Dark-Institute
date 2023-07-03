import random
from player import player
from room import *
from items import *

#validate input

def invalid():
    print("")
    print("*****************************************")
    print("Invalid Action")
    print("*****************************************")
    print("")
def validate(current_player,action):
    actions = ["roll ranged","reload","roll melee","trade","heal","flank","stats","room","drop"]
    if action == "player":
        for a in chapter:
            if current_player == a.get_name():
                return current_player
        invalid()
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
        elif action == "room":
            card.get_room_description()
        elif action == "drop":
            drop(current_player)
        return True
    else:
        invalid()
        return False  
#Actions
def roll_ranged(current_player):
    #Ranged Combat
    print("")
    print("*****************************************")
    print("ACTION: ROLL RANGED")
    weapon = current_player.get_weapon()
    if weapon is not False:        
        ranged_dice = ["Hit","Hit","Miss"]
        choices = ["c","m","w"]        
        print("you are fighting with",weapon)
        print("Ammo Type:",weapon.get_type())
        print("Ammo:",weapon.get_ammo())
        #this will roll for the amount of ammo
        for i in range(0,int(weapon.get_ammo())): 
            valid = False
            roll = random.choice(ranged_dice)
            print("")
            print("Your",i+1,"ammo")
            print("You rolled a ",roll)
            if roll == "Hit":
                if weapon.get_type() == "b":
                    ammo_mod = card.get_room_bdamage()
                elif card.get_room_edamage() == "e":
                    ammo_mod = card.get_room_edamage()
                else:
                    ammo_mod = card.get_room_xdamage()
                #this will apply the correct amount of damage to the room                    
                for i in range (0,(int(ammo_mod))):
                    while valid is not True:
                        print("")
                        print("How do you want to allocate the damage?")
                        print(choices)
                        print("Current Room Health:",card.get_room_health())
                        choice = input()
                        if choice in choices:
                            valid = True                                                 
                            card.remove_room_health(choice,current_player.get_mod())   
                        else:
                            print("Invalid Choice") 
                        if len(card.get_room_health()) == 0:
                            break
                    valid = False
        weapon.reduce_ammo()
        if current_player.get_flank() != True:        
            current_player.remove_health(int(card.get_room_rdamage()))        
def roll_melee(current_player):
        print("")
        print("*****************************************")
        print("ACTION: ROLL MELEE")
        roll = random.choice(current_player.dice)
        print("You rolled a ",roll)
        card.remove_room_health(roll,current_player.get_mod())
        current_player.remove_health(int(card.get_room_cdamage()))
def reload(current_player):
    weapon = current_player.get_weapon()
    weapon.reload()
    print("")
    print("*****************************************")
    print("ACTION: RELOAD")
def trade(current_player):
    tmp_list = players.copy()
    tmp_list.remove(current_player)
    print("")
    print("*****************************************")
    print("ACTION: TRADE")
    print("Available Players: ")
    for tmp_player in tmp_list:
        print(tmp_player)
    print("Which player do you want to trade with?")
    choice = input(": ")

    for trade_player in tmp_list:
        if choice == trade_player.get_name():
            current_player.get_inventory()
            trade_player.get_inventory() 
            print("Which item number do you want to trade: ")  
            choice = input(": ")
            if choice == "x":
                print("Cancel")
                return()
            trade_item = current_player.get_item(int(choice)-1)
            if trade_item != False:
                trade_player.set_inventory(trade_item)
                return()
    invalid()
def heal(current_player):
    print("")
    print("*****************************************")
    print("ACTION: HEAL")
    global heal_avaiable
    if heal_avaiable == True:
        current_player.heal()
        heal_avaiable = False
    else:
        print("")
        print("*****************************************")
        print("Heal Unavailable")
        print("*****************************************")
        print("")
def flank(current_player):
    print("")
    print("*****************************************")
    print("ACTION: FLANK")
    global flank_available
    if flank_available == True:
        ranged_dice = ["Hit","Hit","Miss"]
        roll = random.choice(ranged_dice)
        if roll == "Hit":
            print("You were hit while moving to flank")
            current_player.remove_health(1)
        current_player.flank()
        flank_available = False
    else:
        print("")
        print("*****************************************")
        print("Flanking Unavailable")
        print("*****************************************")
        print("")
def drop(current_player):
    current_player.get_inventory()
    print("Which item should you drop?")
    choice = input(": ")
    if choice == "x":
                print("Cancel")
                return()
    current_player.drop(int(choice)-1)

#Item Setup
item_deck = [None]*10
for i in range(0,len(item_deck)):
    item_deck[i] = weapon()

#Player Setup
print("")
print("Escape The Dark Institution")
print("")
#validation of player_count
player_count = ""
while not(isinstance(player_count,int)):
    print("How many players will try and escape?")
    player_count = input(": ")
    if player_count.isdigit():
        player_count = int(player_count)

players = [None]*player_count
for counter,tmp in enumerate(players):
    print("")
    print("Player",counter+1)
    print("Name your character")
    choice = input(": ")
    players[counter] = player(choice)
    players[counter].set_inventory(random.choice(item_deck))
    players[counter].get_description()

#Room Setup
# room_deck = [None]*(2*player_count)
# for counter, tmp in enumerate(room_deck):
#     room_deck[counter] = room(player_count)

room_deck = []
for i in range(0,3):
    room_deck.append(level_1(player_count))
for i in range(0,3):
    room_deck.append(level_2(player_count))
for i in range(0,3):
    room_deck.append(level_3(player_count))    
room_deck.append(boss(player_count))   
#Main Game

#Moves through each card in the deck
for card in room_deck:
    card.get_room_description()
    chapter = players.copy()
    ranged_combat = True
    heal_avaiable = True
    flank_available = True
    for character in chapter:
        character.reload()
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
                print("roll ranged","¦","roll melee","¦","trade","¦","heal","¦","flank","¦","stats","¦","reload","¦","trade","¦","drop")
                print("")                   
                print("What action will you take?")
                valid = validate(current_player,input(": "))
            chapter.remove(current_player)
    print("")
    print("ROOM COMPLETED")
    print("")
print("YOU WIN!")
    