import pandas as pd
import os

# Define the path to the downloaded CSV file
csv_path = os.path.join(os.getcwd(), "data", "games.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# Filter for Pittsburgh Steelers games
steelers_df = df[(df["home_team"] == "PIT") | (df["away_team"] == "PIT")].copy()

# Display the first few rows
print(steelers_df.head())






