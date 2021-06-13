## Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, how='left', left_index=True, right_index=True)

# Print the first few rows of movies_ratings
print(movies_ratings.head())
