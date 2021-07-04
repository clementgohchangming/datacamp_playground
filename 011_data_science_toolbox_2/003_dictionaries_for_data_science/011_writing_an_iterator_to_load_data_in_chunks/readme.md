# Writing an iterator to load data in chunks (4)
In the previous exercises, you've only processed the data from the first DataFrame chunk. This time, you will aggregate the results over all the DataFrame chunks in the dataset. This basically means you will be processing the entire dataset now. This is neat because you're going to be able to process the entire large dataset by just working on smaller pieces of it!

You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use.

# Instructions
- Initialize an empty DataFrame data using pd.DataFrame().
- In the for loop, iterate over urb_pop_reader to be able to process all the DataFrame chunks in the dataset.
- Using the method append() of the DataFrame data, append df_pop_ceb to data.
