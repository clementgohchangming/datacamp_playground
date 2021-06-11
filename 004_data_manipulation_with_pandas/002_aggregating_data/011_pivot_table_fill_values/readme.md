# Fill in missing values and sum values with pivot tables

The .pivot_table() method has several useful arguments, including fill_value and margins.

fill_value replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course (Dealing with Missing Data in Python), but the simplest thing to do is to substitute a dummy value.
margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: it gives the row and column totals of the pivot table contents.
In this exercise, you'll practice using these arguments to up your pivot table skills, which will help you crunch numbers more efficiently!

sales is available and pandas is imported as pd.

# Part 1: Instructions
Print the mean weekly_sales by department and type, filling in any missing values with 0.

# Part 2: Instructions
Print the mean weekly_sales by department and type, filling in any missing values with 0 and summing all rows and columns.
