# Slicing MultiIndexed DataFrames
This exercise picks up where the last ended (again using The Guardian's Olympic medal dataset).

You are provided with the MultiIndexed DataFrame as produced at the end of the preceding exercise. Your task is to sort the DataFrame and to use the pd.IndexSlice to extract specific slices. Check out this exercise from Manipulating DataFrames with pandas to refresh your memory on how to deal with MultiIndexed DataFrames.

pandas has been imported for you as pd and the DataFrame medals is already in your namespace.

# Instructions
- Create a new DataFrame medals_sorted with the entries of medals sorted. Use .sort_index(level=0) to ensure the Index is sorted suitably.
- Print the number of bronze medals won by Germany and all of the silver medal data. This has been done for you.
- Create an alias for pd.IndexSlice called idx. A slicer pd.IndexSlice is required when slicing on the inner level of a MultiIndex.
- Slice all the data on medals won by the United Kingdom in the DataFrame medals_sorted. To do this, use the .loc[] accessor with idx[:,'United Kingdom'], :.
