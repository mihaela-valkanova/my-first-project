import pandas as pd
import numpy as np

customers = {
    "customer_id": [1, 2, 3, 4],
    "customer_name": ["Anna", "Boris", "Clara", "Daniel"],
    "country": ["BG", "BG", "DE", None]
}

orders = {
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer_id": [1, 2, 1, 3, 2, 4],
    "order_date": [
        "2024-01-10", "2024-01-20",
        "2024-02-05", "2024-02-25",
        "2024-03-03", "2024-03-18"
    ],
    "revenue": [500, 1200, 800, None, 600, 900]
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

print("CUSTOMERS")
print(df_customers)
print("-" * 40)

print("ORDERS")
print(df_orders)
print("-" * 40)

df_orders = df_orders.dropna(subset=["revenue"])

df_customers["country"] = df_customers["country"].fillna("Unknown")

print("CLEANED CUSTOMERS")
print(df_customers)
print("-" * 40)

print("CLEANED ORDERS")
print(df_orders)
print("-" * 40)

df_orders["order_date"] = pd.to_datetime(df_orders["order_date"])
df_orders["month"] = df_orders["order_date"].dt.month

print("ORDERS WITH MONTH")
print(df_orders)
print("-" * 40)

df_merged = pd.merge(
    df_orders,
    df_customers,
    on="customer_id",
    how="left"
)

print("MERGED DATA")
print(df_merged)
print("-" * 40)

revenue_by_country = df_merged.groupby("country")["revenue"].sum()
print("REVENUE BY COUNTRY")
print(revenue_by_country)
print("-" * 40)

revenue_by_month = df_merged.groupby("month")["revenue"].sum()
print("REVENUE BY MONTH")
print(revenue_by_month)
print("-" * 40)

revenue_by_customer = (
    df_merged
    .groupby("customer_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("REVENUE BY CUSTOMER")
print(revenue_by_customer)
print("-" * 40)

print("TOP CUSTOMER")
print(revenue_by_customer.head(1))
