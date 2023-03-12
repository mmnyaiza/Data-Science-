import pandas as pd
import numpy as np
import os
#
cwd = os.getcwd()
# Load the ratings dataset
ratings = pd.read_csv('/mnt/c/Users/Mphumzi/Downloads/Root/Movie recommendation/ml-latest-small/ml-latest-small/ratings.csv')

# Load the movies dataset
movies = pd.read_csv('movies.csv')

# Merge the datasets on movieId
data = pd.merge(ratings, movies, on='movieId')

# Create a pivot table to calculate movie ratings
ratings_table = data.pivot_table(values='rating', index='userId', columns='title', fill_value=0)

# Define the user ratings
user_ratings = ratings_table['User ID']

# Calculate the correlation between users
user_similarity = ratings_table.corrwith(user_ratings)

# Drop any NaN values
user_similarity = user_similarity.dropna()

# Sort the similarities in descending order
user_similarity.sort_values(ascending=False, inplace=True)

# Get the top 10 similar users
top_users = user_similarity.head(10)

# Get the movies that these top users have watched and rated highly
top_movies = ratings_table.loc[top_users.index].mean().sort_values(ascending=False).head(10)

# Print the recommended movies
print(top_movies)
