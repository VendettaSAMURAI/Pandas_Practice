import pandas as pd
df = pd.read_csv("data.csv")
#print(df["Height"].to_string())
print(df.loc[0])