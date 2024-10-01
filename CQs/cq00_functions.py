"""first challenge question for comp110"""

__author__ = "730816088"


def mimic(message: str) -> str:
    """repeats whatever is inputed"""
    return message


def main() -> None:
    "prints the output of the mimic function"
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
