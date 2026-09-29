import pandas as pd
df = pd.read_csv("data.csv",index_col="Name")
#print(df["Height"].to_string())
print(df.loc["Pikachu",["Height","Weight"]])