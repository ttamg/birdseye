import random

import birdseye.trace_module_deep


def roll_the_dice(rolls: int, sides: int = 6) -> tuple:
    """
    This is a function where we roll a number of dice.
    Parameters:
    - rolls (int) - the number of dice to roll
    - sides (int) - the number of sides on the dice (default = 6)
    Returns a tuple of:
    - total score on all dice
    - a list of the dice rolls
    """

    results = []
    for _ in range(rolls):
        results.append(roll(sides))

    return (sum(results), results)


def roll(sides: int = 6) -> int:
    """
    An individual die roll.
    Parameters:
    - sides (int) - the number of sides on the dice (default = 6)
    Returns:
    - the value of the die roll
    """
    return random.randint(1, sides)


def main():
    """ Demo example to run """

    rolls = 2
    sides = 6
    result = roll_the_dice(rolls=rolls, sides=sides)
    return result


if __name__ == "__main__":
    import os

    print("Using environment variables ...")
    print(os.environ.get("BIRDSEYE_DB"))
    print(os.environ.get("JOB_NAME"))

    main()
