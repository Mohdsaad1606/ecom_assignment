import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

query = open("top_customers.sql", "r").read()

results = cursor.execute(query).fetchall()
columns = [desc[0] for desc in cursor.description]

print("\n=== QUERY OUTPUT ===\n")
print(columns)
for row in results:
    print(row)

conn.close()
