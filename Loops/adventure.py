available_exits = ["north", "west", "east", "south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ").casefold()
    if chosen_exit == "quit":
        print("Game Over")
        break

else:
    print("Aren't you glad you got out of there?")
