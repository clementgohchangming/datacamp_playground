# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for country, row in cars.iterrows():
    cars.loc[country, "COUNTRY"] = cars.loc[country, "country"].upper()

# Print cars
print(cars)
