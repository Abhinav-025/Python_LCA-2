#  1. Fetch all female passengers who survived and were older than 30 years. Display Name, Age, Fare, and Pclass.

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df[
    (df["Sex"] == "female") &
    (df["Survived"] == 1) &
    (df["Age"] > 30)
]

print(result[["Name", "Age", "Fare", "Pclass"]])
