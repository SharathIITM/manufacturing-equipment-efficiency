import matplotlib.pyplot as plt

# Quarterly data
quarters = ["Q1", "Q2", "Q3", "Q4"]
efficiency = [72.81, 71.16, 79.85, 80.82]
industry_target = 90

# Calculate average
average_efficiency = sum(efficiency) / len(efficiency)
print("Average Equipment Efficiency:", round(average_efficiency, 2))

# Create line chart
plt.figure(figsize=(8, 5))
plt.plot(quarters, efficiency, marker="o", linewidth=2, label="Equipment Efficiency")
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (90)")

plt.title("Quarterly Equipment Efficiency vs Industry Benchmark")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("trend.png")
plt.close()
