def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz.     Press ENTER to start.")
start = int(input("From where you want to start the counting: "))
end = int(input("To where you want to end the counting: "))
nextNumber = start - 1
while nextNumber < end:
    nextNumber += 1
    print(fizz_buzz(nextNumber))
    nextNumber += 1
    correctAns = fizz_buzz(nextNumber)
    playerAns = input("Your turn: ")
    if playerAns != correctAns:
        print(f"You Lose.   The correct answer was {correctAns}.")
        break

else:
    print(f"Congratulations, You reached {nextNumber}.")


