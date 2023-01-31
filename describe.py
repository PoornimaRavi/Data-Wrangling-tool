import pandas as pd
import numpy as np


def describe(filename):
    df = pd.read_excel(filename)
    print(df.describe())
    return df
