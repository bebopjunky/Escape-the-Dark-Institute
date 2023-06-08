import random
from file_management.data import mods


class player():

    def __init__(self,name):
        self.name = name
        self.title = None
        self.dice = []
        self.health = 12
        self.mod_att = None
        self.mod_desc = None
        self.inventory = []
        self.inventory_weight = 0
        
        self.set_character(name)
        self.set_mod()

    def set_character(self,name):
        stats = ["m","c","w"]
        ranks = ["Boss","Worker","Drone","Engineer","Spider","Monkey","Clown","Human","Dog"]
        self.dice = random.choices(stats, weights = [1, 1, 1], k = 6)
        self.title = name + " The " + random.choice(ranks)    
    def set_mod(self):
        tmp = random.choice(mods)
        mods.remove(tmp)
        mod = tmp.split(",")
        self.mod_desc = mod[0]
        self.mod_att = mod[1]
    def c_roll(self):
        roll = random.choice(self.dice)
        return(roll)
    def r_roll(self):
        pass
    def get_description(self):
        print("")
        print("*****************************************")
        print(self.title)
        print("Health: ",self.health)
        print("Might",self.dice.count("m"))
        print("Cunning",self.dice.count("c"))
        print("Wisdom",self.dice.count("w"))
        print("Mod",self.mod_desc,"which gives you additional: ",self.mod_att)
        print("You are Carrying: ")
        self.get_inventory()
        print("*****************************************")
        print("")
    def get_name(self):
        return(self.name)
    def get_inventory(self):
        for item in self.inventory:
            print("")
    def set_inventory(self,item):
        if len(self.inventory_weight) >4:
            print("Your inventory is full")
        else:
            self.inventory.append(item)