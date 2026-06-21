import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    condition = (cinema["id"] % 2 == 1) & (cinema["description"] != "boring")
    df = cinema[condition].sort_values(ascending = False, by = "rating")
    return df
