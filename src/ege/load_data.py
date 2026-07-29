import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

print(DATA_DIR)

# # df = data frame
# df = pd.read_csv("Connectome.csv")

# df.head(x)