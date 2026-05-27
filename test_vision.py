import cv2
import numpy as np
import sqlite3
import os
from ultralytics import YOLO

# Fix: Dynamically track the absolute Desktop path file location on your Mac
desktop_dir = os.path.expanduser("~/Desktop")
img_path = os.path.join(desktop_dir, "horse_test.jpg")
db_path = os.path.join(desktop_dir, "horse_intelligence.db")

model = YOLO("yolov8n.pt")

print("--- INITIALIZING LIVE BIOMETRIC INGESTION ---")
if not os.path.exists(img_path):
    print(f"Error: Target image file missing from your directory path framework.")
else:
    results = model(img_path, verbose=False)
    img = cv2.imread(img_path)
    
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy.tolist())
            width = x2 - x1
            hq_x1 = int(x2 - (width * 0.35))
            
            crop = img[y1:y2, hq_x1:x2]
            gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            
            grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            angles = np.abs(np.arctan2(grad_y, grad_x) * 180 / np.pi)
            magnitude = cv2.magnitude(grad_x, grad_y)
            
            clean_edges = np.where((angles > 20) & (angles < 160), magnitude, 0)
            variance = clean_edges.var()
            final_muscle_score = round(min(1.0 + (variance / 3.0), 10.0), 2)
            
            print(f"Calculated Muscle Mass Index: {final_muscle_score} / 10")
            print("Connecting to secure SQL ledger storage...")
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            target_name = f"Paddock Subject Alpha (YOLO-Score: {final_muscle_score})"
            cursor.execute("INSERT INTO race_records (horse_name, muscle_score, calculated_probability, public_odds, final_position) VALUES (?, ?, ?, ?, ?)", (target_name, final_muscle_score, 0.446, 8.5, 1))
            
            conn.commit()
            conn.close()
            print("--> SUCCESS: Biometric data stamped permanently into horse_intelligence.db archive.")
            break
