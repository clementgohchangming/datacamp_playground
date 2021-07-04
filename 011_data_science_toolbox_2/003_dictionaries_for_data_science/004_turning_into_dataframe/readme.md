# Turning this all into a DataFrame
You've zipped lists together, created a function to house your code, and even used the function in a list comprehension to generate a list of dictionaries. That was a lot of work and you did a great job!

You will now use all of these to convert the list of dictionaries into a pandas DataFrame. You will see how convenient it is to generate a DataFrame from dictionaries with the DataFrame() function from the pandas package.

The lists2dict() function, feature_names list, and row_lists list have been preloaded for this exercise.

Go for it!

# Instructions
- To use the DataFrame() function you need, first import the pandas package with the alias pd.
- Create a DataFrame from the list of dictionaries in list_of_dicts by calling pd.DataFrame(). Assign the resulting DataFrame to df.
- Inspect the contents of df printing the head of the DataFrame. Head of the DataFrame df can be accessed by calling df.head().

