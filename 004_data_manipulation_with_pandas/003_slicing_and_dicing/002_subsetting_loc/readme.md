# Subsetting with .loc[]
The killer feature for indexes is .loc[]: a subsetting method that accepts index values. When you pass it a single argument, it will take a subset of rows.

The code for subsetting using .loc[] can be easier to read than standard square bracket subsetting, which can make your code less burdensome to maintain.

pandas is loaded as pd. temperatures and temperatures_ind are available; the latter is indexed by city.

# Instructions
- Create a list called cities that contains "Moscow" and "Saint Petersburg".
- Use [] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
- Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.
