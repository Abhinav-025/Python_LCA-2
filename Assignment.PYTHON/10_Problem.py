#  10. Calculate the total number of passengers, number of survivors, and survival percentage for each passenger class.

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.groupby("Pclass").agg(
    Total_Passengers=("Survived", "count"),
    Survivors=("Survived", "sum"),
    Survival_Percentage=("Survived", "mean")
)

result["Survival_Percentage"] = result["Survival_Percentage"] * 100

print(result)