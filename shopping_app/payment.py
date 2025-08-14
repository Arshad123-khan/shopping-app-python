'''
This file simulates checkout and payment method.
Reduces product stock upon successful payment.
'''

from shopping_app import data, auth

#Available payment methods
payment_methods = ["UPI", "Credit Card", "Net Banking" ]

def checkout(session_id):
    if not auth.check_role(session_id, "user"):
        print("Access denied, only users can checkout.")
        return
    
    cart = data.cart_db.get(session_id,[])
    if not cart:
        print("Your cart is empty. Add items before checkout")
        return
    
    # Calculate total price and check for stock availability again.
    total = 0
    for item in cart:
        product = data.products_db.get(item["product_id"])
        if not product:
            print(f"Product ID {item["product_id"]} not found. Removing from cart.")
            continue
        if item["quantity"] > product["stock"]:
            print(f"Not enough stock for{product["name"]}. Available: {product["stock"]}")
            return
        total += product["price"]*item["quantity"]

    # Display payment methods
    print("\n-- Checkout --")
    print(f"Total Amount: ${total}")
    print("Available Payment Methods:")
    for i, method in enumerate(payment_methods, start=1):
        print(f"{i}. {method}")

    #Get user choice
    try:
        choice = int(input("Select payment method (1/2/3): "))
        if choice < 1 or choice > len(payment_methods):
            print("Invalid payment method.")
            return
    except ValueError:
        print("Ivalid input. Enter a number.")
        return
    
    payment_method = payment_methods[choice - 1]
    print(f"Payment succesful via {payment_method}. Thank you for shopping!")

    # Reduce stock after successful payment
    for item in cart:
        product = data.products_db[item["product_id"]]
        product["stock"] -= item["quantity"]

    # Clear cart after checkout
    data.cart_db[session_id] = []
    print("Your order has been placed successfully!")

