import pandas as pd

# Load dataset
file_path = "../data/online_retail_II.xlsx"

df = pd.read_excel(file_path)

# Display basic information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
#  DATA CLEANING
# -----------------------------

# Remove rows without Customer ID
df = df.dropna(subset=["Customer ID"])

# Remove cancelled transactions
df = df[~df["Invoice"].astype(str).str.startswith("C")]

# Keep only positive quantities and prices
df = df[df["Quantity"] > 0]
df = df[df["Price"] > 0]

# Create Total Amount column
df["TotalAmount"] = df["Quantity"] * df["Price"]

print("\nAfter Cleaning:")
print("Rows:", len(df))
print("Unique Customers:", df["Customer ID"].nunique())

print("\nCleaned Data:")
print(df.head())

# -----------------------------
#  REPEAT PURCHASE ANALYSIS
# -----------------------------

# Count unique invoices for each customer
customer_purchases = df.groupby("Customer ID")["Invoice"].nunique()

# Total customers
total_customers = customer_purchases.count()

# Repeat customers = customers with more than 1 purchase
repeat_customers = (customer_purchases > 1).sum()

# First-time customers
first_time_customers = (customer_purchases == 1).sum()

# Repeat purchase rate
repeat_rate = (repeat_customers / total_customers) * 100

print("\n--- Repeat Purchase Analysis ---")
print("Total Customers:", total_customers)
print("First-Time Customers:", first_time_customers)
print("Repeat Customers:", repeat_customers)
print("Repeat Purchase Rate: {:.2f}%".format(repeat_rate))

# -----------------------------
#  FIRST-TIME VS REPEAT AOV
# -----------------------------

# Purchase count for each customer
customer_purchase_count = df.groupby("Customer ID")["Invoice"].nunique()

# Customer type
customer_type = customer_purchase_count.apply(
    lambda x: "Repeat Customer" if x > 1 else "First-Time Customer"
)

# Total spending by customer
customer_spending = df.groupby("Customer ID")["TotalAmount"].sum()

# Create customer summary
customer_summary = pd.DataFrame({
    "PurchaseCount": customer_purchase_count,
    "CustomerType": customer_type,
    "TotalSpending": customer_spending
})

# Calculate average order value
aov_comparison = customer_summary.groupby("CustomerType")["TotalSpending"].mean()

print("\n--- First-Time vs Repeat AOV ---")
print(aov_comparison)

# -----------------------------
#  CUSTOMER SEGMENTATION
# -----------------------------

def assign_segment(purchases):
    if purchases == 1:
        return "One-Time"
    elif purchases <= 4:
        return "Repeat"
    else:
        return "Loyal"


customer_summary["Segment"] = customer_summary["PurchaseCount"].apply(assign_segment)

# Segment summary
segment_table = customer_summary.groupby("Segment").agg(
    Customers=("PurchaseCount", "count"),
    Avg_Purchases=("PurchaseCount", "mean"),
    Avg_Spending=("TotalSpending", "mean")
).reset_index()

print("\n--- Customer Segment Table ---")
print(segment_table)

# -----------------------------
#  SAVE OUTPUTS
# -----------------------------

# Save customer-level analysis
customer_summary.to_csv(
    "../outputs/customer_summary.csv",
    index=True
)

# Save segment table
segment_table.to_csv(
    "../outputs/customer_segments.csv",
    index=False
)

# Save AOV comparison
aov_comparison.to_csv(
    "../outputs/aov_comparison.csv"
)

# Save overall repeat purchase metrics
metrics = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "First-Time Customers",
        "Repeat Customers",
        "Repeat Purchase Rate"
    ],
    "Value": [
        total_customers,
        first_time_customers,
        repeat_customers,
        round(repeat_rate, 2)
    ]
})

metrics.to_csv(
    "../outputs/repeat_purchase_metrics.csv",
    index=False
)

print("\n--- Outputs Saved Successfully ---")
print("Files saved in outputs folder.")