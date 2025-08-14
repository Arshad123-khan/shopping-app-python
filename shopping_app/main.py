from shopping_app import auth, catalog, cart, payment, utils

def main():
    while True:
        utils.clear_screen()
        print("=== Welcome to the Demo Marketplace ===")
        print("1. User Login")
        print("2. Admin login")
        print("3. Exit")
        choice = utils.get_int_input("Emter Choice: ")

        if choice == 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            session_id = auth.authenticate_user(username, password, "user")
            if session_id:
                user_menu(session_id)
        elif choice == 2:
            username = input("Enter Admin Username: ")
            password = input("Enter Password: ")
            session_id = auth.authenticate_user(username, password, "admin")
            if session_id:
                admin_menu(session_id)
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            utils.pause()

def user_menu(session_id):
    while True:
        utils.clear_screen()
        print("\n---USER MENU---")
        print("1. View Products")
        print("2. View Categories")
        print("3. Add to Cart")
        print("4. Remove from the Cart")
        print("5. View Cart")
        print("6. Checkout")
        print("7. Logout")
        choice = utils.get_int_input("Enter choice: ")

        if choice ==1:
            catalog.view_products()
        elif choice == 2:
            catalog.view_categories()
        elif choice == 3:
            pid = utils.get_int_input("Enter Product ID: ")
            qty = utils.get_int_input("Enter quantity: ")
            cart.add_to_cart(session_id, pid, qty)
        elif choice == 4:
            pid = utils.get_int_input("Enter the Product ID to remove: ")
            cart.remove_from_cart(session_id, pid)
        elif choice == 5:
            cart.view_cart(session_id)
        elif choice == 6:
            payment.checkout(session_id)
        elif choice == 7:
            print("Logged out auccessfully.")
            break
        else:
            print("Invalid choice.")

        utils.pause()

def admin_menu(session_id):
    while True:
        utils.clear_screen()
        print("\n---ADMIN MENU---")
        print("1. View Products")
        print("2. View Categories")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Add Category")
        print("7. Delete Category")
        print("8. Logout")
        choice = utils.get_int_input("Enter choice: ")

        if choice == 1:
            catalog.view_products()
        elif choice == 2:
            catalog.add_category()
        elif choice == 3:
            pid = utils.get_int_input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            cid = utils.get_int_input("Enter Category ID: ")
            price = float(input("Enter the price: "))
            stock = utils.get_int_input("Enter Stock: ")
            catalog.add_product(session_id, pid, name, cid, price)

            # Manually adding stock
            if pid in catalog.data.products_db:
                catalog.data.products_db[pid]["stock"] = stock
        elif choice == 4:
            pid = utils.get_int_input("Enter Product ID to update: ")
            name = input("Enter new Name (leave balnk to skip): ")
            cid = input("Enter new Category ID (leave blank to skip): ")
            cid = int(cid) if cid.strip() else None
            price = input("Enter the price (leave blank to skip): ")
            price = float(price) if price.strip() else None
            catalog.update_product(session_id, pid, name or None, cid, price)
        elif choice == 5:
            pid = utils.get_int_input("Enter Product ID: ")
            catalog.delete_product(session_id, pid)
        elif choice == 6:
            cat_id = utils.get_int_input("Enter Category ID: ")
            name = input("Enter Category Name: ")
            catalog.add_category(session_id, cat_id, name)
        elif choice == 7:
            cat_id = utils.get_int_input("enter Category ID to delete: ")
            catalog.delete_category(session_id, cat_id)
        elif choice == 8:
            print("Logged out successfully.")
            break
        else:
            print("Invalid Choice.")

        utils.get_int_input()


if __name__ == "__main__":
    main()



        