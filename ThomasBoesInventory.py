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

        
        if action == "pickup":
            print("There is a %s in front of you." %s(items[0]))
            input("What do you want to pick up?(%s): " %s(items[0]))

            
        elif action == "check":
            break

        
        elif action == "quit":
            print("You close your inventory.")
            break
                    
