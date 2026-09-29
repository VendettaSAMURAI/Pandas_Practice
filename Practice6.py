import pandas as pd
data = {
    "employee": ["Rahul", "Anna", "David"],
    "age": [24, 31, 28,]
}

df = pd.DataFrame(data, index=["Employee1","Employee2","Employee3",])
# New column
df["Job"] = ["SWE","Data_analyst","Pipeline_manager"]
# New Row
new_row = pd.DataFrame([{"employee": "Sandy","age":45,"Job":"CFO"},
                    {"employee": "Eugene","age":60,"Job":"Manager"}],
                       index=["Employee4","Employee5"])
df = pd.concat([df,new_row])
print(df)