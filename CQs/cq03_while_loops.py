"""challenge question using while loops on strings"""

__author__ = "730816088"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    i = 0
    while i < len(phrase):
        if search_char == phrase[i]:
            count += 1
            i += 1
        else:
            i += 1

    return count


print(num_instances(phrase="eeee", search_char="e"))
