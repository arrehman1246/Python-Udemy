even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)

# sort function modifies a list
# sorted function creates a new list

even.sort()
print(even)

even.sort(reverse=True)
print(even)
