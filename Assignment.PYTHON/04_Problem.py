# 4.Find the average age and average fare of passengers grouped by gender.

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.groupby("Sex").agg(
    Average_Age=("Age", "mean"),
    Average_Fare=("Fare", "mean")
)

print(result.round(2))
