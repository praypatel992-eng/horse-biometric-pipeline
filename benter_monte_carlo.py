import numpy as np

print("===========================================================================")
# QUANT SYNDICATE ARCHITECTURE: MONTE CARLO STOCHASTIC SIMULATION CORE
print("===========================================================================")

# 1. Define Core Team Consensus Performance Baselines
# Instead of single scores, we give each horse an Average Performance Mean 
# and a Standard Deviation (Consistency/Variance Factor)
competitors = [
    {"name": "Runner 1 (Bulky Sprinter)",  "mean_perf": 82.5, "std_dev": 4.5, "odds": 5.5}, # High variance/unstable
    {"name": "Runner 2 (Lean Distance)",   "mean_perf": 87.0, "std_dev": 2.1, "odds": 2.1}, # Highly consistent
    {"name": "Runner 3 (Average Field)",   "mean_perf": 81.0, "std_dev": 3.0, "odds": 8.0},
    {"name": "Runner 4 (The Public Trap)", "mean_perf": 76.5, "std_dev": 5.0, "odds": 15.0}
]

SIMULATIONS = 10000
print(f"Initializing {SIMULATIONS:,} Stochastic Race Simulations...")
print("Modeling random track traffic, jockey variance, and physics limits...\n")

# Initialize win counter dictionary
win_counts = {c["name"]: 0 for c in competitors}

# 2. THE STOCHASTIC SIMULATION LOOP
for sim in range(SIMULATIONS):
    simulated_race_times = []
    
    for c in competitors:
        # Generate a random performance score for this specific race instance
        # Using a Normal (Gaussian) Distribution based on the horse's custom profile
        random_variance_score = np.random.normal(c["mean_perf"], c["std_dev"])
        simulated_race_times.append((c["name"], random_variance_score))
    
    # The horse with the HIGHEST performance score wins this simulated race instance
    winner_name = max(simulated_race_times, key=lambda x: x[1])[0]
    win_counts[winner_name] += 1

print("-" * 75)
print(f"Simulation Matrix Complete. Compiling Empirical Results:")
print("-" * 75)

# Calculate empirical probabilities based on actual simulation finish lines
p_monte_carlo = np.array([win_counts[c["name"]] / SIMULATIONS for c in competitors])

# Public market price conversion
p_market = np.array([1.0 / c["odds"] for c in competitors])
p_market /= np.sum(p_market)

# Capital optimization allocation (Quarter-Kelly)
BANKROLL = 1000.00
QUARTER_KELLY = 0.25

for idx, c in enumerate(competitors):
    true_chance = p_monte_carlo[idx]
    market_chance = p_market[idx]
    edge = true_chance / market_chance
    
    # Kelly constraint execution
    b = c["odds"] - 1.0
    k_fraction = max(0.0, ((b * true_chance) - (1.0 - true_chance)) / b) * QUARTER_KELLY
    cash_stake = BANKROLL * k_fraction
    
    print(f"• {c['name']}:")
    print(f"  [Stochastic Core] Total Simulated Wins : {win_counts[c['name']]} / {SIMULATIONS:,}")
    print(f"  [Empirical Line] Simulated Win Chance : {round(true_chance * 100, 1)}%")
    print(f"  [Market Variance] Alpha Edge Multiplier: {round(edge, 2)}x")
    
    if cash_stake > 0:
        print(f"  💰 MONTE CARLO ORDER : Allocate ${cash_stake:,.2f} ({round(k_fraction*100, 2)}% bankroll)")
    else:
        print("  ❌ MONTE CARLO ORDER : PASS")
    print("-" * 75)
