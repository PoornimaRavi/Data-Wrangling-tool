import pandas as pd


def read_excel_file(filename):
    df = pd.read_excel(filename)
    print(df.head())
    return df
