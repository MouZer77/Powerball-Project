import pandas as pd
from collections import Counter

df = pd.read_csv("C:\\Users\\idfap\\Documents\\Projects\\Powerball\\Datasets\\pb_winning_numbers_03-18-2017.csv")

df2 = pd.read_csv("C:\\Users\\idfap\\Documents\\Projects\\Powerball\\Datasets\\Powerball_API_2010.csv")

merged_df = df.merge(df2, on=["id"])

# print(df)
# print(df2)
print(merged_df)


most_occurring_numbers = df.mode(axis=0).iloc[0]

# print(most_occurring_numbers)