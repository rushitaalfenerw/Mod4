import pandas as pd

# Load and rename dataset
df = pd.read_csv("Netflix_shows_movies.csv")
#data.to_csv("Netflix_shows_movies.csv", index=False)

# Check for missing values
print(df.isnull().sum())

# Handle missing values (e.g., fill with mode or drop rows)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
# Other missing value handling strategies can be applied based on specific data analysis needs.

# Explore the cleaned dataset
print(df.head())
print(df.info())

# Descriptive statistics
print(df.describe())

# Group by genre and count occurrences
genre_counts = df['listed_in'].str.split(', ').explode().value_counts()
print(genre_counts)

# Calculate rating distribution
rating_counts = df['rating'].value_counts()
print(rating_counts)

import matplotlib.pyplot as plt
import seaborn as sns

# Most watched genres
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.index[:10], y=genre_counts.values[:10])
plt.title('Top 10 Most Watched Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Ratings distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='rating', data=df)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()