import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the absolute path to the root of the project
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, "data", "steelers_games_by_year.csv")

# Load the cleaned Steelers dataset
df = pd.read_csv(data_path)

# Group by opponent and result (W/L/T)
win_loss_counts = df.groupby(["Opponent", "Result"]).size().unstack(fill_value=0)

# Plot
win_loss_counts.plot(kind="bar", stacked=False, figsize=(12, 6))
plt.title("Steelers Wins/Losses by Opponent")
plt.ylabel("Number of Games")
plt.xlabel("Opponent")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(axis="y")
plt.legend(title="Result")
plt.show()


