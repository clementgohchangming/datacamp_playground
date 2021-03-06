# Concatenating DataFrames with inner join
Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset.

The DataFrames bronze, silver, and gold have been pre-loaded for you.

Your task is to compute an inner join.

# Instructions
- Construct a list of DataFrames called medal_list with entries bronze, silver, and gold.
- Concatenate medal_list horizontally with an inner join to create medals.
- Use the keyword argument keys=['bronze', 'silver', 'gold'] to yield suitable hierarchical indexing.
- Use axis=1 to get horizontal concatenation.
- Use join='inner' to keep only rows that share common index labels.
- Print the new DataFrame medals.

