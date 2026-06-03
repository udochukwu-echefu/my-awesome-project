import pandas as pd
import matplotlib.pyplot as plt

# ── 1. LOAD ──────────────────────────────────────
df = pd.read_csv("sales_data.csv")
print("=== RAW DATA ===")
print(df.shape)
print(df.head())

# ── 2. CLEAN ─────────────────────────────────────
# Fix inconsistent salesperson names
df["salesperson"] = df["salesperson"].str.strip().str.title()

# Remove duplicates
df = df.drop_duplicates()

# Convert date column to proper date type
df["date"] = pd.to_datetime(df["date"])

print("Cleaned. Shape:", df.shape)

# ── 3. ANALYSE ───────────────────────────────────
# Calculate revenue for each row
df["revenue"] = df["units_sold"] * df["unit_price"]

# Q1: Revenue by region
region_revenue = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print("=== REVENUE BY REGION ===")
print(region_revenue)

# Q2: Units sold by product
product_sales = df.groupby("product")["units_sold"].sum().sort_values(ascending=False)
print("=== UNITS SOLD BY PRODUCT ===")
print(product_sales)

# Q3: Top salesperson by revenue
sales_person = df.groupby("salesperson")["revenue"].sum().sort_values(ascending=False)
print("=== TOP SALESPERSON ===")
print(sales_person)
print("Winner:", sales_person.index[0])

# ── 4. VISUALISE ─────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Sales Analysis Report", fontsize=16)

# Chart 1: Revenue by region
axes[0].bar(region_revenue.index, region_revenue.values, color=["blue", "orange", "green"])
axes[0].set_title("Revenue by Region")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Revenue (₦)")

# Chart 2: Units sold by product
axes[1].bar(product_sales.index, product_sales.values, color=["purple", "red", "cyan"])
axes[1].set_title("Units Sold by Product")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Units Sold")

# Chart 3: Revenue by salesperson
axes[2].bar(sales_person.index, sales_person.values, color=["gold", "silver", "brown", "pink"])
axes[2].set_title("Revenue by Salesperson")
axes[2].set_xlabel("Salesperson")
axes[2].set_ylabel("Revenue (₦)")

plt.tight_layout()
plt.savefig("sales_report.png")
plt.show()

print("Report saved as sales_report.png")