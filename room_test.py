from room import *
from file_management.data import room_descriptions
import random


#new_room = level_1(2)
#new_room.get_room_description()
colours = ["aqua",
           "black",
           "blue", 
           "fuchsia", 
           "gray",
            "green",
            "lime",
            "maroon",
            "navy",
            "olive",
            "purple",
            "red",
            "silver",
            "teal",
            "white",
            "yellow"]
colour = random.choice(colours)
colours.remove(colour)
room_title = f"This is: The {colour} room."
room_description = random.choice(room_descriptions)
room_descriptions.remove(room_description)

print(room_title)
print(room_description)