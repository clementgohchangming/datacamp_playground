# Writing a generator to load data in chunks (3)
Great! You've just created a generator function that you can use to help you process large files.

Now let's use your generator function to process the World Bank dataset like you did previously. You will process the file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset. For this exercise, however, you won't process just 1000 rows of data, you'll process the entire dataset!

The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and ready for your use. Go for it!

# Instructions
- Bind the file 'world_dev_ind.csv' to file in the context manager with open().
- Complete the for loop so that it iterates over the generator from the call to read_large_file() to process all the rows of the file.
