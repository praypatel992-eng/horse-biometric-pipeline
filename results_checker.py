import os
import re

print("===========================================================================")
# CORES SYSTEM: AUTOMATED AUDIT & PROFIT SETTLING ENGINE
print("===========================================================================")

file_path = "live_paper_trades.txt"

if not os.path.exists(file_path):
    print(f"Error: Could not locate '{file_path}' on your Desktop workspace.")
else:
    # 1. Read the active paper trades file
    with open(file_path, "r") as f:
        content = f.read()
    
    print("Active Pending Bets Located in Ledger:")
    print("-" * 50)
    
    # Use regular expressions to extract horse names, stakes, and odds from the file text
    bets = re.findall(r"• ([\w\s\(\)]+?)\s*\|\s*Target Stake:\s*\$(\d+\.\d+)\s*\|\s*Market Odds:\s*(\d+\.\d+)", content)
    
    active_portfolio = []
    total_staked_capital = 0.0
    
    for horse, stake_str, odds_str in bets:
        stake = float(stake_str)
        odds = float(odds_str)
        total_staked_capital += stake
        active_portfolio.append({"name": horse.strip(), "stake": stake, "odds": odds})
        print(f"  [Staked] {horse.strip()} | Risk: ${stake:.2f} | Payout Multiplier: {odds}x")
        
    print(f"\nTotal Portfolio Capital at Risk: ${total_staked_capital:.2f}")
    print("-" * 50)
    
    # 2. Input the Winning Outcome
    # In a production system, this string is pulled automatically from a web scraping routine
    print("\nAvailable Competitors:")
    for idx, r in enumerate(active_portfolio):
        print(f" [{idx + 1}] {r['name']}")
        
    try:
        selection = int(input("\nEnter the number of the horse that won the race: "))
        winner_name = active_portfolio[selection - 1]["name"]
    except:
        print("Invalid choice. Running default settlement simulation on Seize the Grey...")
        winner_name = "Seize the Grey (The Mud Champion)"

    print(f"\nSettling race contracts... Confirmed Winner: {winner_name}")
    print("-" * 50)
    
    # 3. Calculate Payouts and Returns
    gross_returns = 0.0
    for r in active_portfolio:
        if r["name"] == winner_name:
            # Payout formula: Stake * Decimal Odds
            win_payout = r["stake"] * r["odds"]
            gross_returns += win_payout
            print(f"  🎉 WINNER MATCHED: {r['name']} paid out ${win_payout:.2f} on a ${r['stake']:.2f} stake!")
            
    net_profit_loss = gross_returns - total_staked_capital
    new_simulated_bankroll = 1000.00 + net_profit_loss
    
    print("-" * 50)
    print(f"Gross Return Cash Flow : ${gross_returns:.2f}")
    print(f"Net Session Alpha P/L  : ${net_profit_loss:+.2f}")
    print(f"Updated System Bankroll: ${new_simulated_bankroll:,.2f}")
    
    # 4. Update the Text Ledger Permanently
    updated_content = re.sub(
        r"FINAL STATUS\s*:\s*PENDING OFFICIAL RESULTS",
        f"FINAL STATUS   : SETTLED\nOFFICIAL WINNER: {winner_name}\nSESSION P/L    : {net_profit_loss:+.2f}\nUPDATED BAL    : ${new_simulated_bankroll:,.2f}",
        content
    )
    
    with open(file_path, "w") as f:
        f.write(updated_content)
        
    print("\n--> SUCCESS: System ledger files archived and stamped with session results!")
