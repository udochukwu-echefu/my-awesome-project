import numpy as np
import pandas as pd

# ── NUMPY ──────────────────────────────────────
# NumPy works with arrays (like lists, but faster + smarter)

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Average:", np.mean(numbers))
print("Total:", np.sum(numbers))
print("Highest:", np.max(numbers))
print("Lowest:", np.min(numbers))

# ── PANDAS ─────────────────────────────────────
# Pandas works with tables (like Excel in Python)

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000],
}

df = pd.DataFrame(data)
df["bonus"] = df["salary"] * 0.10
highest_paid = df.sort_values("salary", ascending=False)["name"].iloc[0]
print("Highest paid:", highest_paid)
print(df.sort_values("salary", ascending=False))
print (df[df["age"] > 28])

print("\n--- Our Table ---")
print(df)
print("\nAverage salary:", df["salary"].mean())
print("Oldest person:", df["age"].max())