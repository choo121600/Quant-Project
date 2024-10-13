import pandas as pd
import os

def save_to_csv(df: pd.DataFrame, filename: str, processed_dir: str = 'data/processed/') -> None:
    """

    :param df:
    :param filename:
    :param processed_dir:
    :return:
    """

    os.makedirs(processed_dir, exist_ok=True)
    filepath = os.path.join(processed_dir, filename)
    df.to_csv(filepath)
