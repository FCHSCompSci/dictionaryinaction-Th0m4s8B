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
        print("You can also quit")
        action = input("What do you choose to do?(pickup/check/quit): ")

        #picks up an item
        if action == "pickup":
            print("There is an apple, a coin, a sentient pile of dirt,and 50 copies of skyrim in front of you.")
            new_item = input("What do you want to pick up?(apple/coin/dirt/skyrim): ")
            print("You pickup %s." %(new_item))
            #checks if a slot is empty and can hold an item
            if storage['space_1'] == "empty":
                storage['space_1'] = new_item
            else:
                if storage['space_2'] == "empty":
                    storage['space_2'] = new_item
                else:
                    if storage['space_3'] == "empty":
                        storage['space_3'] = new_item

                        
        #shows the inventory    
        elif action == "check":
            print(storage)


        #ends the loop
        elif action == "quit":
            print("You close your inventory.")
            break
                    
