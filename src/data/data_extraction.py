import os
import pandas as pd


def load_data(path):
    """Load all CSV files from the given directory into a single DataFrame."""
    # Get all csv files in the directory
    files = [f for f in os.listdir(path) if f.endswith('.csv')]

    dataframes = []
    for file in files:
        df = pd.read_csv(os.path.join(path, file))
        dataframes.append(df)

    # Concatenate all dataframes
    data = pd.concat(dataframes, ignore_index=True)

    return data
