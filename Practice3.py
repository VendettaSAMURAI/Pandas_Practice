import pandas as pd
numbers = {
    "apple": 45,
    "banana": 78,
    "orange": 12,
    "mango": 91,
    "grape": 33
}

series = pd.Series(numbers)
series.loc["apple"] += 100
print(series)