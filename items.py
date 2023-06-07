from file_management.data import items
import random

class item():
    def __init__ (self):
        self.item_name = None
        self.item_desc = None
        self.item_weight = None
        self.item_type = None
        self.item_ammo = None

        self.setup()

    def setup(self):
        tmp = random.choice(items)
        items.remove(tmp)
        item = tmp.split(",")

        self.item_name = item[0].strip()
        self.item_desc = item[1].strip()
        self.item_weight = item[2].strip()
        self.item_type = item[3].strip()
        self.item_ammo = item[4].strip()