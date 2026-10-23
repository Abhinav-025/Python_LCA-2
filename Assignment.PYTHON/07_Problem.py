#  7.  the number of missing values in each column and display only the columns containing missing values.
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])

