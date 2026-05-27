import matplotlib.pyplot as plt

print("===========================================================================")
# GRAPHICS ENGINE: BIOMETRIC VISUALIZATION INTERFACE
print("===========================================================================")

# 1. Competitor Data Arrays
runners = ["Mindframe", "Seize the Grey", "Mystik Dan", "Resilience"]
muscle_scores = [5.2, 8.8, 6.1, 4.5]

print("Processing database variables and rendering graphics plot...")

# 2. Configure the Chart Layout
plt.figure(figsize=(8, 5))
colors = ['#3498db', '#e74c3c', '#f1c40f', '#2ecc71'] # Custom hex color codes

# Build a bar chart structure
plt.bar(runners, muscle_scores, color=colors, edgecolor='black', zorder=2)

# 3. Design the Label Overlays
plt.title("Biometric Performance Review: Muscle Mass Counts", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Upcoming Field Contestants", fontsize=11, labelpad=10)
plt.ylabel("Proprietary Muscle Score Index (1-10)", fontsize=11, labelpad=10)
plt.ylim(0, 10)
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)

# Add exact value labels on top of each bar marker
for i, score in enumerate(muscle_scores):
    plt.text(i, score + 0.2, f"{score}/10", ha='center', fontweight='bold', fontsize=10)

# 4. Export the Graphic Directly onto your Desktop Wallpaper
output_filename = "belmont_biometric_chart.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
plt.close()

print(f"\nSUCCESS! Generated highly visual data presentation chart.")
print(f"Look at your Desktop workspace folder layout for: {output_filename}")
