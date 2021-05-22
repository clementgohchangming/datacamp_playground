# Subsetting columns
When working with data, you may not need all of the variables in your dataset. Square brackets ([]) can be used to select only the columns that matter to you in an order that makes sense to you. To select only "col_a" of the DataFrame df, use

df["col_a"]
To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]
homelessness is available and pandas is loaded as pd.

# Instructions

Part 1: Create a DataFrame called individuals that contains only the individuals column of homelessness. Print the head of the result.

Part 2: Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
Print the head of the result.

Part 3: Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order.
Print the head of the result. 
