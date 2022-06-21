# Write a program to ask for a name and age.
# When both values have been entered, check if the person is the right age to go ..
# ...on an 18-30 holiday (they must be over 18 and under 31).
# If theyare welcome, welcome them to the hoilday, otherwise print a (polite) ....
# ...message refusing them entry.

name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}? "))

if 18 <= age < 31:
    print(f"Enjoy your holidays, {name}")

else:
    print(f"Sorry {name} but our holidays are only for cool people.")
