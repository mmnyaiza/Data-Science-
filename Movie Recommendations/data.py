import pandas as pd

# Load data from a CSV file
data = pd.read_csv('ratings.csv')

# Create a pivot table to calculate movie ratings
ratings_table = data.pivot_table(values='rating', index='userId', columns='title', fill_value=0)

# Print out the column names of the ratings_table DataFrame
print(ratings_table.columns)

# Access a specific column by name
user_ratings = ratings_table['userId']
print(user_ratings)

