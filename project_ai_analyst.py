import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ── LOAD & ANALYSE DATA WITH PANDAS ──────────────
df = pd.read_csv("sales_data.csv")
df["salesperson"] = df["salesperson"].str.strip().str.title()
df["revenue"] = df["units_sold"] * df["unit_price"]

total_revenue = df["revenue"].sum()
top_region = df.groupby("region")["revenue"].sum().idxmax()
top_salesperson = df.groupby("salesperson")["revenue"].sum().idxmax()
best_product = df.groupby("product")["units_sold"].sum().idxmax()

region_breakdown = df.groupby("region")["revenue"].sum().to_string()
salesperson_breakdown = df.groupby("salesperson")["revenue"].sum().to_string()
product_breakdown = df.groupby("product")["units_sold"].sum().to_string()

# ── GIVE THE AI THE DATA AS CONTEXT ──────────────
system_prompt = f"""
You are an expert sales data analyst assistant.
You have access to real sales data summarised below.
Answer all questions accurately using this data.
Be concise and always give actionable insights.

=== SALES DATA SUMMARY ===
Total Revenue: {total_revenue:,}
Top Region: {top_region}
Top Salesperson: {top_salesperson}
Best Selling Product: {best_product}
Total Transactions: {len(df)}
Date Range: {df['date'].min()} to {df['date'].max()}

=== REVENUE BY REGION ===
{region_breakdown}

=== REVENUE BY SALESPERSON ===
{salesperson_breakdown}

=== UNITS SOLD BY PRODUCT ===
{product_breakdown}
"""

messages = [{"role": "system", "content": system_prompt}]

# ── CHAT INTERFACE ────────────────────────────────
print("📊 AI Sales Analyst ready!")
print(f"Loaded {len(df)} sales records")
print("Ask me anything about the sales data. Type 'quit' to exit.")
print("-" * 50)

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Analyst: Goodbye! Keep making data-driven decisions!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"Analyst: {reply}")
    print()