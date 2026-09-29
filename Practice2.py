import pandas as pd
data = [100,400,300,200,202]
series = pd.Series(data,index=["a","b","c","d","e"])
print(series.loc[series<=200])