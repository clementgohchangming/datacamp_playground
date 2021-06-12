# Concatenating pandas Series along row axis
Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead. You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have been pre-loaded.

Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to .append().

You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as you'll see in later exercises.

# Instructions
- Create an empty list called units. This has been done for you.
- Use a for loop to iterate over [jan, feb, mar]:
- In each iteration of the loop, append the 'Units' column of each DataFrame to units.
- Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
- Specify the keyword argument axis='rows' to stack the Series vertically.
- Verify that quarter1 has the individual Series stacked vertically by printing slices. This has been done for you, so hit 'Submit Answer' to see the result!
