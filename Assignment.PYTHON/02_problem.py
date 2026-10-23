#  2. Display the top 10 passengers who paid the highest fares. Show Name, Fare, and Pclass.


import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.sort_values(
    by="Fare", ascending=False
).head(10)

print(result[["Name", "Fare", "Pclass"]])

