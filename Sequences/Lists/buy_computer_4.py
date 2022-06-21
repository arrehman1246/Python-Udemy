available_parts = ["computer",
                   "monitor",
                   "cpu",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
computer_parts = []   # create an empty list.

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append(chosen_part)
            print("Adding {}".format(current_choice))
        print("Your list now contains {}".format(computer_parts))

    else:
        print("Please choose options from the list")
        #   enumerate function:
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")

    current_choice = input()

print(f"Your final list is: {computer_parts}")
