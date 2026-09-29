import pandas as pd
df = pd.read_csv("data.csv",index_col="Name")
#print(df["Height"].to_string())
print(df.iloc[0:11:2, 0:3])