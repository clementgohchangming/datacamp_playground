# Counting categorical variables
Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. In this exercise, you'll count the number of each type of store and the number of each department number using the DataFrames you created in the previous exercise:

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
The store_types and store_depts DataFrames you created in the last exercise are available, and pandas is imported as pd.

# Instructions
- Count the number of stores of each store type in store_types.
- Count the proportion of stores of each store type in store_types.
- Count the number of different departments in store_depts, sorting the counts in descending order.
- Count the proportion of different departments in store_depts, sorting the proportions in descending order.

