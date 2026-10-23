#  6. Count the number of passengers in each combination of gender and passenger class.
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.groupby(["Sex", "Pclass"]).size()

print(result)