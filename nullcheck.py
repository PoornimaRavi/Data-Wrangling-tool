import numpy as np


def drop_nan_values(dataframe):
    nan_in_df = dataframe.isnull().sum().any()
    if nan_in_df == True:
        print("Null values are present in Data")
        df = dataframe.dropna()
        return df
    else:
        print("No Null values present in Data")
        return dataframe

