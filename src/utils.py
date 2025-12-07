import pandas as pd

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    print(f"Dataset loaded: {file_path}")
    return df

def assign_champion(df):
    df['Champion'] = 0
    seasons = df['Season'].unique()
    for season in seasons:
        idx = df[df['Season'] == season]['Points'].idxmax()
        df.at[idx, 'Champion'] = 1
    return df
