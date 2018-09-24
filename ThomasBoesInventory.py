#Thomas Boes, Dictionary Project, 9/24/18

def inventory():
    print("You open your inventory.")
    #the spaces of your inventory
    storage = {
        'space_1':"empty",
        'space_2':"empty",
        'space_3':"empty",
        }
    while True:
        storage_count = range(1,(len(storage)+1))
        for num in storage_count:
            space_num = num
        print("You can pick up an item or check your inventory.")
        print("You can also increase or decrease your inventory size.")
        print("You can also quit")
        action = input("What do you choose to do?((p)ickup/(c)heck/(q)uit/(e)xpand_inventory/(d)ecrease_inventory): ")

        #picks up an item
        if action == "p":
            print()
            print("There are apples, coins, sentient piles of dirt,and many copies of skyrim in front of you.")
            new_item = input("What do you choose to pick up?(apple/coin/dirt/skyrim): ")
            print()    
            #checks if a slot is empty and can hold an item
            for key in storage:
                if storage[key] == "empty":
                    storage[key] = new_item
                    print("You pickup %s." %(new_item))
                    print()
                    break
            if storage['space_%s'%space_num] != "empty":
                print("-----------------------")
                print("Your inventory is full.")
                print("-----------------------")
                    

        #shows the inventory    
        elif action == "c":
            for key, value in storage.items():
                print()
                print("%s: %s" % (key, value))
            print()
            
        #increases number of inventory spaces
        elif action == "e":
            storage['space_%s'%(len(storage)+1)] = "empty"
            print("--------------------------------------")
            print("Your inventory has gained a new space.")
            print("--------------------------------------")

        #decreases number of inventory spaces
        elif action == "d":
            print("!!!WARNING!!!")
            print("This will delete the last inventory space forever.")
            delete = input("Do you wish to continue?(y/n): ")
            if delete == "y":
                del storage['space_%s'%len(storage)]
                print("--------------------------------")
                print("Your inventory has lost a space.")
                print("--------------------------------")

            
        #ends the main loop
        elif action == "q":
            print("-------------------------")
            print("You close your inventory.")
            print("-------------------------")
            break
                    

