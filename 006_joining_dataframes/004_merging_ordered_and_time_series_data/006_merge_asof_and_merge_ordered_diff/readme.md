# merge_asof() and merge_ordered() differences
The merge_asof() and merge_ordered() functions are similar in the type of merge they perform and the input arguments they use. In this exercise, think about how the functions are different.

# Instructions
Drag and drop the statement into the appropriate box for either the merge_asof() function, the merge_ordered() function, or both if it applies to both functions.

# Items to drag
A. This function can be used when working with ordered or time-series data
B. This function can set the suffix for overlapping column names.
C. It allows for a right join during the merge
D. It can be used to do fuzzy matching of dates betwen tables
E. After matching two tables, if there are missing values at the top of the table from the right table, this function can fill them in.
F. Has an argument that can be set to forward to select the first row in the right table whose key column is greater than or equal to the left 
G. If it cannot match the rows of the tables exactly, it can use forward fill to interpolate the missing data

# Buckets
1. merge_asof()
2. merge_unordered()
3. both

# Answer
(both) A. This function can be used when working with ordered or time-series data
(both) B. This function can set the suffix for overlapping column names.
(merge_unordered) C. It allows for a right join during the merge
(asof). It can be used to do fuzzy matching of dates between tables
(asof) E. After matching two tables, if there are missing values at the top of the table from the right table, this function can fill them in.
(asof) F. Has an argument that can be set to forward to select the first row in the right table whose key column is greater than or equal to the left 
(merge_unordered) G. If it cannot match the rows of the tables exactly, it can use forward fill to interpolate the missing data


