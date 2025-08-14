'''
Handles product catalog and category management for the shopping app.
users can only view products, while admins can view, add, update, or delete products and categories.
'''

from shopping_app import data, auth

# Functios to view products and categories (All Roles)
def view_categories():
    print("Available Categories:")
    for category_id, category_name in data.categories_db.items():
        print(f"ID:{category_id} | Name: {category_name}")
    
def view_products():
    print("Available Products:")
    for product_id, product_info in data.products_db.items():
        category_name = data.categories_db[product_info['category_id']]
        print(f"ID:{product_id} | Name: {product_info['name']} | Category: {category_name} | Price: ${product_info['price']} | Stock: {product_info['stock']}")


# Functions for Admins to manage products and categories
def add_product(session_id, product_id,name, category_id, price):
    if not auth.check_role(session_id,'admin'):
        print("Access Denied, only Admin can add products")
        return
    if product_id in data.products_db:
        print("Product already exists")
        return
    if category_id not in data.categories_db:
        print("Invalid category ID.")
        return
    data.products_db[product_id] = {
        "name": name,
        'price': price,
        'category_id': category_id
    }
    print(f"Product '{name}' added successfully.")       


# Function to update products and categories
def update_product(session_id, product_id, name=None, category_id= None, price=None):
    if not auth.check_role(session_id,'admin'):
        print("Access Denied, only Admin can update products")
        return
    if product_id not in data.products_db:
        print("Product not found")
        return
    
    if name:
        data.products_db[product_id]["name"] = name
    if category_id:
        data.products_db[product_id]["category_id"] = category_id
    if price:
        data.products_db[product_id]["price"] = price   
    '''
    if stock:
        data.products_db[product_id]["stock"] = stock  
    '''

    print(f"Product '{product_id}' updated succesfully")

# Function to delete products 
def delete_product(session_id, product_id):
    if not auth.check_role(session_id,'admin'):
        print("Access Denied, only Admin can delete products")
        return

    if product_id not in data.products_db:
        print("Product not found")
        return
    
    del data.products_db[product_id]
    print(f"Product '{product_id}' deleted succesfully.")

# Functions of category management
# Funtion to add categories
def add_category(session_id, category_id, name):
    if not auth.check_role(session_id,'admin'):
        print("Access Denied, only Admin can delete products")
        return

    if category_id in data.categories_db:
        print("Category ID already exists.")
        return

    data.categories_db[category_id] = name
    print(f"Category '{category_id}' added succesfully.")

# Function to delete categories
def delete_category(session_id, category_id):
    if not auth.check_role(session_id,'admin'):
        print("Access Denied, only Admin can delete products")
        return

    if category_id not in data.categories_db:
        print("Caategory not found")
        return
    
    data.products_db = {
        prod_id: prod for prod_id, prod in data.products_db.items()
        if prod['category_id'] != category_id
    }
    del data.categories_db[category_id]
    print(f"Category '{category_id}' deleted succesfully.")