

import pandas as pd

def calculate_statistics(df):
    numeric_df = df.select_dtypes(include='number')
    stats = {
        'mean': numeric_df.mean(),
        'median': numeric_df.median(),
        'mode': numeric_df.mode().iloc[0],
        'std_dev': numeric_df.std(),
        'correlation': numeric_df.corr()
    }
    return stats
