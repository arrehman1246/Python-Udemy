if 0:
    print("True")
else:
    print("False")

print("-" * 80)

name = input("Please enter your name: ")

# if name:    -OR-    "" means empty STRING
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
