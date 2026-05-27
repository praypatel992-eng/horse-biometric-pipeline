import sqlite3

print("--- OPENING LIVE RELATIONAL STORAGE LEDGER ---")
conn = sqlite3.connect("horse_intelligence.db")
cursor = conn.cursor()

# Query every column from our race history table
try:
    cursor.execute("SELECT record_id, horse_name, muscle_score, calculated_probability FROM race_records")
    rows = cursor.fetchall()
    
    print("-" * 85)
    print(f"{'ID':<5} | {'HORSE NAME':<30} | {'MUSCLE SCORE':<12} | {'CALCULATED PROB'}")
    print("-" * 85)
    
    for row in rows:
        # Format the table rows cleanly on screen
        print(f"{row[0]:<5} | {row[1]:<30} | {row[2]:<12} | {round(row[3]*100, 1)}%")
    print("-" * 85)
    print(f"Total Database Payload: {len(rows)} secure records retrieved.")

except Exception as e:
    print(f"Database Read Error: {e}")

conn.close()
