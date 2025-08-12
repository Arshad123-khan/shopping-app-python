'''
Handles shopping cart operations for users.
Admins are restricted from performing these actions.
'''

from shopping_app import data, auth

# Function to view cart
def view_cart(session_id):
    if not auth.check_role(session_id, "user"):
        print("Access Denied, only users can access cart.")
        return
    cart = data.cart_db.get(session_id,[])
    if not cart:
        print("Your cart is empty.")
        return
    
    print("\n -- Your Cart---")
    total = 0
    for items in  cart:
        product = data.products_db.get(items['product_id'])
        if product:
            subtotal = product['price'] * items['quantity']
            total += subtotal
            print(f"{product['name']} (x{items['quantity']}) - ${subtotal}")
        print(f"Total: {total}")

# Funtion to add items to the cart
def add_to_cart(session_id, product_id, quantity):
    if not auth.check_role(session_id, "user"):
        print("Access Denied, only users can access cart.")
        return
    if product_id not in data.products_db:
        print("Product not found.")
        return
    
    product = data.products_db[product_id]

    # Check stock availability
    if quantity > product['stock']:
        print(f"Not enough stock for {product['name']}. Available: {product['stock']}")
        return
    
    cart = data.cart_db.setdefault(session_id,[])

    # Check if the product already exists in the cart
    for items in cart:
        if items['product_id'] == product_id:
            if items['quantity'] + quantity > product['stock']:
                print(f"Cannot add more than {product['stock']} units of {product['name']}.")
                return
            items['quantity'] += quantity
            print(f" Updated quantity of {product['name']} to {items['quantity']}.")
            return
        
    cart.append({"product_id": product_id, "quantity": quantity})
    print(f"Added {quantity} x {product['name']} to the cart.")

# Function to remove the item from cart
def remove_from_cart(session_id, product_id):
    if not auth.check_role(session_id, "user"):
        print("Access Denied, only users can access cart.")
        return
    '''
    if product_id not in data.products_db:
        print("Product not found.")
        return
    '''
    cart = data.cart_db.get(session_id,[])
    updated_cart = [item for item in cart if item["product_id"] != product_id]

    if len(updated_cart) == len(cart):
        print("Product not foundd in the cart.")
    else:
        data.cart_db[session_id] = updated_cart
        print(f"Removed product {product_id} from cart.")

# Function to clear cart
def clear_cart(session_id):
        if not auth.check_role(session_id, "user"):
            print("Access Denied, only users can access cart.")
            return
        data.cart_db[session_id] =[]
        print("Cart cleared succesfully.")