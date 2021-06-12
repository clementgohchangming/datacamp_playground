# Reading multiple files to build a DataFrame
It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.

Here, you'll work with DataFrames compiled from The Guardian's Olympic medal dataset.

pandas has been imported as pd and the list medal_types has been pre-loaded for you, which contains the strings 'bronze', 'silver', and 'gold'.

# Instructions
- Iterate over medal_types in the for loop.
- Inside the for loop:
- Create file_name using string interpolation with the loop variable medal. This has been done for you. The expression "%s_top5.csv" % medal evaluates as a string with the value of medal replacing %s in the format string.
- Create the list of column names called columns. This has been done for you.
- Read file_name into a DataFrame called medal_df. Specify the keyword arguments header=0, index_col='Country', and names=columns to get the correct row and column Indexes.
- Append medal_df to medals using the list .append() method.
