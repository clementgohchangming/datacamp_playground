# Import pandas
import pandas as pd

# print(artist_names)

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=artist_names)

print(df.head())

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())

