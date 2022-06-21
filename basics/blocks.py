name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}: "))
print(age)

if 18 <= age <= 200:
    print("You are old enough to vote")

elif age <= 800:
    print("Sorry Yoda, but you died in Return of the Jedi")

else:
    print("Please come back in {} years".format(18 - age))
