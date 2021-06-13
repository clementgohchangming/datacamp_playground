# Inner joins and number of rows returned
All of the merges you have studied to this point are called inner joins. It is necessary to understand that inner joins only return the rows with matching values in both tables. You will explore this further by reviewing the merge between the wards and census tables, then comparing it to merges of copies of these tables that are slightly altered, named wards_altered, and census_altered. The first row of the wards column has been changed in the altered tables. You will examine how this affects the merge between them. The tables have been loaded for you.

For this exercise, it is important to know that the wards and census tables start with 50 rows.

# Instructions

# Part 1
Merge wards and census on the ward column and save the result to wards_census.

# Part 2
Merge the wards_altered and census tables on the ward column, and notice the difference in returned rows.

# Part 3
Merge the wards and census_altered tables on the ward column, and notice the difference in returned rows.
