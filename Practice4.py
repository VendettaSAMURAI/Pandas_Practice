import pandas as pd
data = {
    "employee": ["Rahul", "Anna", "David"],
    "age": [24, 31, 28,]
}

df = pd.DataFrame(data, index=["Employee1","Employee2","Employee3",])

print(df)