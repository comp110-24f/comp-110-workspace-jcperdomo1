"""challenge question 02 for comp110, practice with conditionals"""

__author__ = "730816088"


def guess_a_number() -> None:
    secret: int = 7
    guess = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is 7")
    elif guess > secret:
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
