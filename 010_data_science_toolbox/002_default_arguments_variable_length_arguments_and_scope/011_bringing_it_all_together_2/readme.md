# Bringing it all together (2)
Wow, you've just generalized your Twitter language analysis that you did in the previous chapter to include a default argument for the column name. You're now going to generalize this function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided.

# Instructions
- Complete the function header by supplying the parameter for the dataframe df and the flexible argument *args.
- Complete the for loop within the function definition so that the loop occurs over the tuple args.
- Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the result to result1.
- Call count_entries() by passing the tweets_df DataFrame and the column names 'lang' and 'source'. Assign the result to result2. 
