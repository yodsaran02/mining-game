
import random
import time
import os
print("loading...")
coordinates_x = []
coordinates_y = []
#make coordinates list
for x in range(-1000,1001):
    coordinates_x.append(x)
for y in range(-1000,1001):
    coordinates_y.append(y)
print("done")
#player_inventory
player_inventory = []
#ore_list
dirt_cords = []
stone_cords = []
iron_cords = []
gold_cords = []
diamond_cords = []
allore = 4000000
dirtore= allore*1
stonetore= allore*0.7
ironore= allore*0.3
goldore= allore*0.1
diamondore= allore*0.01


print("dirtore_finished")

for s in range(int(stonetore)-1):
    stonetore_cords = []
    stonetore_cords.append(random.choice(coordinates_x))
    stonetore_cords.append(random.choice(coordinates_y))
    stone_cords.append(stonetore_cords)

print("stonetore_finished")
for i in range(int(ironore)-1):
    ironore_cords = []
    ironore_cords.append(random.choice(coordinates_x))
    ironore_cords.append(random.choice(coordinates_y))
    iron_cords.append(ironore_cords)
print("ironore_finished")
for g in range(int(goldore)-1):
    goldore_cords = []
    goldore_cords.append(random.choice(coordinates_x))
    goldore_cords.append(random.choice(coordinates_y))
    gold_cords.append(goldore_cords)
print("goldore_finished")
for d in range(int(diamondore)-1):
    diamondore_cords = []
    diamondore_cords.append(random.choice(coordinates_x))
    diamondore_cords.append(random.choice(coordinates_y))
    diamond_cords.append(diamondore_cords)
print("diamondore_finished")

def check(player_inventory,local_money,player_position,mtime,ptime):
    if player_position not in dirt_cords:
        time.sleep(mtime/ptime)
        dirt_cords.append(player_position)
        player_inventory.append("dirt")
        print("You have mined dirt! You now have " + str(local_money) + " money!")
    elif player_position in stone_cords:
        time.sleep(mtime*1.3/ptime)
        stone_cords.remove(player_position)
        player_inventory.append("stone")
        print("You have mined stone! You now have " + str(local_money) + " money!")
    elif player_position in iron_cords:
        time.sleep(mtime*1.8/ ptime)
        iron_cords.remove(player_position)
        player_inventory.append("iron")
        print("You have mined iron! You now have " + str(local_money) + " money!")
    elif player_position in gold_cords:
        time.sleep(mtime*2.3/ ptime)
        gold_cords.remove(player_position)
        player_inventory.append("gold")
        print("You have mined gold! You now have " + str(local_money) + " money!")
    elif player_position in diamond_cords:
        time.sleep(mtime*3/ ptime)
        diamond_cords.remove(player_position)
        player_inventory.append("diamond")
        print("You have mined diamond! You now have " + str(local_money) + " money!")
    else:
        print("You have mined nothing!")
print("loading..finished")

def main():
    if os.path.isdir('saves') and os.path.isfile('saves/save.owsf'):
        print("loading save")

    local_money = 0
    player_position = [0,0]
    local_miningspeed = 10
    local_tool_lvl = 20
    local_max_mining_time = 10
    player_inventory = []



    print("Welcome to the Ore World!")
    print("You are a miner, and you have to mine ore to Get money!")
    player_position = [0, 0]
    while True:
        print("\nYou have " + str(local_money) + " money!")
        print("you are at"+str(player_position))
        print("1:Mine")
        print("2:Inventory")
        print("3:Goto..")
        print("4:Sell")
        print("5:Exit")

        choice = input("What do you want to do? ")

        if choice == "1":
            if local_tool_lvl > 1:
                ptime = (local_tool_lvl-1)+(local_tool_lvl*2)
            else:
                ptime = 9
            print("\nYou have chosen to mine!")
            check(player_inventory,player_position,local_miningspeed,ptime)
        elif choice == "2":
            print("You have chosen to view your inventory!")
            print(player_inventory)
        elif choice == "3":
            print("You have chosen to go to a new location!")
            gotox = int(input("Where do you want to go? in x axis"))
            gotoy = int(input("Where do you want to go? in y axis"))
            if gotox > 1000 or gotox < -1000 or gotoy > 1000 or gotoy < -1000:
                print("You can't go there!")
            else:
                player_position = [gotox, gotoy]

        elif choice == "4":
            print("You have chosen to sell your ore!")
            while True:
                if "dirt" in player_inventory:
                    player_inventory.remove("dirt")
                    local_money += 3
                    print("You have sold dirt!")
                if "stone" in player_inventory:
                    player_inventory.remove("stone")
                    local_money += 7
                    print("You have sold stone!")
                if "iron" in player_inventory:
                    player_inventory.remove("iron")
                    local_money += 20
                    print("You have sold iron!")
                if "gold" in player_inventory:
                    player_inventory.remove("gold")
                    local_money += 40
                    print("You have sold gold!")
                if "diamond" in player_inventory:
                    player_inventory.remove("diamond")
                    local_money += 100
                    print("You have sold diamond!")
                if "diamond" not in player_inventory and "gold" not in player_inventory and "iron" not in player_inventory and "stone" not in player_inventory and "dirt" not in player_inventory:
                    print("You have sold nothing!")
                    break
        elif choice == "5":
            print("You have chosen to exit!")
            save_choice = input("Do you wanna save the process?(y/n):")
            if save_choice == "y":
                if os.path.isdir('saves') and os.path.isfile('saves/save.owsf'):
                    os.remove('saves/save.owsf')
                    with open("saves/save.owsf", "a") as f:
                        f.write("money:" + str(local_money) + "\n")
                        f.write("position:" + str(player_position) + "\n")
                        f.write("mtime:" + str(local_miningspeed) + "\n")
                        f.write("toollvl:" + str(local_tool_lvl) + "\n")
                        f.write("mxtime" + str(local_max_mining_time) + "\n")
                        f.write("player_inv:" + str(player_inventory))
                        f.close()
                else:
                    os.makedirs('saves')
                    with open("saves/save.owsf", "a") as f:
                        f.write("money:"+str(local_money) + "\n")
                        f.write("position:"+str(player_position) + "\n")
                        f.write("mtime:"+str(local_miningspeed) + "\n")
                        f.write("toollvl:"+str(local_tool_lvl) + "\n")
                        f.write("mxtime"+str(local_max_mining_time) + "\n")
                        f.write("player_inv:"+str(player_inventory))
                        f.close()


                print("Saved!")
            else:
                break

            print("Thanks for playing!!")
            break






if __name__ == "__main__":
    main()
