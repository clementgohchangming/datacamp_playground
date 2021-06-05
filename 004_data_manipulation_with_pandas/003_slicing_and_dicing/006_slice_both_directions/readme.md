# Slicing in both directions
You've seen slicing DataFrames by rows and by columns, but since DataFrames are two-dimensional objects, it is often natural to slice both dimensions at once. That is, by passing two arguments to .loc[], you can subset by rows and columns in one go.

pandas is loaded as pd. temperatures_srt is indexed by country and city, has a sorted index, and is available.
 
# Instructions
- Use .loc[] slicing to subset rows from India, Hyderabad to Iraq, Baghdad.
- Use .loc[] slicing to subset columns from date to avg_temp_c.
- Slice in both directions at once from Hyderabad to Baghdad, and date to avg_temp_c.
