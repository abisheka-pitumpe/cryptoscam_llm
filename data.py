import pandas as pd

# Load the dataframes
negatives_df = pd.read_csv('negatives_new.csv')
positives_df = pd.read_csv('positives_new.csv')

# Merge the two DataFrames
merged_df = pd.concat([negatives_df, positives_df], ignore_index=True)

# Randomize the order of the rows
merged_randomized_df = merged_df.sample(frac=1).reset_index(drop=True)

# If you want to save the merged and randomized DataFrame to a new CSV
merged_randomized_df.to_csv('merged_randomized.csv', index=False)
