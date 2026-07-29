import pandas as pd
from pathlib import Path

# gets data folder (without having to use a local path like ../data)
DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data"

# -> pd.DataFrame specifies the return type of this function
# like -> int
def load_connectome() -> pd.DataFrame:
    file_path = DATA_DIRECTORY / "Connectome.csv"
    df = pd.read_csv(file_path)
    remove_unnamed_columns(df)
    return df

def remove_unnamed_columns(df) -> pd.DataFrame:    
    new_df = df.drop(df.columns[df.columns.str.contains(
        'Unnamed', case=False)], axis=1, inplace=True)
    return new_df

df_connectome = load_connectome()

print(df_connectome)