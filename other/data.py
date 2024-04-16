import pandas as pd

# Load the dataframes
negatives_df = pd.read_csv('data/negatives.csv.txt')
positives_df = pd.read_csv('data/positives.csv.txt')

# Merge the two DataFrames
merged_df = pd.concat([negatives_df, positives_df], ignore_index=True)

# Randomize the order of the rows
merged_randomized_df = merged_df.sample(frac=1).reset_index(drop=True)

# If you want to save the merged and randomized DataFrame to a new CSV
merged_randomized_df.to_csv('merged_randomized_new.csv', index=False)
