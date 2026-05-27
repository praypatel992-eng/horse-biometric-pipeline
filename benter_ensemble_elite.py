import numpy as np

print("===========================================================================")
# QUANT SYNDICATE ARCHITECTURE: TRI-MODEL ENSEMBLE NEURAL SYSTEM
print("===========================================================================")

# Environmental parameters
DISTANCE = 12.0  # Long Endurance
MOISTURE = 1.0   # Fast, Dry Track

# Core Competitor Profiles
runners = [
    {"name": "Runner 1 (Bulky Sprinter)", "speed": 85, "muscle": 9.2, "odds": 5.5},
    {"name": "Runner 2 (Lean Distance)",  "speed": 88, "muscle": 4.5, "odds": 2.1},
    {"name": "Runner 3 (Average Field)",   "speed": 80, "muscle": 6.0, "odds": 8.0},
    {"name": "Runner 4 (The Public Trap)", "speed": 75, "muscle": 5.0, "odds": 15.0}
]

# --- 1. MODEL ALPHA NODE (Historical Speed Probability) ---
speed_array = np.array([r["speed"] for r in runners], dtype=float)
p_alpha = np.exp(speed_array / 10.0) / np.sum(np.exp(speed_array / 10.0))

# --- 2. MODEL BETA NODE (Biometric Vision Probability) ---
# Calculate muscle efficiency dynamically based on the distance environment
muscle_scores = []
for r in runners:
    if DISTANCE > 8.0:
        # Distance penalty: Lean horses (low muscle score mass) are more efficient
        efficiency = 10.0 - r["muscle"]
    else:
        # Sprint bonus: Bulky horses are more efficient
        efficiency = r["muscle"]
    muscle_scores.append(efficiency)

muscle_array = np.array(muscle_scores, dtype=float)
p_beta = np.exp(muscle_array / 2.0) / np.sum(np.exp(muscle_array / 2.0))

# --- 3. MODEL GAMMA NODE (Environmental Track Inversion Probability) ---
# Muddy tracks heavily favor high raw muscle; dry tracks favor baseline speed ratings
gamma_scores = []
for r in runners:
    if MOISTURE > 7.0:
        score = r["muscle"] * 1.5
    else:
        score = r["speed"] * 0.8
    gamma_scores.append(score)

gamma_array = np.array(gamma_scores, dtype=float)
p_gamma = np.exp(gamma_array / 10.0) / np.sum(np.exp(gamma_array / 10.0))


# --- THE ENSEMBLE LAYER: DOT PRODUCT BLENDING MATRIX ---
# We blend the three completely independent models using an ensemble consensus formula
w_a, w_b, w_g = 0.40, 0.45, 0.15  # Model importance weighting factors
p_ensemble = (p_alpha * w_a) + (p_beta * w_b) + (p_gamma * w_g)
p_ensemble /= np.sum(p_ensemble)  # Lock pool to exactly 100%

# Establish public market baseline
p_market = np.array([1.0 / r["odds"] for r in runners])
p_market /= np.sum(p_market)

# Final Stage-2 Capital Optimization Allocation (Quarter-Kelly)
BANKROLL = 1000.00
QUARTER_KELLY = 0.25

print(f"Executing Consensus Verification Across Models Alpha, Beta, & Gamma...\n")
print("-" * 75)

for idx, r in enumerate(runners):
    true_chance = p_ensemble[idx]
    market_chance = p_market[idx]
    alpha_edge = true_chance / market_chance
    
    # Capital management execution
    b = r["odds"] - 1.0
    k_fraction = max(0.0, ((b * true_chance) - (1.0 - true_chance)) / b) * QUARTER_KELLY
    cash_stake = BANKROLL * k_fraction
    
    print(f"• {r['name']}:")
    print(f"  [Model Consensus] Integrated Probability : {round(true_chance * 100, 1)}%")
    print(f"  [Alpha Discrepancy] Market Edge Index   : {round(alpha_edge, 2)}x")
    
    if cash_stake > 0:
        print(f"  💰 ORDER DEPLOYED : Stake ${cash_stake:,.2f} ({round(k_fraction*100, 2)}% bankroll)")
    else:
        print("  ❌ ORDER DEPLOYED : PASS (Market price overvalued)")
    print("-" * 75)
