import pandas as pd
from math import pow

file_path="results.txt"

# Initial ELO Ratings
initial_ratings = {
    "Rangers": 1500, "Celtic": 1500,
    "Hearts": 1500, "Kilmarnock": 1500, "St. Mirren": 1500, "Dundee": 1500,
    "Aberdeen": 1500, "Hibernian": 1500, "Motherwell": 1500, "St. Johnstone": 1500,
    "Ross County": 1500, "Dundee United": 1500
}

# Constants
K = 30  # ELO adjustment factor

# Load match results
def load_results(file_path):
    return pd.read_csv(file_path, names=["Date", "TeamA", "TeamB", "ScoreA", "ScoreB"])

# Expected score for team A given ratings of A and B
def expected_score(rating_a, rating_b):
    return 1 / (1 + pow(10, (rating_b - rating_a) / 400))

# Update ratings based on a single match
def update_ratings(rating_a, rating_b, score_a, score_b):
    expected_a = expected_score(rating_a, rating_b)
    expected_b = expected_score(rating_b, rating_a)
    
    # Determine the outcome (1 = win, 0.5 = draw, 0 = loss)
    if score_a > score_b:
        actual_a, actual_b = 1, 0
    elif score_a < score_b:
        actual_a, actual_b = 0, 1
    else:
        actual_a, actual_b = 0.5, 0.5
    
    # Calculate new ratings
    new_rating_a = rating_a + K * (actual_a - expected_a)
    new_rating_b = rating_b + K * (actual_b - expected_b)
    
    return new_rating_a, new_rating_b

# Main function to process all results
def process_results(file_path, initial_ratings):
    ratings = initial_ratings.copy()
    results = load_results(file_path)
    
    for _, row in results.iterrows():
        team_a, team_b = row['TeamA'], row['TeamB']
        score_a, score_b = row['ScoreA'], row['ScoreB']
        
        # Get current ratings
        rating_a = ratings[team_a]
        rating_b = ratings[team_b]
        
        # Update ratings
        new_rating_a, new_rating_b = update_ratings(rating_a, rating_b, score_a, score_b)
        ratings[team_a] = new_rating_a
        ratings[team_b] = new_rating_b
        
        # Print match outcome and updated ratings
        print(f"{team_a} vs {team_b}: {score_a}-{score_b}")
        print(f"Updated Ratings -> {team_a}: {new_rating_a:.2f}, {team_b}: {new_rating_b:.2f}")
    
        # Sort ratings in descending order
        sorted_ratings = dict(sorted(ratings.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_ratings

# Run the ELO rating process on sample file
final_ratings = process_results("results.txt", initial_ratings)
print("\nCurrent ELO:")
for team, rating in final_ratings.items():
    print(f"{team}: {rating:.2f}")
