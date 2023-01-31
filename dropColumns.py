
def drop_columns(dataframe):
    df = dataframe.drop(dataframe.columns[[2]], axis=1)
    print(df.head())
    return df

