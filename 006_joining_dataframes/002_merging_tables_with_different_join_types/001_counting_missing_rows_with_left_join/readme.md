# Counting missing rows with left join
The Movie Database is supported by volunteers going out into the world, collecting data, and entering it into the database. This includes financial data, such as movie budget and revenue. If you wanted to know which movies are still missing data, you could use a left join to identify them. Practice using a left join by merging the movies table and the financials table.

The movies and financials tables have been loaded for you.

# Instructions

# Part 1:

# Question

What column is likely the best column to merge the two tables on?

# Possible Answers

A. on='budget'
B. on='popularity'
C. on='id'

# Answer
C. on='id'

# Part 2:
Merge the movies table, as the left table, with the financials table using a left join, and save the result to movies_financials.

# Part 3:
Count the number of rows in movies_financials with a null value in the budget column.
