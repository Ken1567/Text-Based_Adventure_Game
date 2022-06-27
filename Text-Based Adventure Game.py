import time

print("\nWelcome to the World of Choices!")
time.sleep(2)
print("\nWhere every action has a consequence.....")
time.sleep(3)

name = input("\nWhat is your name? ")
age = int(input("\nHow old are you?? "))

health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("\nDo you want to play? ").lower()

    if (wants_to_play == "yes") or (wants_to_play == "y"):
        print("Starting...\n")
        time.sleep(1)  # Adding delays for extra effects
        print("Please wait!")
        time.sleep(1)
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1

        print(f"\nYou are staring with {health} health, {name}.")
        print("Let's play!\n")

        time.sleep(2)

        left_or_right = input(f"""First choice, {name}. Left or Right? It is so sudden, I know. Not that you have a choice anyway.
        \nType your choice: """)
        if left_or_right == "left":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

            ans = input(f"""\nGood choice, {name}. You follow a path which leads you to a lake. Do you swim across or go around?
            \nType your choice: across or around?\n""")

            if ans == "around":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print(f"\nYou went around and reached the other side of the lake. Almost there, {name}")
            elif ans == "across":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print(f"\nYou managed to get across, but was bitten by a strange fish. Poor choice, {name}.")
                print("You lose 5 health.")
                health -= 5

            ans = input(f"""\nYou notice a house and a river. Which do you go to, {name}?
            \nType your choice: river or house?\n""")
            if ans == "house":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nYou go to the house and is greeted by the owner. He offered you some food. You ate it but soon realized that it was poisoned. You immediately ran away from the house")
                print(f"\nYou lose 5 health. Poor choice, {name}.")
                health -= 5

                if health <= 0:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1

                    print(f"\nYou now have 0 health and you lost the game. Such is life, my dear {name} :(")
                else:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1
                        
                    print("\nA group of villagers found you lying under a tree half dead. They carried you to their village and cured your poison.") 
                    print("""\nYou have survived...for now... You win!
                    \nThanks for playing!""")

            else:
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nYou fell in the river and died. You thought it was shallow but man it was' too deep, even the fish could see Adele rollin!")
                time.sleep(2/5)
                print(f"Better luck next time, {name} :P")

        else:
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

            print(f"\nYou entered a jungle and got eaten by a bear. You died too early. RIP {name}.")

    else:
        print("\nExiting...")
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1
        print()

else:
    print("\nYou are not old enough to play...")
    print("\nExiting...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()
