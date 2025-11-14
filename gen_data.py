import pandas as pd
import random
import string

# Generate Products
products = pd.DataFrame({
    "product_id": range(1, 11),
    "product_name": [f"Product_{i}" for i in range(1, 11)],
    "price": [round(random.uniform(10, 100), 2) for _ in range(10)]
})
products.to_csv("products.csv", index=False)

# Generate Customers
customers = pd.DataFrame({
    "customer_id": range(1, 6),
    "name": [f"Customer_{i}" for i in range(1, 6)],
    "email": [f"cust{i}@example.com" for i in range(1, 6)]
})
customers.to_csv("customers.csv", index=False)

# Generate Orders
orders = pd.DataFrame({
    "order_id": range(1, 11),
    "customer_id": [random.randint(1, 5) for _ in range(10)],
    "order_date": pd.date_range("2025-01-01", periods=10).strftime("%Y-%m-%d")
})
orders.to_csv("orders.csv", index=False)

# Generate Order Items
order_items = pd.DataFrame({
    "order_item_id": range(1, 21),
    "order_id": [random.randint(1, 10) for _ in range(20)],
    "product_id": [random.randint(1, 10) for _ in range(20)],
    "quantity": [random.randint(1, 5) for _ in range(20)]
})
order_items.to_csv("order_items.csv", index=False)

# Generate Reviews
reviews = pd.DataFrame({
    "review_id": range(1, 11),
    "product_id": [random.randint(1, 10) for _ in range(10)],
    "rating": [random.randint(1, 5) for _ in range(10)],
    "comment": [f"Review {i}" for i in range(1, 10)] + ["Excellent!"]
})
reviews.to_csv("reviews.csv", index=False)

print("✅ Synthetic e-commerce data generated successfully!")
