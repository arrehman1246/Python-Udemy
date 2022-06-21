parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print(f"{letter} is in {parrot}.")

else:
    print("I don't need that letter")