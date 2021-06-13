# Appending DataFrames with ignore_index
In this exercise, you'll use the Baby Names Dataset (from data.gov) again. This time, both DataFrames names_1981 and names_1881 are loaded without specifying an Index column (so the default Indexes for both are RangeIndexes).

You'll use the DataFrame .append() method to make a DataFrame combined_names. To distinguish rows from the original two DataFrames, you'll add a 'year' column to each with the year (1881 or 1981 in this case). In addition, you'll specify ignore_index=True so that the index values are not used along the concatenation axis. The resulting axis will instead be labeled 0, 1, ..., n-1, which is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information.

# Instructions
- Create a 'year' column in the DataFrames names_1881 and names_1981, with values of 1881 and 1981 respectively. Recall that assigning a scalar value to a DataFrame column broadcasts that value throughout.
- Create a new DataFrame called combined_names by appending the rows of names_1981 underneath the rows of names_1881. Specify the keyword argument ignore_index=True to make a new RangeIndex of unique integers for each row.
- Print the shapes of all three DataFrames. This has been done for you.
- Extract all rows from combined_names that have the name 'Morgan'. To do this, use the .loc[] accessor with an appropriate filter. The relevant column of combined_names here is 'name'.
