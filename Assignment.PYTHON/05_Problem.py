# 5. Fetch passengers who were travelling with at least two siblings or spouses and at least one parent or child.

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df[
    (df["SibSp"] >= 2) &
    (df["Parch"] >= 1)
]

print(result)
