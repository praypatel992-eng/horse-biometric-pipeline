import numpy as np

print("===========================================================================")
# QUANTUM CAP-ALLOCATION ENGINE: BENTER STAGE-2 ARCHITECTURE
print("===========================================================================")

# 1. Advanced Field Data Matrix
# We track public price, raw performance ratings, and biometric muscle features
race_field = [
    {"name": "Runner 1 (The Heavy Favorite)", "odds": 1.75, "speed_rating": 88, "muscle_index": 5.5},
    {"name": "Runner 2 (The Hidden Overlay)", "odds": 8.50, "speed_rating": 81, "muscle_index": 9.4}, # Massive physical condition!
    {"name": "Runner 3 (The Stable Inefficient)","odds": 5.00, "speed_rating": 83, "muscle_index": 6.0},
    {"name": "Runner 4 (The Public Trap)",     "odds": 14.00, "speed_rating": 72, "muscle_index": 3.1}
]

# --- STAGE 1: GENETIC PROPENSITY SCORING (The Pure Model) ---
raw_scores = []
for runner in race_field:
    # Blend base speed with custom biometric features
    score = (runner["speed_rating"] / 10.0) + runner["muscle_index"]
    raw_scores.append(score)

# Apply Softmax with temperature control scaling (T=2.2) to establish pure model probabilities
exp_scores = np.exp(np.array(raw_scores) / 2.2)
p_model = exp_scores / np.sum(exp_scores)


# --- STAGE 2: THE COMPOSITE BLENDING LAYER (Benter's Secret Sauce) ---
# Benter discovered that blending model probabilities with market probabilities 
# via a logarithmic weight creates a significantly more accurate predictive line.
p_composite = []
total_composite_weight = 0.0

# Extract public implied probabilities from market prices
p_market = np.array([1.0 / r["odds"] for r in race_field])
# Normalize market probabilities to ensure parimutuel pool integrity (sum to 100%)
p_market = p_market / np.sum(p_market)

# Blending weights: 0.65 Model influence, 0.35 Market wisdom influence
w_model = 0.65
w_market = 0.35

for idx in range(len(race_field)):
    # Geometric mean blending technique to optimize composite calibration
    raw_blend = (p_model[idx] ** w_model) * (p_market[idx] ** w_market)
    p_composite.append(raw_blend)

# Re-normalize composite vector to keep probabilities locked at exactly 100.0%
p_composite = np.array(p_composite) / np.sum(p_composite)


# --- RISK MITIGATION LAYER: FRACTIONAL KELLY STAKING ---
# Benter never bet full Kelly allocations because real-world variance causes bankroll decay.
# We implement an institutional 0.25 (Quarter-Kelly) multiplier safety framework.
BANKROLL = 1000.00  # Starting capital simulation pool
KELLY_MULTIPLIER = 0.25

print(f"Active Capital Management Simulation Pool: ${BANKROLL:,.2f}")
print("Executing Multi-Stage Edge Discrepancy Scans...\n")

for idx, runner in enumerate(race_field):
    true_p = p_composite[idx]
    market_p = p_market[idx]
    decimal_odds = runner["odds"]
    
    # Calculate True Discrepancy Ratio (Overlay Index)
    edge_ratio = true_p / market_p
    
    # The Kelly Formula: f* = (bp - q) / b
    # Where b = decimal odds - 1, p = true probability, q = 1 - p
    b_factor = decimal_odds - 1.0
    q_factor = 1.0 - true_p
    
    raw_kelly = ((b_factor * true_p) - q_factor) / b_factor
    
    # Apply the Fractional safety buffer
    safeguarded_stake_fraction = max(0.0, raw_kelly * KELLY_MULTIPLIER)
    suggested_cash_allocation = BANKROLL * safeguarded_stake_fraction
    
    print(f"• {runner['name']}:")
    print(f"  [+] Market Price Forecast  : {round(market_p * 100, 1)}% chance")
    print(f"  [+] AI Stage-2 Forecast    : {round(true_p * 100, 1)}% chance")
    print(f"  [+] Calculated Alpha Edge  : {round(edge_ratio, 2)}x Value Multiplier")
    
    if suggested_cash_allocation > 0:
        print(f"  ⭐ SYSTEM STAKE TRIGGERED : Allocate {round(safeguarded_stake_fraction * 100, 2)}% of capital")
        print(f"  💰 EXECUTION ORDER        : Deploy exact cash value: ${suggested_cash_allocation:,.2f}")
    else:
        print("  [-] SYSTEM STAKE TRIGGERED : PASS (No mathematical alpha advantage)")
    print("-" * 75)
