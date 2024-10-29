Netflix Show and Movie Analysis

This Python script and R integration analyze a Netflix show and movie dataset (Netflix_shows_movies.csv). It performs data cleaning, exploration, and visualization tasks.

Python Script (data_analysis.py)

Import Libraries:

Pandas for data manipulation
Matplotlib and Seaborn for data visualization

Load and Clean Data:
Reads the CSV file using pandas.
Checks for missing values and handles them (e.g., filling with mode).

Data Exploration:
Prints the first few rows and summary statistics.
Explores the 'listed_in' column for genre information.
Calculates rating distribution.

Data Visualization:

Creates bar charts for:
Top 10 most watched genres.
Rating distribution.

R Integration ( requires tidyverse package)

Load Libraries:

tidyverse for data manipulation and visualization.

Load Data:
Checks if the CSV file exists at the specified path.
Reads the data using read.csv.

Data Exploration:
Prints the first few rows and column names.
Conditional Visualization (if 'listed_in' exists):
Creates a bar chart for the top 10 most watched genres using ggplot2.
Saves the chart as a PNG image.

Note:

Install the required libraries (pandas, matplotlib, seaborn, and tidyverse) before running the scripts.