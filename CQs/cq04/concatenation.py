"""1 of 3 files for challenge question 4 comp110"""


def concat(input1: str, input2: str) -> str:
    mergedword = input1 + input2
    return mergedword


word1: str = "happy"
word2: str = "Tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
