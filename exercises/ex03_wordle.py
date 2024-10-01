"""Third exercise for comp110-- wordle mimic"""

__author__ = "730816088"


def input_guess(secret_word_len: int) -> str:
    """function to get user input and find its length"""
    guess = input(f"Enter a {secret_word_len} character word: ")
    guess_length = len(guess)  # local variable to store the length of user input
    while guess_length != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        guess_length = len(guess)
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """function to check if the guessed word is the secret word"""
    assert len(char_guess) == 1  # assumes search_char argument is one character long
    i: int = 0
    while i < len(secret_word):  # while loop to iterate searched_string
        if char_guess == secret_word[i]:
            return True  # returns True value for function and stops the loop
        i += 1
    return False


def emojified(secret_word: str, guessed_word: str) -> str:
    """compare two strings and output emojis indicating matches between them"""
    assert len(guessed_word) == len(
        secret_word
    )  # asserts both words will be same length
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"  # unicodes for emojis
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_output: str = ""
    i: int = 0
    while i < len(secret_word):  # loop to compare secret and inputted word
        if guessed_word[i] == secret_word[i]:
            emoji_output += f"{GREEN_BOX}"  # concating the empty string with emojis
        elif contains_char(secret_word=secret_word, char_guess=guessed_word[i]):
            emoji_output += f"{YELLOW_BOX}"
        else:
            emoji_output += f"{WHITE_BOX}"
        i += 1
    return emoji_output


def main(secret: str) -> None:
    """uses 3 previously defined funcs, compares input to secret word using emojis"""
    """runs game by keeping track of turns and whether player has guessed correctly"""
    turn: int = 1  # variable to keep track of turn
    won_game = False  # variable to determine if player won the game

    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        player_guess = input_guess(
            secret_word_len=len(secret)
        )  # storing player input as a variable
        result = emojified(
            secret_word=secret, guessed_word=player_guess
        )  # storing the emojis as a varible for easier retrieval
        print(result)

        if player_guess == secret:
            won_game = True
        if won_game:  # no need for comparison operator since won_game is a bool
            print(f"You won in {turn}/6 turns!")
            turn = 10  # make turn 10 to end the loop once player wins
        else:
            turn += (
                1  # increases player turn by one if they did not win on previous turn
            )

    if (turn > 6) and (
        turn != 10
    ):  # if statement that runs of player runs out of turns
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")  # defines secret word "codes" (can be any word of any length)
