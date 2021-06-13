# Subsetting rows with .query()
In this exercise, you will revisit GDP and population data for Australia and Sweden from the World Bank and expand on it using the .query() method. You'll merge the two tables and compute the GDP per capita. Afterwards, you'll use the .query() method to sub-select the rows and create a plot. Recall that you will need to merge on multiple columns in the proper order.

The tables gdp and pop have been loaded for you.

# Instructions

# Part 1:
Use merge_ordered() on gdp and pop on columns country and date with the fill feature, save to gdp_pop and print.

# Part 2:
Add a column named gdp_per_capita to gdp_pop that divides gdp by pop.

# Part 3:
Pivot gdp_pop so values='gdp_per_capita', index='date', and columns='country', save as gdp_pivot.

# Part 4:
Use .query() to select rows from gdp_pivot where date is greater than equal to 1991-01-01". Save as recent_gdp_pop.
