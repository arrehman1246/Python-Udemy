import random

highest = 20
answer = random.randint(1, highest)
print(answer)  # TODO : REMOVE IT AFTER TESTING

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("Well done! You got it first time")

while guess != answer:
    if guess == 0:
        print("You Quit")
        break
    if guess > answer:
        print("Please guess lower")
    # guess must be lower than answer
    else:
        print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done! you guessed it")
        break
