import pandas as pd
from pathlib import Path

# gets data folder (without having to use a local path like ../data)
DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data"

# -> pd.DataFrame specifies the return type of this function
# like -> int
def load_connectome() -> pd.DataFrame:
    file_path = DATA_DIRECTORY / "Connectome.csv"
    
    # read the unnamed column as the index (to get rid of the unnamed column)
    df = pd.read_csv(file_path, index_col=0)
    return df

df_connectome = load_connectome()

print(df_connectome)