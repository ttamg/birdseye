import os
import random

# Environment variables set here when imported
os.environ["BIRDSEYE_DB"] = "/Users/matt/Projects/birdseye/.bird.sqlite"
os.environ["BIRDSEYE_JOB"] = "My pandas job"
os.environ["BIRDSEYE_ENABLED"] = "True"

from birdseye import eye
import pandas as pd


@eye(enabled=os.environ["BIRDSEYE_ENABLED"])
def get_dataframe(data: list):
    """ Creates a new dataframe """
    df = pd.DataFrame(data)
    return df


@eye(enabled=os.environ["BIRDSEYE_ENABLED"])
def modify_dataframe(df: pd.DataFrame, modifier: int):
    """ Adds a number to a dataframe """
    df2 = df.copy()
    for column in ["2", "6", "9"]:
        df2[column] = df2[column] + modifier
    return df2


@eye(enabled=os.environ["BIRDSEYE_ENABLED"])
def main():
    """ Pandas example """

    dummy_data = [
        {str(a): random.randint(0, 100) for a in range(10)} for x in range(20)
    ]
    df = get_dataframe(data=dummy_data)

    df2 = modify_dataframe(df=df, modifier=7)

    return df, df2


if __name__ == "__main__":
    import os

    print("Using environment variables ...")
    print(os.environ.get("BIRDSEYE_ENABLED"))
    print(os.environ.get("BIRDSEYE_DB"))
    print(os.environ.get("BIRDSEYE_JOB"))

    df, df2 = main()
