from file_management.data import rooms
import random

class room():
    def __init__ (self,player_count):
        self.room_level = None
        self.room_name = None
        self.room_desc = None
        self.room_health = [None]
        self.room_rdamage = None
        self.room_cdamage = None
        self.room_reward = None
        self.room_ballistic = None
        self.room_energy = None
        self.room_explosive = None

        self.setup(player_count)
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

    def get_room_health(self):
        return(self.room_health)