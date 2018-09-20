def inventory():
    print("This is your inventory.")
    #the spaces of your inventory
    storage = {
        'space_1':"empty",
        'space_2':"empty",
        'space_3':"empty",
        }
    while True:
        items = ["apple","coin","sentient pile of dirt","50 copies of skyrim"]
        print("You can pick up an item or check your inventory.")
        print("You can also increase or decrease your inventory size.")
        print("You can also quit")
        action = input("What do you choose to do?((p)ickup/(c)heck/(q)uit/(e)xpand_inventory): ")

        #picks up an item
        if action == "p":
            print()
            print("There are apples, coins, sentient piles of dirt,and many copies of skyrim in front of you.")
            new_item = input("What do you want to pick up?(apple/coin/dirt/skyrim): ")
            print()    
            print("You pickup %s." %(new_item))
            #checks if a slot is empty and can hold an item
            for key in storage:
                if storage[key] == "empty":
                    storage[key] = new_item
                    break
                
                #need to put this into my code
                    print("----------------------")
                    print("Your inventory is full")
                    print("----------------------")
                    

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

            
        #ends the loop
        elif action == "q":
            print("-------------------------")
            print("You close your inventory.")
            print("-------------------------")
            break
                    

