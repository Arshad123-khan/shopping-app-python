from shopping_app import auth, catalog, cart
'''
# Admin Login
admin_session = auth.authenticate_user("admin1", "adminpass1", "admin")

if admin_session:    
    catalog.view_products()  # View current products   
    catalog.add_category(admin_session, 4, "Accessories") # Add new category   
    catalog.add_product(admin_session, 401, 'Sun Glasses',4, 150, 10) #Add new product
    catalog.view_products # View updated catalog
else:
    print("Could not login as admin. Please check credentials.")
'''
# User Login
user_session = auth.authenticate_user('user1','password1','user')

if user_session:
    catalog.view_products()
    cart.add_to_cart(user_session,101,5) #Should pass
    cart.add_to_cart(user_session,101, 500) # Should fail
    cart.add_to_cart(user_session, 301, 3) # Should pass
    cart.view_cart(user_session)
    cart.remove_from_cart(user_session, 102)
    cart.view_cart(user_session)
else:
    print("Could not log in as user.")