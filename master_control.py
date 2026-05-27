import os
import sys

def show_menu():
    print("=" * 80)
    print("      QUANTUM SYNDICATE PLATFORM CORE v1.2 — INTEGRATED OPERATING SUITE")
    print("      Developer: Pray Patel")
    print("=" * 80)
    print("  [1] Fire AI Vision Pipeline             (Extract Custom Muscle Ratings)")
    print("  [2] Execute Stage-2 Kelly Engine        (Compare Model vs Public Wisdom)")
    print("  [3] Run Machine Learning Intersections  (Apply Distance/Moisture Nodes)")
    print("  [4] Launch 10,000 Monte Carlo Races     (Stochastic Chaos Simulation)")
    print("  [5] Trigger Live Web Scraper Array      (Ingest External Odds Feeds)")
    print("  [6] Query Relational Ledger Archives     (Check Local SQL Databases)")
    print("  [7] Run Automated Settlement Auditor    (Calculate Profit & Clear Logs)")
    print("  [8] TERMINATE CENTRAL SYSTEM ENGINE")
    print("=" * 80)

def main():
    while True:
        show_menu()
        try:
            choice = input("Select System Vector Protocol (1-8): ").strip()
            print("\n" + "-" * 80)
            
            if choice == "1":
                os.system("python3 test_vision.py")
            elif choice == "2":
                os.system("python3 benter_ultra_engine.py")
            elif choice == "3":
                os.system("python3 benter_ml_elite.py")
            elif choice == "4":
                os.system("python3 benter_monte_carlo.py")
            elif choice == "5":
                os.system("python3 benter_live_scraper.py")
            elif choice == "6":
                os.system("python3 save_to_database.py")
            elif choice == "7":
                print("[SYS INTERFACE] Executing Post-Race Payout Calculations...")
                os.system("python3 results_checker.py")
            elif choice == "8":
                print("[SYS INTERFACE] Disconnecting server connections... Goodbye.")
                print("=" * 80)
                sys.exit()
            else:
                print("Invalid System Protocol Core Selection. Choose numbers 1-8.")
                
            print("-" * 80 + "\n")
            input("Press [ENTER] to return to the Master Control Panel Dashboard...")
            os.system("clear")
            
        except KeyboardInterrupt:
            print("\n\nSystem Interrupted safely.")
            sys.exit()

if __name__ == "__main__":
    main()
