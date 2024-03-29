from file_management.data import rooms
from file_management.data import room_descriptions
import random
colours = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
    "white",
    "black",
    "gray",
    "brown",
    "pink",
    "purple",
    "maroon",
    "navy",
    "turquoise",
    "cyan",
    "magenta",
    "lime",
    "olive",
    "tan",
    "sienna",
    "gold",
    "silver",
    "bronze",
    "coral",
    "aquamarine",
    "fuchsia",
    "lavender",
    "mint",
    "maize",
    "ochre",
    "scarlet",
    "taupe",
    "wheat",
    "azure",
    "ecru",
    "ivory",
    "pearl",
    "slate",
]
class room():
    def __init__ (self,player_count):
        self.room_level = None
        self.room_name = None
        self.room_desc = None
        self.room_health = []
        self.room_rdamage = None
        self.room_cdamage = None
        self.room_reward = None
        self.room_ballistic = None
        self.room_energy = None
        self.room_explosive = None

        #self.setup(player_count)
        
    def __str__(self):
        return f"{self.room_name}"

    def setup(self,player_count):
        tmp = random.choice(rooms)
        rooms.remove(tmp)
        room = tmp.split(",")

        self.room_level = room[0]
        self.room_name = room[1]
        self.room_desc = room[2]
        self.room_health = room[3].split("#")
        self.room_rdamage = room[4]
        self.room_cdamage = room[5]
        self.room_reward = room[6]
        self.room_ballistic = room[7]
        self.room_energy = room[8]
        self.room_explosive = room[9]

        stats = ["m","c","w"]
        for i in range(0,player_count):
            tmp = random.choice(stats)
            self.room_health.append(tmp)

    def rnd_setup(self,player_count):                      
            colour = random.choice(colours)
            colours.remove(colour)
            self.room_name = f"The {colour} room."

            room_description = random.choice(room_descriptions)
            room_descriptions.remove(room_description)
            self.room_desc = room_description
            
            #self.room_health = room[3].split("#")
            health = ["m","c","w"]
            for i in range(0,((player_count*int(self.room_level)))):
                room_health = random.choice(health)
                self.room_health.append(room_health)            
            self.room_rdamage = random.randint(0,int(self.room_level))
            self.room_cdamage = random.randint(0,int(self.room_level))
            self.room_reward = random.randint(0,int(self.room_level)) + 1
            self.room_ballistic = random.randint(0,int(self.room_level)) + 1
            self.room_energy = random.randint(0,int(self.room_level)) + 1
            self.room_explosive = random.randint(0,int(self.room_level)) + 2

    def get_room_description(self):
        print("")
        print("*****************************************")
        print("This is:",self.room_name)
        print(self.room_desc)
        print("Health:",self.room_health)
        print("Ranged Combat Attack Damage:",self.room_rdamage)
        print("Close Combat Attack Damage",self.room_cdamage)
        print("Reward:",self.room_reward,"items")
        print("The room will take",self.room_ballistic,"ballistic damage")
        print("The room will take",self.room_energy,"energy damage")
        print("The room will take",self.room_explosive,"explosive damage")
        print("*****************************************")
        print("")
    
    def get_room_rdamage(self):
        return (self.room_rdamage)
    def get_room_bdamage(self):
        return (self.room_ballistic)
    def get_room_edamage(self):
        return (self.room_energy)
    def get_room_xdamage(self):
        return (self.room_explosive)                     
    def get_room_health(self):
        return(self.room_health)
    def remove_room_health(self,roll,mod):        
        if roll in self.room_health:
            self.room_health.remove(roll)
            if mod in self.room_health:
                self.room_health.remove(mod)
                print("Mod Activated!")            
            print("Current Room Health:",self.room_health)

class level_1(room):
    def __init__(self,player_count):
        super().__init__(player_count)
        self.room_level = 1
        self.rnd_setup(player_count)
class level_2(room):
    def __init__(self,player_count):
        super().__init__(player_count)
        self.room_level = 2
        self.rnd_setup(player_count)
class level_3(room):
    def __init__(self,player_count):
        super().__init__(player_count)
        self.room_level = 3
        self.rnd_setup(player_count)
class boss(room):
    def __init__(self,player_count):
        super().__init__(player_count)
        self.room_level = 4
        self.rnd_setup(player_count)     

#create sub classes for the different room types. 