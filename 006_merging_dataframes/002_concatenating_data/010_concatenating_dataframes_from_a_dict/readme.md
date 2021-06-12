# Concatenating DataFrames from a dict
You're now going to revisit the sales data you worked with earlier in the chapter. Three DataFrames jan, feb, and mar have been pre-loaded for you. Your task is to aggregate the sum of all sales over the 'Company' column into a single DataFrame. You'll do this by constructing a dictionary of these DataFrames and then concatenating them.

# Instructions
- Create a list called month_list consisting of the tuples ('january', jan), ('february', feb), and ('march', mar).
- Create an empty dictionary called month_dict.
- Inside the for loop:
- Group month_data by 'Company' and use .sum() to aggregate.
- Construct a new DataFrame called sales by concatenating the DataFrames stored in month_dict.
- Create an alias for pd.IndexSlice and print all sales by 'Mediacore'. This has been done for you, so hit 'Submit Answer' to see the result!
