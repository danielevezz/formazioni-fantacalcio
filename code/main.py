import pandas as pd
from Parser import Parser 

parser = Parser("team.csv")

players = parser.parse()

df = pd.DataFrame.from_records(p.to_dict() for p in players)
df["cost"] = df["cost"].apply(pd.to_numeric)

print(df.sort_values("cost", ascending=False))


