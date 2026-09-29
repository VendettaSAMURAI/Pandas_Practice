import pandas as pd
df = pd.read_csv("data.csv")

#print(df.mean(numeric_only=True))
#print(df.count())
#print(df["Height"].mean())

group = df.groupby ("Type1")
#print(group["Height"].mean())
#print(group["Height"].sum())
#print(group["Height"].min())
#print(group["Height"].max())