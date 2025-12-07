import pandas as pd

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("data/premier_league.csv")  # make sure path is correct
print("Dataset loaded!")
print(df.head())

# -----------------------------
# 2. Calculate a score for each team
# -----------------------------
# We can combine Points and Goal Difference to estimate strength
df['Score'] = df['Points'] + df['Goal Difference']

# -----------------------------
# 3. Calculate Winning Probabilities
# -----------------------------
df['Win_Probability'] = df['Score'] / df['Score'].sum()

# -----------------------------
# 4. Sort teams by probability
# -----------------------------
predictions = df.sort_values('Win_Probability', ascending=False)

print("\n=== Predicted Winning Probabilities ===")
print(predictions[['Team', 'Points', 'Goal Difference', 'Win_Probability']])

# -----------------------------
# 5. Print Predicted Winner
# -----------------------------
winner = predictions.iloc[0]['Team']
print("\n🏆 Predicted Premier League Winner:", winner)
