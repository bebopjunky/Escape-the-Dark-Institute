from file_management.data import items
import random

class item():
    def __init__ (self):
        self.item_name = None
        self.item_desc = None
        self.item_weight = None
        self.item_type = None
        self.item_ammo = None
        self.item_ammo_full = None

        self.setup()

    def __str__(self):
        return f"{self.item_name}"
    
    def setup(self):
        tmp = random.choice(items)
        items.remove(tmp)
        item = tmp.split(",")

        self.item_name = item[0].strip()
        self.item_desc = item[1].strip()
        self.item_weight = item[2].strip()
        self.item_type = item[3].strip()
        self.item_ammo = item[4].strip()
        self.item_ammo_full = item[4].strip()   
    def get_description(self):
        print("*****************************************")
        print("Item Name: ",self.item_name)
        print(self.item_desc)
        print("Size",self.item_weight)
        if self.item_type == "b":
            print("It fires ballistic ammo and contains",self.item_ammo,"shots")
        elif self.item_type == "e":
            print("It fires energy ammo and contains",self.item_ammo,"shots")
        else:
            print("It fires explosive ammo and contains",self.item_ammo,"shots")
        print("*****************************************")  
    def get_ammo(self):
        return(self.item_ammo)   
    def get_type(self):
        if self.item_type == "b":
            return ("ballistic")
        elif self.item_type == "e":
            return ("energy")
        else:
            return ("explosive") 
    def reduce_ammo(self):
        self.item_ammo = 0   
    def reload(self):
        self.item_ammo = self.item_ammo_full