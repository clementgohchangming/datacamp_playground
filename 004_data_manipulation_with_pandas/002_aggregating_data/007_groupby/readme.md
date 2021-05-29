# What percent of sales occurred at each store type?
While .groupby() is useful, you can calculate grouped summary statistics without it.

Walmart distinguishes three types of stores: "supercenters," "discount stores," and "neighborhood markets," encoded in this dataset as type "A," "B," and "C." In this exercise, you'll calculate the total sales made at each store type, without using .groupby(). You can then use these numbers to see what proportion of Walmart's total sales were made at each type.

sales is available and pandas is imported as pd

# Instructions

- Calculate the total weekly_sales over the whole dataset.
- Subset for type "A" stores, and calculate their total weekly sales.
- Do the same for type "B" and type "C" stores.
- Combine the A/B/C results into a list, and divide by sales_all to get the proportion of sales by type.
