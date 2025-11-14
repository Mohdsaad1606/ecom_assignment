import sqlite3
import pandas as pd

# Connect to SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect("ecommerce.db")

# Define CSV files and table names
files = {
    "products": "products.csv",
    "customers": "customers.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "reviews": "reviews.csv"
}

# Load each CSV into a SQLite table
for table, csv_file in files.items():
    df = pd.read_csv(csv_file)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"✅ Loaded {csv_file} into table '{table}'")

conn.close()
print("🎯 All CSV files successfully imported into ecommerce.db")
