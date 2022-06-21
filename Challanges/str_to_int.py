generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# 1st Method:
# replaces the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
# The warning on line 20 is telling that we are changing str to int. In this case, this is exactly what we wanted.
# so, we can ignore it in this case
print(values_list)

# 2nd Method:
integer_list = []
for value in values_list:
    integer_list.append(int(value))
print(integer_list)

# think advantage and disadvantage of the 2 codes