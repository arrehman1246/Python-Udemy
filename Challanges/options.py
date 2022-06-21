choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose an option from the list below:")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo Swimming")
        print("4.\tHave Dinner")
        print("5.\tGo to bed")
        print("0.\tExit")

    choice = input("Please choose an option: ")
