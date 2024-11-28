import pandas as pd
import uuid
from faker import Faker
import random

# Initialize Faker to generate fake data
fake = Faker()

# Number of records (orders) to generate
num_records = 4000  # Fewer orders, but each order has multiple items

# Pre-defined lists of supermarket products, categories, and fixed prices
products = [
    ("Apple", "Fruits", 1.50),
    ("Banana", "Fruits", 0.30),
    ("Carrot", "Vegetables", 2.00),
    ("Tomato", "Vegetables", 2.50),
    ("Chicken Breast", "Meat", 8.00),
    ("Beef Steak", "Meat", 12.00),
    ("Milk", "Dairy", 3.50),
    ("Cheese", "Dairy", 5.00),
    ("Bread", "Bakery", 2.50),
    ("Cake", "Bakery", 15.00)
]

# Generate unique IDs for products and categories
product_ids = {name: str(uuid.uuid4()) for name, _, _ in products}
category_ids = {category: str(uuid.uuid4()) for _, category in set((name, category) for name, category, _ in products)}

# Set for storing unique emails to ensure no duplicates
used_emails = set()

# List to store all generated data
data = []

# Loop to generate each order
for _ in range(num_records):
    # Generate unique IDs for customer and order
    customer_id = str(uuid.uuid4())
    order_id = str(uuid.uuid4())

    # Generate a unique email for the customer
    email = fake.email()
    while email in used_emails:
        email = fake.email()
    used_emails.add(email)

    # Generate fake data for the customer and order
    customer_name = fake.name()
    order_date = fake.date_between(start_date='-2y', end_date='today')
    phone_number = fake.phone_number()
    address = fake.street_address()
    city = fake.city()
    state = fake.state_abbr()
    zip_code = fake.zipcode()
    order_status = random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])
    payment_method = random.choice(["Credit Card", "PayPal", "Bank Transfer"])


    # Random number of products per order
    num_products = random.randint(1, 5)
    total_order_value = 0
    products_list = []
    selected_products = set()  # Set to track products already selected for this order

    # Loop to generate product details for the order
    while len(selected_products) < num_products:
        product_choice = random.choice(products)
        product_name = product_choice[0]

        if product_name not in selected_products:
            selected_products.add(product_name)
            category_name, price = product_choice[1], product_choice[2]
            product_id = product_ids[product_name]
            category_id = category_ids[category_name]
            quantity = random.randint(1, 10)
            total_product_price = round(price * quantity, 2)
            total_order_value += total_product_price

            # Collect individual product info
            products_list.append([product_id, product_name, category_id, category_name, price, quantity, total_product_price])

    # Generate random shipping cost and add to total order value
    shipping_cost = round(random.uniform(5.0, 20.0), 2)
    total_order_value += shipping_cost

    # Append data for each product in the order to the main data list
    for product in products_list:
        data.append([
            order_id, order_date, customer_id, customer_name, email, phone_number, address, city, state, zip_code,
            product[0], product[1], product[2], product[3], product[4], product[5], product[6],
            order_status, payment_method, shipping_cost, total_order_value
        ])

# Define the column names for the DataFrame
columns = ["OrderID", "OrderDate", "CustomerID", "CustomerName", "Email", "PhoneNumber", "Address", "City", "State", "ZipCode", "ProductID", "ProductName", "CategoryID", "CategoryName", "Price", "Quantity", "TotalProductPrice", "OrderStatus", "PaymentMethod", "ShippingCost", "TotalOrderValue"]

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to an Excel file
df.to_excel("orders_data.xlsx", index=False)

print("SpreadSheet 'orders_data.xlsx' successfully created!")
