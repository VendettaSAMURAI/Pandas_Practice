import pandas as pd
df = pd.read_csv("data.csv")

#tall_pokemon = df[df["Height"]>=2]
#Legendary = df[df["Legendary"] == True]

#Water_pokemon = df([df["Type1"] == "Water"]|
                  # df["Type2"] == "Water")
ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying") ]                 
print(ff_pokemon)