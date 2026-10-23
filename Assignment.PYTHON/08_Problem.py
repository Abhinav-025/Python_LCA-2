#   8. Find the survival rate of passengers grouped by both gender and embarkation port.

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.groupby(["Sex", "Embarked"])["Survived"].mean() * 100

print(result)