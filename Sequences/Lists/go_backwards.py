# SIMPLER THAN OUTLIERS.PY

# when we remove items in a list using forward index, it changes the index position
# but, if we go backward and remove index 10, index from 0 to 9 won't be affected
data = [104, 101, 5, 105, 308, 103, 5,
        107, 100, 306, 185, 102, 108]

min_valid = 100
max_valid = 200

# -OK-

# for index in range(len(data) - 1, -1, -1):
#     if data[index] > max_valid or data[index] < min_valid:
#         print(index, data)
#         del data[index]

# --ANOTHER METHOD--
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value > max_valid or value < min_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)
