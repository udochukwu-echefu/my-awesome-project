import pandas as pd

df = pd.read_csv("dirty_data.csv")

print("=== ORIGINAL MESSY DATA ===")
print(df)
print()

# 1. Find missing values
print("=== MISSING VALUES ===")
print(df.isnull().sum())
print()

# 2. Remove duplicates
df = df.drop_duplicates()
print("=== AFTER REMOVING DUPLICATES ===")
print(df)
print()

# 3. Fix missing values
df["score"] = df["score"].fillna(df["score"].mean())
df["age"] = df["age"].fillna(df["age"].median())
print("=== AFTER FIXING MISSING VALUES ===")
print(df)
print()

# 4. Fix inconsistent city names (Lagos/LAGOS/lagos → Lagos)
df["city"] = df["city"].str.strip().str.title()

# 5. Fix name spacing
df["name"] = df["name"].str.strip().str.title()

# 6. Remove outliers (age 200 is clearly wrong)
df = df[df["age"] < 100]

print("=== CLEAN DATA ===")
print(df)