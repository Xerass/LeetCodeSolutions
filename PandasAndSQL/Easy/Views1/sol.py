import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_viewed = views[views["author_id"] == views["viewer_id"]]["author_id"].unique()
    return pd.DataFrame({"id": self_viewed}).sort_values("id").reset_index(drop=True)
