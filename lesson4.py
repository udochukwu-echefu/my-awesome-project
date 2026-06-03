import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("students.csv")

# ── CHART 1: Bar chart — average score per city ──
city_scores = df.groupby("city")["score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(city_scores.index, city_scores.values, color=["blue", "orange", "green"])
plt.title("Average Score by City")
plt.xlabel("City")
plt.ylabel("Average Score")
plt.savefig("chart1_cities.png")
plt.show()

# ── CHART 2: Histogram — score distribution ──
plt.figure(figsize=(8, 5))
plt.hist(df["score"], bins=5, color="purple", edgecolor="black")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.savefig("chart2_scores.png")
plt.show()

# ── CHART 3: Scatter plot — age vs score ──
plt.figure(figsize=(8, 5))
plt.scatter(df["age"], df["score"], color="red", s=100)
plt.title("Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.savefig("chart3_scatter.png")
plt.show()

print("All 3 charts saved!")

