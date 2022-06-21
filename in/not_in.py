activity = input("What would you like to do today? ")

# casefold turns letters into lowercase
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
