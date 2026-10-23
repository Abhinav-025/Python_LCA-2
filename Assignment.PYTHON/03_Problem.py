# 3. Calculate the survival rate for each passenger class and display the results in descending order of survival rate.

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.groupby("Pclass")["Survived"].mean() * 100

result = result.sort_values(ascending=False)

print(result.round(2))
