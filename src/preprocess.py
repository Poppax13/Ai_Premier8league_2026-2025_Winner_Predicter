from sklearn.preprocessing import LabelEncoder

def encode_teams(df):
    le = LabelEncoder()
    df['TeamEnc'] = le.fit_transform(df['Team'])
    return df, le
