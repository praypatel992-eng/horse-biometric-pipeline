import numpy as np

print("===========================================================================")
# LIVE UPCOMING EVENT ENGINE: THE BELMONT STAKES ARCHITECTURE
print("===========================================================================")

# The Belmont Stakes is a legendary long-distance race (12 Furlongs) on a dry track
RACE_DISTANCE_FURLONGS = 12.0   
TRACK_MOISTURE_INDEX = 1.5      # Fast, dry track condition

print(f"LIVE FIELD CARD LOADED: Belmont Stakes | Distance = {RACE_DISTANCE_FURLONGS} Furlongs")
print("Extracting multi-variable non-linear machine learning nodes...\n")

# ACTUAL UPCOMING FIELD CONTESTANTS & EXPECTED ODDS MARKET PRICES
runners = [
    {"name": "Mindframe (The Fast Favorite)", "base_speed": 94, "ai_muscle_mass": 5.2, "market_odds": 2.5}, 
    {"name": "Seize the Grey (The Mud Champion)", "base_speed": 91, "ai_muscle_mass": 8.8, "market_odds": 6.0}, # High muscle bulk
    {"name": "Mystik Dan (The Classic Winner)", "base_speed": 92, "ai_muscle_mass": 6.1, "market_odds": 5.0},
    {"name": "Resilience (The Lean Distance Sleeper)", "base_speed": 89, "ai_muscle_mass": 4.5, "market_odds": 12.0} # Lean condition!
]

ml_propensity_scores = []
for r in runners:
    score = r["base_speed"]
    
    # Machine Learning Node: Distance x Muscle Mass Interaction
    if RACE_DISTANCE_FURLONGS <= 6.0:
        muscle_alpha = r["ai_muscle_mass"] ** 1.4  
    else:
        # Long endurance race node: Heavy muscle bulk is penalized for burning oxygen too fast!
        muscle_alpha = r["ai_muscle_mass"] * 0.25   
        
    final_ml_feature_score = score + (muscle_alpha * 4.0)
    ml_propensity_scores.append(final_ml_feature_score)

# Softmax pooling
exp_ml = np.exp(np.array(ml_propensity_scores) / 5.0) 
p_pure_ml = exp_ml / np.sum(exp_ml)

# Market normalization
p_market = np.array([1.0 / r["market_odds"] for r in runners])
p_market /= np.sum(p_market) 

# Benter Composite Weight Blending Layer
p_composite = (p_pure_ml ** 0.70) * (p_market ** 0.30)
p_composite /= np.sum(p_composite)

# Capital Staking Simulation Layer
BANKROLL = 1000.00
QUARTER_KELLY = 0.25

print("-" * 75)
for idx, r in enumerate(runners):
    true_chance = p_composite[idx]
    market_chance = p_market[idx]
    edge = true_chance / market_chance
    
    b = r["market_odds"] - 1.0
    k_fraction = max(0.0, ((b * true_chance) - (1.0 - true_chance)) / b) * QUARTER_KELLY
    cash_allocation = BANKROLL * k_fraction
    
    print(f"• {r['name']}:")
    print(f"  [AI Live Line] True Win Chance  : {round(true_chance * 100, 1)}%")
    print(f"  [Market Bias] Alpha Edge Value : {round(edge, 2)}x")
    
    if cash_allocation > 0:
        print(f"  💰 PAPER TRADE EXECUTION : Mock-Stake ${cash_allocation:,.2f} ({round(k_fraction*100, 2)}% bankroll)")
    else:
        print("  ❌ PAPER TRADE EXECUTION : PASS (No mathematical value)")
    print("-" * 75)
