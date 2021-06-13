# Right join to find unique movies
Most of the recent big-budget science fiction movies can also be classified as action movies. You are given a table of science fiction movies called scifi_movies and another table of action movies called action_movies. Your goal is to find which movies are considered only science fiction movies. Once you have this table, you can merge the movies table in to see the movie names. Since this exercise is related to science fiction movies, use a right join as your superhero power to solve this problem.

The movies, scifi_movies, and action_movies tables have been loaded for you.

# Instructions

# Part 1:
Merge action_movies and scifi_movies tables with a right join on movie_id. Save the result as action_scifi.

# Part 2:
Update the merge to add suffixes, where '_act' and '_sci' are suffixes for the left and right tables, respectively.

# Part 3:
From action_scifi, subset only the rows where the genre_act column is null.

# Part 4:
Merge movies and scifi_only using the id column in the left table and the movie_id column in the right table with an inner join.
