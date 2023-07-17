# Takes a pandas DataFrame df as input and returns a new DataFrame where all the columns are 
# converted to string data type. This can be useful for preprocessing steps in data analysis 
# where you want to ensure all data is in a uniform text format.
import pandas as pd

def astype_str_all_cols(df: pd.DataFrame) -> pd.DataFrame:
    return df.astype({col: str for col in df.columns})