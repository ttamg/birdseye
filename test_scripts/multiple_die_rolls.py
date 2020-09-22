import os

# Environment variables set here when imported
os.environ["BIRDSEYE_DB"] = "/Users/matt/Projects/birdseye/.bird.sqlite"
os.environ["BIRDSEYE_JOB"] = "Alpha test"
os.environ["BIRDSEYE_ENABLED"] = "True"

from birdseye import eye
from test_scripts.die_roll import roll_the_dice


@eye(enabled=os.environ["BIRDSEYE_ENABLED"])
def main():
    """ Demo example to run """

    rolls = 10
    sides = 6
    result1 = roll_the_dice(rolls=rolls, sides=sides)

    rolls = 3
    sides = 20
    result2 = roll_the_dice(rolls=rolls, sides=sides)

    return result1, result2


if __name__ == "__main__":
    import os

    print("Using environment variables ...")
    print(os.environ.get("BIRDSEYE_ENABLED"))
    print(os.environ.get("BIRDSEYE_DB"))
    print(os.environ.get("BIRDSEYE_JOB"))

    main()
