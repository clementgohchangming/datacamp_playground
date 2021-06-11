# Pivoting on one variable
Pivot tables are the standard way of aggregating data in spreadsheets. In pandas, pivot tables are essentially just another way of performing grouped calculations. That is, the .pivot_table() method is just an alternative to .groupby().

In this exercise, you'll perform calculations using .pivot_table() to replicate the calculations you performed in the last lesson using .groupby().

sales is available and pandas is imported as pd.

# Part 1: Instructions
Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.

# Part 2: Instructions
Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.

# Part 3: Instructions
Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday. 

