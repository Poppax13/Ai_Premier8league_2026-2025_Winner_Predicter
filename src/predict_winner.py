import pandas as pd

def predict_season_winner(model, X_test, df_test, le_team):
    df_test['Win_Probability'] = model.predict_proba(X_test)[:, 1]
    predictions = df_test.sort_values('Win_Probability', ascending=False)
    
    winner_encoded = predictions.iloc[0]['TeamEnc']
    winner_team = le_team.inverse_transform([int(winner_encoded)])[0]
    
    print("\n=== Predicted Winning Probabilities ===")
    print(predictions[['Team', 'Points', 'Win_Probability']])
    print("\n🏆 Predicted Premier League Winner:", winner_team)
    
    return predictions, winner_team
