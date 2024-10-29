# Load necessary libraries
library(tidyverse)

# Load the dataset in R using the full path
file_path <- "~/Documents/Masters/Mod4/Netflix_shows_movies.csv"

# Attempt to read the CSV file
if (file.exists(file_path)) {
    netflix_data <- read.csv(file_path)
    
    # Check the first few rows and column names
    print(head(netflix_data))
    print(colnames(netflix_data))
    
    # Check if 'listed_in' column exists before proceeding
    if ("listed_in" %in% colnames(netflix_data)) {
        
        # Create a bar chart for the top 10 genres
        plot <- netflix_data %>%
            separate_rows(listed_in, sep = ", ") %>%
            count(listed_in) %>%
            top_n(10, n) %>%
            ggplot(aes(x = reorder(listed_in, n), y = n)) +
            geom_bar(stat = "identity", fill = "steelblue") +
            coord_flip() +
            labs(title = "Top 10 Most Watched Genres",
                 x = "Genre",
                 y = "Count")
        
        # Save the plot
        ggsave("Top_10_Most_Watched_Genres.png", plot, width = 8, height = 6)  # Change dimensions as needed
        
    } else {
        print("The 'listed_in' column does not exist in the dataset.")
    }
} else {
    print("The file does not exist at the specified path.")
}
