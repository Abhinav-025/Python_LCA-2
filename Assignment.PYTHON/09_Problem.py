# 9. Fetch passengers whose fares are greater than the average fare of the entire dataset. Display their names, fares, and passenger classes.
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

avg_fare = df["Fare"].mean()

result = df[df["Fare"] > avg_fare][["Name", "Fare", "Pclass"]]

print(result)