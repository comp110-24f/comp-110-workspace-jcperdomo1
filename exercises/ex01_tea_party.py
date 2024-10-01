"""Exercise 01 for Comp110"""

__author__ = "730816088"


def tea_bags(people: int) -> int:
    """function to calculate tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """function to calculate the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """function to calculate the cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """function to plan each aspect of the tea party"""
    print("A cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
