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

    def __str__(self):
        return f"{self.title}"    

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
    def get_mod(self):
        return(self.mod_att)
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
        for item in self.inventory:
            item.get_description()
        print("*****************************************")
        print("")
    def get_name(self):
        return(self.name)
    def set_inventory(self,item):
        if self.inventory_weight>4:
            print("Your inventory is full")
        else:
            self.inventory.append(item)
            self.inventory_weight=0
            for stuff in self.inventory:
                self.inventory_weight = int(stuff.item_weight) + self.inventory_weight
    def get_ammo(self):
        for weapon in self.inventory:
            if int(weapon.item_ammo) > 0:
                return (weapon)
            else:
                print("")
                print("Out of ammo")
                print("")
                return False
            