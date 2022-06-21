strings = "The quick brown fox jumps over the lazy dog"

# sort function modifies a list
# sorted function creates a new list

letters = sorted(strings)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letters = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letters)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"]

names.sort(key=str.casefold)
print(names)
