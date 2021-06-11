# Sorting by index values
Previously, you changed the order of the rows in a DataFrame by calling .sort_values(). It's also useful to be able to sort by elements in the index. For this, you need to use .sort_index().

pandas is loaded as pd. temperatures_ind has a multi-level index of country and city, and is available.

# Instructions
- Sort temperatures_ind by the index values.
- Sort temperatures_ind by the index values at the "city" level.
- Sort temperatures_ind by ascending country then descending city.
