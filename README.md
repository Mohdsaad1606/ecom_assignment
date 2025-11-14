This project demonstrates a complete miniature data engineering workflow using Python, SQLite, and SQL.
It simulates an e-commerce environment, generates synthetic data, loads it into a database, and performs a multi-table analytical SQL query.

📌 Project Overview

This project includes:

✔ Synthetic e-commerce data generation

✔ SQLite database creation

✔ Five related tables:

customers

products

orders

order_items

reviews

✔ Python scripts to ingest and query the database

✔ An analytical SQL query joining multiple tables

✔ Output displayed through Python (no SQLite CLI required)

This satisfies a typical data engineering assignment workflow end-to-end.

📂 Project Structure
ecom_assignment/
│
├── setup_ecommerce.py      # Creates the DB, tables, and loads all synthetic data
├── run_query.py            # Executes the SQL query and prints results
├── top_customers.sql       # Multi-table join SQL query
├── test_db.py              # Verifies tables + row counts
├── ecommerce.db            # Auto-generated SQLite database
└── README.md               # Project documentation

🔧 Technologies Used

Python 3.x

SQLite

Faker (data generation)

SQL

Cursor IDE

Git / GitHub

⚙️ 1. Generating the Database

Run:

python setup_ecommerce.py


This will:

Create ecommerce.db

Generate synthetic:

customers

products

orders

order_items

reviews

Insert all data into tables

Output:

Database created successfully!

📊 2. SQL Query (top_customers.sql)

This SQL file contains the analytical query that joins five tables:

SELECT 
    c.customer_id,
    c.name AS customer_name,
    SUM(oi.quantity * p.price) AS total_spent,
    COUNT(DISTINCT o.order_id) AS total_orders,
    AVG(r.rating) AS avg_rating_given
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN reviews r ON p.product_id = r.product_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;


This query calculates the top customers by total spending.

🏃‍♂️ 3. Running the SQL Query

Run:

python run_query.py


Example Output:

=== QUERY OUTPUT ===

['customer_id', 'customer_name', 'total_spent', 'total_orders', 'avg_rating_given']
(3, 'Customer_3', 36916.47, 2, 3.6)
(1, 'Customer_1', 36358.56, 5, 4.0)
(2, 'Customer_2', 21156.48, 3, 3.8)

🧪 4. Testing the Database

Run:

python test_db.py


Expected:

TABLES:
[('customers',), ('products',), ('orders',), ('order_items',), ('reviews',)]

Row counts:
customers 20
products 10
orders 30
order_items 45
reviews 40

✅ Assignment Requirements Achieved

✔ Data generation
✔ Database ingestion
✔ Multi-table SQL joins
✔ Analytical output
✔ Code organized & documented
✔ Uploaded to GitHub

👤 Author

Mohammed Saad
