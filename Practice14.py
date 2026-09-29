import pandas as pd



# Data Cleaning
df = pd.read_csv("data.csv")


#1 Drop irrelevant Data
#df = df.drop(columns=["Legendary","No"])

#2 Handle Missing data 
#df = df.dropna(subset=['Type2'])
#df = df.fillna({'Type2':"None"})

#3 Fix inconsistent value
#df["Type1"] = df["Type1"].replace({"Grass":"GRASS",
                                  # "Fire":"FIRE",
                                  # "Water":"WATER"})

#4 Standardize text
#df["Name"] = df["Name"].str.lower()

#5 Fix data types
#df["Legendary"] = df["Legendary"].astype(bool)

#6 Remove Duplicate values
df = df.drop_duplicates()

print(df.to_string())



