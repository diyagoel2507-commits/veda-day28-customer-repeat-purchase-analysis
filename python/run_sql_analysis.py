import sqlite3
import pandas as pd

# Load customer summary created by Python
csv_path = "outputs/customer_summary.csv"

df = pd.read_csv(csv_path)

# Create SQLite database
conn = sqlite3.connect("outputs/customer_analysis.db")

# Create table from CSV
df.to_sql("customer_summary", conn, if_exists="replace", index=False)

# Read and execute SQL file
with open("sql/repeat_purchase_analysis.sql", "r") as file:
    sql_script = file.read()

# Split queries using semicolon
queries = [q.strip() for q in sql_script.split(";") if q.strip()]

print("\n========== SQL ANALYSIS RESULTS ==========\n")

for query in queries:
    # Ignore comments
    result = pd.read_sql_query(query, conn)

    print(result.to_string(index=False))
    print("\n------------------------------------------\n")

conn.close()

print("SQL analysis completed successfully!")