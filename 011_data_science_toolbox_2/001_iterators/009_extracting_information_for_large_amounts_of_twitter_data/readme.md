# Extracting information for large amounts of Twitter data
Great job chunking out that file in the previous exercise. You now know how to deal with situations where you need to process a very large file and that's a very useful skill to have!

It's good to know how to process a file in smaller, more manageable chunks, but it can become very tedious having to write and rewrite the same code for the same task each time. In this exercise, you will be making your code more reusable by putting your work in the last exercise in a function definition.

The pandas package has been imported as pd and the file 'tweets.csv' is in your current directory for your use.

# Instructions
- Define the function count_entries(), which has 3 parameters. The first parameter is csv_file for the filename, the second is c_size for the chunk size, and the last is colname for the column name.
- Iterate over the file in csv_file file by using a for loop. Use the loop variable chunk and iterate over the call to pd.read_csv(), passing c_size to chunksize.
- In the inner loop, iterate over the column given by colname in chunk by using a for loop. Use the loop variable entry.
- Call the count_entries() function by passing to it the filename 'tweets.csv', the size of chunks 10, and the name of the column to count, 'lang'. Assign the result of the call to the variable result_counts.

