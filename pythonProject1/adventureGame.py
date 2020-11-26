while True:
    answer = input("Would you like to play? yes/no").lower().strip()

    if answer == "yes":
        answer = input("You have reached a crossroad, would you like to go left or right").lower().strip()
        if answer == "left":
            answer = input("You have stimbled into a room and encounter a monster, would you like to stay and fight it or run into the next room? stay/run").lower().strip()
            if answer == "stay":
                print("The monster kills you. YOU LOSE")

            elif answer == "move":
                print("You stumble upon tons of treasure, YOU WIN")

            else:
                print("invalid option")
        

        elif answer == "right":
            answer = input("You enter a room and encounter a group of females in a pool, would you like to join them or move on to the next room? join/move").lower().strip()
            if answer == "join":
                print("The femals turn out to be witches and they eat you alive. YOU LOSE")

            elif answer == "move":
                print("You stumble upon tons of treasure, YOU WIN")

            else:
                print("invalid option")


        else:
            print("Invalid choice")




    else:
        print("Thats too bad")
        break
