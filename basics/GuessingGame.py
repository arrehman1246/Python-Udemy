answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess > answer:
        print("Please guess lower")
    else:  #guess must be lower than answer
        print("Please guess higher")
    guess=int(input())
    if guess == answer:
        print("Well done! you guessed it")
    else:
        print("Sorry, you have not guessed correctly.\nPlease try again.")

else:
    print("You got it first time")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done! you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done! you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

# else:
#     print("You got it first time")
