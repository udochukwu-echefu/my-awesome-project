import pandas as pd

# Load data from a CSV file
df = pd.read_csv("students.csv")

# First look at your data
print("Shape:", df.shape)        # rows, columns
print("Columns:", df.columns.tolist())
print()
print("First 3 rows:")
print(df.head(3))
print()
print("Summary stats:")
print(df.describe())


# 1. Show only Lagos students
print("Lagos students:")
print(df[df["city"] == "Lagos"])

# 2. Average score per city
print("Average score by city:")
print(df.groupby("city")["score"].mean())

# 3. Show only students who scored above 80
print("High scorers (above 80):")
print(df[df["score"] > 80])

# 4. Count students per grade
print("Students per grade:")
print(df["grade"].value_counts())