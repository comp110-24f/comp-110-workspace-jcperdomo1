"""Exercise 2 for comp110, chardle game/wordle mimic"""

__author__ = "730816088"


def input_word() -> str:
    """function to take player input for a five letter word"""
    player_input = input("Enter a 5-character word: ")
    if len(player_input) == 5:
        return player_input
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """function to take letter input to compare to the 5 letter word"""
    letter_input = input("Enter a single character: ")
    if len(letter_input) == 1:
        return letter_input
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """function to compare the the letter and word inputs"""
    count = 0

    print("Searching for " + letter + " in " + word)
    """list of conditionals to find index placement of words"""

    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if (
        (word[0] != letter)
        and (word[1] != letter)
        and (word[2] != letter)
        and (word[3] != letter)
        and (word[4] != letter)
    ):
        print("No instances of " + letter + " found in " + word)
        """if statement to display the number of instances a letter appears"""

    if count == 1:
        print("1 instance found of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances found of " + letter + " found in " + word)
    return None


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    return None


if __name__ == "__main__":
    main()
