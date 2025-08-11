''' 
This file contans all the in-memory database structure for the shopping app.
Since we do not have any database set up, we will use a dictionary to simulate the database.
'''

# USER and Admin accounts
# Key: username, Value: dictionary with passwords and roles
users_db = {
    'user1': {'password': 'password1', 'role': 'user'},
    'user2': {'password': 'password2', 'role': 'user'},
    'user3': {'password': 'password3', 'role': 'user'},}
admins_db = {
    'admin1': {'password': 'adminpass1', 'role': 'admin'}, 
    'admin2': {'password': 'adminpass2', 'role': 'admin'},}

#Product Categories
# Key: category_id, Value: category name
categories_db = {
    1: 'Electronics',
    2: 'Clothing',
    3: 'Footwear'}

# Products catalog
# Key: product_id, Value: dictionary with product details
products_db = {
    101: {'name': 'Smartphone', 'category_id': 1, 'price': 699.99, 'stock': 50},
    102: {'name': 'Laptop', 'category_id': 1, 'price': 999.99, 'stock': 30},
    201: {'name': 'T-Shirt', 'category_id': 2, 'price': 19.99, 'stock': 100},
    202: {'name': 'Jeans', 'category_id': 2, 'price': 39.99, 'stock': 80},
    301: {'name': 'Sneakers', 'category_id': 3, 'price': 59.99, 'stock': 60},
    302: {'name': 'Boots', 'category_id': 3, 'price': 89.99, 'stock': 40}
}

# Shopping Cart
# Key: session_id, Value: dictionary with cart items
cart_db = {}