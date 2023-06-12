import random

dice = ["r","p","s"]
room_health = ["r","p","r","r","p"]


def roll(dice,room_health):
    roll = random.choice(dice)
    print("you rolled a",roll)
    if roll in room_health:
        print("a hit")
                           
        room_health.remove(roll)


while len(room_health) > 0:
    print("will you shoot?")
    action = input(": ")
    if action == "y":
        roll(dice,room_health)
        print(room_health)
    else:
        print("Loser")
        break


