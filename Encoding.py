from sklearn.preprocessing import LabelEncoder


def label_encoder(df):

    le = LabelEncoder()
    df['Subscribed'] = le.fit_transform(df['Subscribed'])
    print(df.head())
    return df




